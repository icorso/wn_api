from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, contains_string

from constants import ApiKey, PaynomixCard
from data.rest2_payment_requests import rest2_payment_moto
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '22015'
KEY = WNClient().db().get_api_key(ApiKey.API_WN_FULL)
wn = WNClient().vagrant.wn.rest2(terminal_id=TERM_ID)


def test_paynomix_preauth_success():
    r = rest2_payment_moto()
    r.auto_capture = 'false'
    r.customer_account.card_details.card_number = PaynomixCard.rand().cardnumber
    response = wn.payment(request=r, api2_key=KEY)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.status, equal_to('PENDING'))


def test_paynomix_preauth_complete():
    r = rest2_payment_moto()
    r.auto_capture = 'false'
    r.customer_account.card_details.card_number = PaynomixCard.rand().cardnumber
    response = wn.payment(request=r, api2_key=KEY)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.status, equal_to('PENDING'))

    capture_response = wn.payment_capture(uniqueref=response.unique_reference, amount=response.order.total_amount,
                                          api2_key=KEY)
    assert_that(capture_response, instance_of(Payment))
    assert_that(capture_response.transaction_result.result_message, contains_string('Approved'))
    assert_that(capture_response.transaction_result.type, equal_to('COMPLETION'))
    assert_that(capture_response.transaction_result.status, equal_to('READY'))


def test_paynomix_preauth_reverse():
    r = rest2_payment_moto()
    r.auto_capture = 'false'
    r.customer_account.card_details.card_number = PaynomixCard.rand().cardnumber
    response = wn.payment(request=r, api2_key=KEY)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.status, equal_to('PENDING'))

    reverse_response = wn.payment_reverse(uniqueref=response.unique_reference, amount=response.order.total_amount,
                                          api2_key=KEY)
    assert_that(reverse_response, instance_of(Payment))
    assert_that(reverse_response.transaction_result.result_message, contains_string('Approved'))
    assert_that(reverse_response.transaction_result.type, equal_to('PREAUTH'))
    assert_that(reverse_response.transaction_result.status, equal_to('VOID'))
