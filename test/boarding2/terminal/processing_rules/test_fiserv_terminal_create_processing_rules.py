import json

import deepdiff
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import LocalMerchant, ApiKey
from model.boarding2 import FiServTerminal
from model.boarding2 import ProcessingRule
from model.boarding2 import ProcessingRuleInstruction
from model.boarding2 import ProcessingRulePredicate
from wnclient import WNClient

wn = WNClient().local.goepay.boarding2()
db = WNClient().db()
GOEPAY_KEY = ApiKey.BOARDING_GOEPAY_FULL
fake = Factory().create()
TERM_ID = '22003'
FDRC_TERM_ID = '22004'


def test_fiserv_create_terminal_create_enable_processing_rules():
    key = db.get_api_key(GOEPAY_KEY)
    terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FiServTerminal, key, silence=False)
    processing_rules = [ProcessingRule(
        enable=True,
        conditions=[ProcessingRulePredicate(when='TENDER_TYPE', _is='EQUALS', value='CREDIT_DEBIT')],
        then=ProcessingRuleInstruction(action='ROUTE_TO_TERMINAL', terminal_number=FDRC_TERM_ID))]
    terminal.processing_rules = processing_rules
    terminal.secret = 'someSecretPhrase'

    response = wn.create_terminal(LocalMerchant.GOEPAY.itemid, terminal, FiServTerminal, key, silence=False)
    assert_that(response, instance_of(FiServTerminal))
    new_terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, response.terminal_number, FiServTerminal, key)

    # comparing processing_rules object only
    diff = json.dumps(
        json.loads(
            deepdiff.DeepDiff(terminal.processing_rules, new_terminal.processing_rules).to_json()
        ), indent=4)
    print(diff)
    assert_that(diff, equal_to('{}'))
