from faker import Factory
from hamcrest import assert_that, instance_of

from constants import LocalMerchant, ApiKey
from model.boarding2 import FdrcTerminal
from wnclient import WNClient

wn = WNClient().vagrant.wn.boarding2()
db = WNClient().db()
API_KEY = ApiKey.BOARDING_WN_FULL
fake = Factory().create()
TERM_ID = '22008'


def test_fdrc_get_terminal_valid():
    key = db.get_api_key(API_KEY)
    response = wn.get_terminal(LocalMerchant.WN.itemid, TERM_ID, FdrcTerminal, key)
    assert_that(response, instance_of(FdrcTerminal))


def test_fdrc_get_terminal_template_valid():
    key = db.get_api_key(API_KEY)
    response = wn.get_terminal_template(terminal_name='fdrc_term_tpl', response_type=FdrcTerminal, boarding2_key=key)
    assert_that(response, instance_of(FdrcTerminal))
