import json

import deepdiff
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, none, not_none

from constants import LocalMerchant, ApiKey
from model.boarding2 import Error
from model.boarding2 import FiServTerminal
from model.boarding2 import ProcessingRule
from model.boarding2 import ProcessingRuleInstruction
from model.boarding2 import ProcessingRulePredicate
from utils import logger
from wnclient import WNClient

wn = WNClient().local.goepay.boarding2()
db = WNClient().db()
GOEPAY_KEY = ApiKey.BOARDING_GOEPAY_FULL
fake = Factory().create()
FDRC_TERM_ID = '22004'
TERM_ID = '22003'


def fiserv_processing_rule(is_enable=True, when='TENDER_TYPE', _is='EQUALS', value='CREDIT_DEBIT',
                           action='ROUTE_TO_TERMINAL', terminal_number=FDRC_TERM_ID):
    return ProcessingRule(enable=is_enable,
        conditions=[ProcessingRulePredicate(when=when, _is=_is, value=value)],
        then=ProcessingRuleInstruction(action=action, terminal_number=terminal_number))


def test_fiserv_terminal_update_enable_processing_rules():
    key = db.get_api_key(GOEPAY_KEY)
    terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FiServTerminal, key)
    assert_that(terminal.processing_rules, none(), 'Please disable alternative routing: Cards > Allow PaymentType routing')
    terminal.processing_rules = [fiserv_processing_rule(terminal_number=FDRC_TERM_ID)]
    terminal.secret = 'someSecretPhrase'

    response = wn.update_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, terminal, FiServTerminal, key, silence=False)
    assert_that(response, instance_of(FiServTerminal))
    assert_that(response.processing_rules, not_none())
    new_terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, response.terminal_number, FiServTerminal, key)

    diff = json.dumps(json.loads(deepdiff.DeepDiff(terminal.processing_rules,
                                                   new_terminal.processing_rules).to_json()), indent=4)
    logger.warning(diff)
    assert_that(diff, equal_to('{}'))


def test_fiserv_terminal_update_unassigned_processing_rules():
    # issue 28207
    unassigned_terminal = '22005'
    key = db.get_api_key(GOEPAY_KEY)
    terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FiServTerminal, key)
    assert_that(terminal.processing_rules, none(), 'Please disable alternative routing: Cards > Allow PaymentType routing')
    terminal.processing_rules = [fiserv_processing_rule(terminal_number=unassigned_terminal)]
    terminal.secret = 'someSecretPhrase'

    response = wn.update_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, terminal, FiServTerminal, key, silence=False)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('Secondary terminal is invalid'))
