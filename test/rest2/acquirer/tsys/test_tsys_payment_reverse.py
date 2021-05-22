from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey
from data.rest2_payment_requests import rest2_payment_moto
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '21006'
KEY = WNClient().db().get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)


def test_payment_partial_reverse_valid():
    response = wn.payment(request=rest2_payment_moto(), api2_key=KEY)
    assert_that(response, instance_of(Payment))
    reverse_amount = round(response.order.total_amount / 2)

    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=reverse_amount,
        api2_key=KEY, silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.transaction_result.status, equal_to('READY'))
    assert_that(reversal_response.transaction_result.authorized_amount,
                equal_to(round(response.order.total_amount - reverse_amount)))

