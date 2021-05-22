import json

import deepdiff
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import LocalMerchant, ApiKey
from model.boarding2 import FiServTerminal
from wnclient import WNClient

wn = WNClient().vagrant.wn.boarding2()
db = WNClient().db()
GOEPAY_KEY = ApiKey.BOARDING_WN_FULL
fake = Factory().create()
TERM_ID = '22008'


def test_fiserv_create_terminal_valid():
    key = db.get_api_key(GOEPAY_KEY)
    terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FiServTerminal, key)
    terminal.secret = 'someSecretPhrase'

    response = wn.create_terminal(LocalMerchant.GOEPAY.itemid, terminal, FiServTerminal, key, silence=False)
    assert_that(response, instance_of(FiServTerminal))
    new_terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, response.terminal_number, FiServTerminal, key)

    terminal.terminal_number = new_terminal.terminal_number
    terminal.secret = None
    diff = json.dumps(
        json.loads(
            deepdiff.DeepDiff(terminal.to_dict(), new_terminal.to_dict()).to_json()
        ), indent=4)
    print(diff)
    assert_that(diff, equal_to('{}'))
