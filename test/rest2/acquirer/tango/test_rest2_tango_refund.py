from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey, Currency
from data.rest2_payment_requests import rest2_payment_moto
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '21004'
KEY = WNClient().db().get_api_key(ApiKey.API_GO_FULL)
rest = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)
boarding = WNClient().vagrant.go.boarding()


def test_tango_partial_refund_ok():
    response = rest.payment(request=rest2_payment_moto(currency=Currency.CAD, cardtype='visa'), api2_key=KEY)
    assert_that(response, instance_of(Payment))

    refund_amount = round(response.order.total_amount / 2)
    refund_response = rest.payment_refund(response.unique_reference, refund_amount, api2_key=KEY, silence=False)
    assert_that(refund_response, instance_of(Payment))
    assert_that(refund_response.transaction_result.status, equal_to('READY'))
    assert_that(refund_response.transaction_result.authorized_amount, equal_to(refund_amount * -1))


def test_tango_refund_reverse_valid():
    response = rest.payment(request=rest2_payment_moto(currency=Currency.CAD, cardtype='visa'), api2_key=KEY)
    assert_that(response, instance_of(Payment))

    refund_amount = round(response.order.total_amount / 2)
    refund_response = rest.payment_refund(response.unique_reference, refund_amount, api2_key=KEY)
    assert_that(refund_response, instance_of(Payment))

    reversal_response = rest.refund_reverse(
        uniqueref=refund_response.unique_reference,
        api2_key=KEY, silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.transaction_result.status, equal_to('VOID'))
    assert_that(reversal_response.transaction_result.type, equal_to('REFUND'))
