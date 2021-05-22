import json

import deepdiff
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, none, not_none

from constants import LocalMerchant, ApiKey
from model.boarding2 import Error
from model.boarding2 import FdrcTerminal
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
TERM_ID = '22004'
FISERV_TERM_ID = '22003'


def fdrc_processing_rule(is_enable=True, when='TENDER_TYPE', _is='EQUALS', value='EBT', action='ROUTE_TO_TERMINAL',
                         terminal_number=FISERV_TERM_ID):
    return ProcessingRule(
        enable=is_enable,
        conditions=[ProcessingRulePredicate(when=when, _is=_is, value=value)],
        then=ProcessingRuleInstruction(action=action, terminal_number=terminal_number)
    )


def test_fdrc_terminal_update_enable_processing_rules():
    key = db.get_api_key(GOEPAY_KEY)
    terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FdrcTerminal, key)
    assert_that(terminal.processing_rules, none(), 'Please disable alternative routing: Cards > Allow PaymentType routing')
    terminal.processing_rules = [fdrc_processing_rule(terminal_number='22029')]
    terminal.secret = 'someSecretPhrase'

    response = wn.update_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, terminal, FdrcTerminal, key, silence=False)
    assert_that(response, instance_of(FdrcTerminal))
    assert_that(response.processing_rules, not_none())
    new_terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, response.terminal_number, FdrcTerminal, key)

    diff = json.dumps(json.loads(deepdiff.DeepDiff(terminal.processing_rules,
                                                   new_terminal.processing_rules).to_json()), indent=4)
    logger.warning(diff)
    assert_that(diff, equal_to('{}'))


def test_fdrc_terminal_update_disable_processing_rules():
    key = db.get_api_key(GOEPAY_KEY)
    terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FdrcTerminal, key)
    assert_that(terminal.processing_rules, not_none(), 'Please enable alternative routing: Cards > Allow PaymentType routing')
    terminal.processing_rules[0].enable = False
    terminal.secret = 'someSecretPhrase'

    response = wn.update_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, terminal, FdrcTerminal, key, silence=False)
    assert_that(response, instance_of(FdrcTerminal))
    assert_that(response.processing_rules, none())
    new_terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, response.terminal_number, FdrcTerminal, key)
    assert_that(new_terminal.processing_rules, none())


def test_fdrc_terminal_update_terminal_number_processing_rules():
    key = db.get_api_key(GOEPAY_KEY)

    # fdrc terminal alt routing to 22003
    terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FdrcTerminal, key)
    assert_that(terminal.processing_rules, not_none(), 'Please enable alternative routing: Cards > Allow PaymentType routing')

    # create new fiserv terminal
    fiserv_terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, FISERV_TERM_ID, FiServTerminal, key)
    fiserv_terminal.secret = 'someSecretPhrase'
    new_fiserv_terminal = wn.create_terminal(LocalMerchant.GOEPAY.itemid, fiserv_terminal, FiServTerminal, key)

    # update fdrc terminal with new alternative terminal
    terminal.processing_rules[0].then.terminal_number = new_fiserv_terminal.terminal_number
    terminal.secret = 'someSecretPhrase'
    response = wn.update_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, terminal, FdrcTerminal, key, silence=False)
    assert_that(response, instance_of(FdrcTerminal))
    assert_that(response.processing_rules, not_none())

    new_terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, response.terminal_number, FdrcTerminal, key)
    diff = json.dumps(json.loads(deepdiff.DeepDiff(terminal.processing_rules,
                                                   new_terminal.processing_rules).to_json()), indent=4)
    logger.warning(diff)
    assert_that(diff, equal_to('{}'))


def test_fdrc_terminal_update_inactive_terminal_processing_rules():
    inactive_fiserv_terminal = '22029'  # TODO create and deactivate fiserv terminal
    key = db.get_api_key(GOEPAY_KEY)
    terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FdrcTerminal, key)
    assert_that(terminal.processing_rules, none(), 'Please disable alternative routing: Cards > Allow PaymentType routing')
    terminal.processing_rules = [fdrc_processing_rule(terminal_number=inactive_fiserv_terminal)]
    terminal.secret = 'someSecretPhrase'

    response = wn.update_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, terminal, FdrcTerminal, key, silence=False)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('Secondary terminal is invalid'))
