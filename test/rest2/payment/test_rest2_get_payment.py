from faker import Factory
from hamcrest import assert_that, instance_of

from constants import ApiKey
from data.rest2_payment_requests import rest2_payment_moto
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '21001'
KEY = db.get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)
go_boarding = WNClient().vagrant.go.boarding()


def test_get_payment_valid():
    payment_response = wn.payment(request=rest2_payment_moto(), api2_key=KEY)
    get_payment_response = wn.get_payment(uniqueref=payment_response.unique_reference, api2_key=KEY, silence=False)
    assert_that(get_payment_response, instance_of(Payment))
