from faker import Factory
from hamcrest import assert_that, instance_of

from constants import LocalMerchant, ApiKey
from model.boarding2 import FiServTerminal
from wnclient import WNClient

wn = WNClient().local.goepay.boarding2()
db = WNClient().db()
GOEPAY_KEY = ApiKey.BOARDING_GOEPAY_FULL
fake = Factory().create()
TERM_ID = '22003'


def test_fiserv_get_terminal_valid():
    key = db.get_api_key(GOEPAY_KEY)
    response = wn.get_terminal(LocalMerchant.GOEPAY.itemid, TERM_ID, FiServTerminal, key)
    assert_that(response, instance_of(FiServTerminal))


def test_fiserv_get_terminal_template_valid():
    key = db.get_api_key(GOEPAY_KEY)
    response = wn.get_terminal_template(terminal_name='fiserv_term_tpl', response_type=FiServTerminal, boarding2_key=key)
    assert_that(response, instance_of(FiServTerminal))
