import json

import deepdiff
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import LocalMerchant, ApiKey
from model.boarding2 import TsysSaratogaTerminal
from wnclient import WNClient

wn = WNClient().local.go.boarding2()
db = WNClient().db()
GO_KEY = ApiKey.BOARDING_GO_FULL
fake = Factory().create()
TERM_ID = '21001'


def test_tsys_saratoga_update_terminal_valid():
    key = db.get_api_key(GO_KEY)
    terminal: TsysSaratogaTerminal = wn.get_terminal(LocalMerchant.GO.itemid, TERM_ID, TsysSaratogaTerminal, key)
    terminal.secret = 'someSecretPhrase'
    terminal.bank_settings.customer_service_email = fake.free_email()

    update_terminal_response = wn.update_terminal(LocalMerchant.GO.itemid, TERM_ID, terminal, TsysSaratogaTerminal, key)
    assert_that(update_terminal_response, instance_of(TsysSaratogaTerminal))

    terminal.secret = None
    diff = json.dumps(
        json.loads(
            deepdiff.DeepDiff(terminal.to_dict(), update_terminal_response.to_dict()).to_json()
        ), indent=4)
    print(diff)
    assert_that(diff, equal_to('{}'))

    get_updated_terminal = wn.get_terminal(LocalMerchant.GO.itemid, update_terminal_response.terminal_number, TsysSaratogaTerminal, key)

    diff = json.dumps(
        json.loads(
            deepdiff.DeepDiff(terminal.to_dict(), get_updated_terminal.to_dict()).to_json()
        ), indent=4)
    print(diff)
    assert_that(diff, equal_to('{}'))
