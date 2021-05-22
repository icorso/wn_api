import json

import deepdiff
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, none, not_none

from constants import LocalMerchant, ApiKey
from model.boarding2 import FdrcTerminal
from model.boarding2 import ProcessingRule
from model.boarding2 import ProcessingRuleInstruction
from model.boarding2 import ProcessingRulePredicate
from utils import logger
from wnclient import WNClient

wn = WNClient().local.goepay.boarding2()
db = WNClient().db()
GOEPAY_KEY = ApiKey.BOARDING_GOEPAY_FULL
fake = Factory().create()
TERM_ID = '22004'
FISERV_TERM_ID = '22003'


def fdrc_processing_rule(is_enable=True, when='TENDER_TYPE', _is='EQUALS', value='EBT', action='ROUTE_TO_TERMINAL',
                         terminal_number=FISERV_TERM_ID):
    return ProcessingRule(
        enable=is_enable,
        conditions=[ProcessingRulePredicate(when=when, _is=_is, value=value)],
        then=ProcessingRuleInstruction(action=action, terminal_number=terminal_number)
    )


def test_fdrc_terminal_create_enable_processing_rules():
    key = db.get_api_key(GOEPAY_KEY)
    terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FdrcTerminal, key)
    processing_rules = [fdrc_processing_rule()]
    terminal.processing_rules = processing_rules
    terminal.secret = 'someSecretPhrase'

    response = wn.create_terminal(LocalMerchant.GOEPAY.itemid, terminal, FdrcTerminal, key, silence=False)
    assert_that(response, instance_of(FdrcTerminal))
    assert_that(response.processing_rules, not_none())
    new_terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, response.terminal_number, FdrcTerminal, key)

    diff = json.dumps(
        json.loads(    # comparing processing_rules object only
            deepdiff.DeepDiff(terminal.processing_rules, new_terminal.processing_rules).to_json()
        ), indent=4)
    logger.warning(diff)
    assert_that(diff, equal_to('{}'))


def test_fdrc_terminal_create_disable_processing_rules():
    key = db.get_api_key(GOEPAY_KEY)
    terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FdrcTerminal, key)
    processing_rules = [fdrc_processing_rule(is_enable=False)]
    terminal.processing_rules = processing_rules
    terminal.secret = 'someSecretPhrase'

    response = wn.create_terminal(LocalMerchant.GOEPAY.itemid, terminal, FdrcTerminal, key, silence=False)
    assert_that(response, instance_of(FdrcTerminal))
    assert_that(response.processing_rules, none())

    new_terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, response.terminal_number, FdrcTerminal, key)
    assert_that(new_terminal.processing_rules, none())
