import json

import deepdiff
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import LocalMerchant, ApiKey
from model.boarding2 import FiServTerminal, FdrcTerminal
from wnclient import WNClient

wn = WNClient().vagrant.wn.boarding2()
db = WNClient().db()
GOEPAY_KEY = ApiKey.BOARDING_WN_FULL
fake = Factory().create()
TERM_ID = '22005'


def test_fiserv_create_terminal_valid():
    key = db.get_api_key(GOEPAY_KEY)
    terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FdrcTerminal, key)
    terminal.secret = 'someSecretPhrase'

    response = wn.create_terminal(LocalMerchant.GOEPAY.itemid, terminal, FdrcTerminal, key, silence=False)
    assert_that(response, instance_of(FdrcTerminal))
    new_terminal = wn.get_terminal(LocalMerchant.GOEPAY.itemid, response.terminal_number, FdrcTerminal, key)

    terminal.terminal_number = new_terminal.terminal_number
    terminal.secret = None
    diff = json.dumps(
        json.loads(
            deepdiff.DeepDiff(terminal.to_dict(), new_terminal.to_dict()).to_json()
        ), indent=4)
    print(diff)
    assert_that(diff, equal_to('{}'))
