from faker import Factory
from hamcrest import assert_that, instance_of

from constants import ApiKey
from data.rest2_credentials_requests import rest2_credentials_keyed
from data.rest2_payment_requests import rest2_credentials_payment
from model.rest2 import Payment
from model.rest2.secure_credentials import SecureCredentials
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '22001'
KEY = db.get_api_key(ApiKey.API_WN_FULL)
wn = WNClient().vagrant.wn.rest2(terminal_id=TERM_ID)


def test_credentials_payment_valid():
    response = wn.credentials_store(request=rest2_credentials_keyed(cardtype='visa'), api2_key=KEY, silence=False)
    assert_that(response, instance_of(SecureCredentials))

    payment_response = wn.payment(request=rest2_credentials_payment(response.credentials_number), api2_key=KEY)
    assert_that(payment_response, instance_of(Payment))
