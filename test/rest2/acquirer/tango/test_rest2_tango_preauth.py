from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey, Currency
from data.rest2_payment_requests import rest2_payment_moto
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '21004'
KEY = db.get_api_key(ApiKey.API_GO_FULL)
rest2 = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)
boarding2 = WNClient().vagrant.go.boarding2()
"""
Testing of Tango acquirer pre-auth completion and void, see issue #31735
"""


def test_tango_preauth():
    request = rest2_payment_moto(currency=Currency.CAD, cardtype='visa')
    request.auto_capture = False
    response = rest2.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.type, equal_to('PREAUTH'))
    assert_that(response.transaction_result.status, equal_to('PENDING'))


def test_tango_preauth_completion():
    request = rest2_payment_moto(currency=Currency.CAD, cardtype='visa')
    request.auto_capture = False
    response = rest2.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.type, equal_to('PREAUTH'))
    assert_that(response.transaction_result.status, equal_to('PENDING'))

    capture_response = rest2.payment_capture(uniqueref=response.unique_reference,
                                             amount=response.order.total_amount,
                                             api2_key=KEY, silence=True)
    assert_that(capture_response, instance_of(Payment))
    assert_that(capture_response.transaction_result.result_message, equal_to('Approval'))
    assert_that(capture_response.transaction_result.type, equal_to('COMPLETION'))
    assert_that(capture_response.transaction_result.status, equal_to('READY'))


def test_tango_preauth_void():
    request = rest2_payment_moto(currency=Currency.CAD, cardtype='visa')
    request.auto_capture = False
    response = rest2.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.type, equal_to('PREAUTH'))
    assert_that(response.transaction_result.status, equal_to('PENDING'))

    reversal_response = rest2.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY, silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.transaction_result.status, equal_to('VOID'))
    assert_that(reversal_response.transaction_result.authorized_amount, equal_to(response.order.total_amount))
