import json

import deepdiff
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import LocalMerchant, ApiKey
from model.boarding2 import FiServTerminal
from wnclient import WNClient
fake = Factory.create()

wn = WNClient().local.goepay.boarding2()
db = WNClient().db()
GOEPAY_KEY = ApiKey.BOARDING_GOEPAY_FULL
TERM_ID = '22003'
FDRC_TERM_ID = '22004'


def test_fiserv_update_terminal_batch_time():
    key = db.get_api_key(GOEPAY_KEY)
    terminal: FiServTerminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FiServTerminal, key)
    terminal.secret = 'someSecretPhrase'
    terminal.bank_settings.batch_time = str(fake.date_time())[11:-3]
    update_terminal_response = wn.update_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, terminal, FiServTerminal, key, silence=False)
    assert_that(update_terminal_response, instance_of(FiServTerminal))

    terminal.secret = None
    diff = json.dumps(
        json.loads(
            deepdiff.DeepDiff(terminal.to_dict(), update_terminal_response.to_dict()).to_json()
        ), indent=4)
    print(diff)
    assert_that(diff, equal_to('{}'))

    get_updated_terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, update_terminal_response.terminal_number, FiServTerminal, key)

    diff = json.dumps(
        json.loads(
            deepdiff.DeepDiff(terminal.to_dict(), get_updated_terminal.to_dict()).to_json()
        ), indent=4)
    print(diff)
    assert_that(diff, equal_to('{}'))
