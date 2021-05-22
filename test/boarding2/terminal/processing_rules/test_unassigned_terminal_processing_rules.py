from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import LocalMerchant, ApiKey
from model.boarding2 import Error
from model.boarding2 import ProcessingRule
from model.boarding2 import ProcessingRuleInstruction
from model.boarding2 import ProcessingRulePredicate
from model.boarding2 import UnassignedTerminal
from wnclient import WNClient

wn = WNClient().local.goepay.boarding2()
db = WNClient().db()
GOEPAY_KEY = ApiKey.BOARDING_GOEPAY_FULL
fake = Factory().create()
TERM_ID = '22031'
FISERV_TERM_ID = '22003'


def test_unassgined_terminal_not_allow_processing_rules():
    key = db.get_api_key(GOEPAY_KEY)
    terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, UnassignedTerminal, key, silence=False)
    processing_rules = [ProcessingRule(
        enable=True,
        conditions=[ProcessingRulePredicate(when='TENDER_TYPE', _is='EQUALS', value='EBT')],
        then=ProcessingRuleInstruction(action='ROUTE_TO_TERMINAL', terminal_number=FISERV_TERM_ID))]
    terminal.processing_rules = processing_rules
    terminal.secret = 'someSecretPhrase'

    response = wn.create_terminal(LocalMerchant.GOEPAY.itemid, terminal, UnassignedTerminal, key, silence=False)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('Unable to deserialize value'))
    assert_that(response.details[0].source._property, equal_to('processingRules'))
