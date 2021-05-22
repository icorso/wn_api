from faker import Factory
from hamcrest import assert_that, instance_of

from constants import ApiKey
from data.rest2_payment_requests import rest2_payment_moto
from model.rest2 import Error
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '22001'
INACTIVE_TERM = '22016'  # TODO
KEY = db.get_api_key(ApiKey.API_WN_FULL)
wn = WNClient().vagrant.wn.rest2(terminal_id=TERM_ID)


def test_payment_moto_inactive_terminal_keyed():
    p = rest2_payment_moto()
    response = wn.with_terminal(INACTIVE_TERM).payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Error))
