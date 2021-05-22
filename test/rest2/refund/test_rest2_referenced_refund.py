from faker import Factory
from hamcrest import assert_that, instance_of

from constants import ApiKey
from data.rest2_payment_requests import rest2_payment_moto
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '21001'
KEY = WNClient().db().get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)
wn_boarding = WNClient().vagrant.go.boarding()


def test_referenced_refund_ok():
    response = wn.payment(request=rest2_payment_moto(), api2_key=KEY)
    assert_that(response, instance_of(Payment))

    refund_amount = round(response.order.total_amount / 2)
    refund_response = wn.payment_refund(response.unique_reference, refund_amount, api2_key=KEY, silence=False)
    assert_that(refund_response, instance_of(Payment))
