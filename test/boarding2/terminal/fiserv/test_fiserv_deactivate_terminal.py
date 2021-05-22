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
API_KEY = ApiKey.BOARDING_WN_FULL
TERM_ID = '22003'
FDRC_TERM_ID = '22004'


def test_fiserv_deactivate_terminal():
    key = db.get_api_key(API_KEY)
    update_terminal_response = wn.deactivate_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FiServTerminal, key, silence=False)
    assert_that(update_terminal_response, instance_of(FiServTerminal))


def test_fiserv_activate_terminal():
    key = db.get_api_key(API_KEY)
    update_terminal_response = wn.activate_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FiServTerminal, key, silence=False)
    assert_that(update_terminal_response, instance_of(FiServTerminal))
