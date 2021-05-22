import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import LocalMerchant, ApiKey
from model.boarding2 import FdrcTerminal, Error
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


@pytest.mark.parametrize('value,error_message,expected', [
    ('TENDERTYPE', 'Unable to resolve type identifier', 'Known types: [TENDER_TYPE]'),
    ('TENDER_TYPE ', 'Unable to resolve type identifier', 'Known types: [TENDER_TYPE]'),
    (' TENDER_TYPE', 'Unable to resolve type identifier', 'Known types: [TENDER_TYPE]'),
    ('tender_type', 'Unable to resolve type identifier', 'Known types: [TENDER_TYPE]'),
    ('', 'Unable to resolve type identifier', 'Known types: [TENDER_TYPE]'),
    (None, 'Unable to resolve type identifier', 'Known types: [TENDER_TYPE]')
])
def test_tender_type_when_validation(value, error_message, expected):
    key = db.get_api_key(GOEPAY_KEY)
    terminal: FdrcTerminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FdrcTerminal, key)
    processing_rules = [fdrc_processing_rule(when=value)]
    terminal.processing_rules = processing_rules
    terminal.secret = 'someSecretPhrase'

    response = wn.create_terminal(LocalMerchant.GOEPAY.itemid, terminal, FdrcTerminal, key)
    logger.warning(response.json())
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to(error_message))
    assert_that(response.details[0].source.expected, equal_to(expected))


@pytest.mark.parametrize('value,error_message,expected', [
    ('EQUAL ', 'Unable to deserialize value', 'Acceptable values: [EQUALS]'),
    (' EQUAL', 'Unable to deserialize value', 'Acceptable values: [EQUALS]'),
    ('EQUAL', 'Unable to deserialize value', 'Acceptable values: [EQUALS]'),
    ('equals', 'Unable to deserialize value', 'Acceptable values: [EQUALS]'),
    ('', 'Unable to deserialize value', 'Acceptable values: [EQUALS]'),
    (None, 'must not be null', None)
])
def test_tender_type_is_validation(value, error_message, expected):
    key = db.get_api_key(GOEPAY_KEY)
    terminal: FdrcTerminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FdrcTerminal, key)
    processing_rules = [fdrc_processing_rule(_is=value)]
    terminal.processing_rules = processing_rules
    terminal.secret = 'someSecretPhrase'

    response = wn.create_terminal(LocalMerchant.GOEPAY.itemid, terminal, FdrcTerminal, key)
    logger.warning(response.json())
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to(error_message))
    assert_that(response.details[0].source.expected, equal_to(expected))


@pytest.mark.parametrize('value,error_message,expected', [
    ('CREDIT_DEBIT', 'Tender type not supported by the terminal', 'EBT'),
    ('EB', 'Unable to deserialize value', 'Acceptable values: [CREDIT_DEBIT, EBT]'),
    ('EBT ', 'Unable to deserialize value', 'Acceptable values: [CREDIT_DEBIT, EBT]'),
    (' EBT', 'Unable to deserialize value', 'Acceptable values: [CREDIT_DEBIT, EBT]'),
    ('ebt', 'Unable to deserialize value', 'Acceptable values: [CREDIT_DEBIT, EBT]'),
    ('', 'Unable to deserialize value', 'Acceptable values: [CREDIT_DEBIT, EBT]'),
    (None, 'Should be specified', None)
])
def test_tender_type_value_validation(value, error_message, expected):
    key = db.get_api_key(GOEPAY_KEY)
    terminal: FdrcTerminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FdrcTerminal, key)
    processing_rules = [fdrc_processing_rule(value=value)]
    terminal.processing_rules = processing_rules
    terminal.secret = 'someSecretPhrase'

    response = wn.create_terminal(LocalMerchant.GOEPAY.itemid, terminal, FdrcTerminal, key)
    logger.warn(response.json())
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to(error_message))
    assert_that(response.details[0].source.expected, equal_to(expected))


@pytest.mark.parametrize('value,error_message,expected', [
    ('ROUTE_TOTERMINAL', 'Unable to deserialize value', 'Acceptable values: [ROUTE_TO_TERMINAL]'),
    ('ROUTE_TO_TERMINAL ', 'Unable to deserialize value', 'Acceptable values: [ROUTE_TO_TERMINAL]'),
    (' ROUTE_TO_TERMINAL', 'Unable to deserialize value', 'Acceptable values: [ROUTE_TO_TERMINAL]'),
    ('route_to_terminal', 'Unable to deserialize value', 'Acceptable values: [ROUTE_TO_TERMINAL]'),
    ('', 'Unable to deserialize value', 'Acceptable values: [ROUTE_TO_TERMINAL]'),
    (None, 'must not be null', None)
])
def test_tender_type_action_validation(value, error_message, expected):
    key = db.get_api_key(GOEPAY_KEY)
    terminal: FdrcTerminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FdrcTerminal, key)
    processing_rules = [fdrc_processing_rule(action=value)]
    terminal.processing_rules = processing_rules
    terminal.secret = 'someSecretPhrase'

    response = wn.create_terminal(LocalMerchant.GOEPAY.itemid, terminal, FdrcTerminal, key)
    logger.warning(response.json())
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to(error_message))
    assert_that(response.details[0].source.expected, equal_to(expected))


@pytest.mark.parametrize('value,error_message', [
    ('21001', 'Resource not found'),
    ('', 'Resource not found'),
    (None, 'must not be null')
])
def test_tender_type_terminal_number_validation(value, error_message):
    key = db.get_api_key(GOEPAY_KEY)
    terminal: FdrcTerminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FdrcTerminal, key)
    processing_rules = [fdrc_processing_rule(terminal_number=value)]
    terminal.processing_rules = processing_rules
    terminal.secret = 'someSecretPhrase'
    logger.warning(processing_rules)
    response = wn.create_terminal(LocalMerchant.GOEPAY.itemid, terminal, FdrcTerminal, key)
    logger.warning(response.json())
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to(error_message))
