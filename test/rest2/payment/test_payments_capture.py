import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, contains_string

from constants import ApiKey
from data.rest2_payment_requests import rest2_payment_moto
from model.rest2 import Error
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '21001'
NMI_TERM_ID = '21002'
AIB_TERM_ID = '22001'
TANGO_TERM_ID = '21004'
TSYS_TERM_ID = '21003'
PAYU_TERM_ID = '21004'
SIERRA_TERM_ID = '21005'
GO_KEY = db.get_api_key(ApiKey.API_GO_FULL)
WN_KEY = db.get_api_key(ApiKey.API_WN_FULL)
go = WNClient().vagrant.go
wn = WNClient().vagrant.wn
go_boarding = WNClient().vagrant.go.boarding()
wn_boarding = WNClient().vagrant.wn.boarding()


def test_preauth_capture():
    term_id = TERM_ID
    go_boarding.update_terminal_integration(term_id, 'autoReady', True, silence=True)
    go_boarding.update_terminal_bank_settings(term_id, 'allowPreAuth', True, silence=True)

    request = rest2_payment_moto()
    request.auto_capture = False
    request.process_as_sale = False
    response = go.rest2(terminal_id=term_id).payment(request=request, api2_key=GO_KEY, silence=True)
    capture_response = go.rest2(term_id).payment_capture(uniqueref=response.unique_reference,
                                                         amount=response.order.total_amount,
                                                         api2_key=GO_KEY, silence=True)
    assert_that(capture_response, instance_of(Payment))
    assert_that(capture_response.transaction_result.result_message, equal_to('APPROVAL'))
    assert_that(capture_response.transaction_result.type, equal_to('COMPLETION'))
    assert_that(capture_response.transaction_result.status, equal_to('READY'))


def test_auth_capture():
    term_id = AIB_TERM_ID
    wn_boarding.update_terminal_integration(term_id, 'autoReady', False, silence=True)
    wn_boarding.update_terminal_bank_settings(term_id, 'allowPreAuth', False, silence=True)

    request = rest2_payment_moto(cardtype='VISA')
    request.auto_capture = False
    request.process_as_sale = False
    response = wn.rest2(terminal_id=term_id).payment(request=request, api2_key=WN_KEY)
    capture_response = wn.rest2(terminal_id=term_id).payment_capture(uniqueref=response.unique_reference,
                                                                     amount=response.order.total_amount,
                                                                     api2_key=WN_KEY)
    assert_that(capture_response, instance_of(Payment))
    assert_that(capture_response.transaction_result.result_message, contains_string('AUTH CODE'))
    assert_that(capture_response.transaction_result.type, equal_to('SALE'))
    assert_that(capture_response.transaction_result.status, equal_to('READY'))


def test_sale_capture_full_amount():
    term_id = PAYU_TERM_ID
    go_boarding.update_terminal_integration(term_id, 'autoReady', True, silence=True)
    go_boarding.update_terminal_bank_settings(term_id, 'allowPreAuth', False, silence=True)

    request = rest2_payment_moto(cardtype='visa')
    request.auto_capture = True
    request.process_as_sale = True
    request.customer_account.cardholder_name = fake.name()

    response = go.rest2(terminal_id=term_id).payment(request=request, api2_key=GO_KEY, silence=False)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.status, equal_to('COMPLETE'))

    capture_response = go.rest2(terminal_id=term_id).payment_capture(uniqueref=response.unique_reference,
                                                                     amount=response.order.total_amount,
                                                                     api2_key=GO_KEY)
    assert_that(capture_response, instance_of(Payment))
    assert_that(capture_response.transaction_result.status, equal_to('COMPLETE'))


@pytest.mark.parametrize('amount, error_message', [
    (0.01, 'Partial Reversal is not supported for PayULatam'),
    (1000, 'Top-up is not supported for PayULatam')
])
def test_sale_partial_capture_not_allowed(amount, error_message):
    term_id = PAYU_TERM_ID
    go_boarding.update_terminal_integration(term_id, 'autoReady', True, silence=True)
    go_boarding.update_terminal_bank_settings(term_id, 'allowPreAuth', False, silence=True)

    request = rest2_payment_moto(cardtype='visa')
    request.auto_capture = True
    request.process_as_sale = True
    request.customer_account.cardholder_name = fake.name()

    response = go.rest2(terminal_id=term_id).payment(request=request, api2_key=GO_KEY, silence=False)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.status, equal_to('COMPLETE'))

    error_response = go.rest2(terminal_id=term_id).payment_capture(uniqueref=response.unique_reference,
                                                                     amount=amount,
                                                                     api2_key=GO_KEY)
    assert_that(error_response, instance_of(Error))
    assert_that(error_response.details[0].error_message,
                equal_to(error_message))


@pytest.mark.parametrize('amount', [0.01, 1000])
def test_sale_partial_capture_allowed(amount):
    term_id = SIERRA_TERM_ID
    go_boarding.update_terminal_integration(term_id, 'autoReady', True, silence=True)
    go_boarding.update_terminal_bank_settings(term_id, 'allowPreAuth', False, silence=True)

    request = rest2_payment_moto(cardtype='visa')
    request.auto_capture = True
    request.customer_account.cardholder_name = fake.name()

    response = go.rest2(terminal_id=term_id).payment(request=request, api2_key=GO_KEY, silence=False)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.status, equal_to('READY'))

    capture_response = go.rest2(terminal_id=term_id).payment_capture(uniqueref=response.unique_reference,
                                                                     amount=amount,
                                                                     api2_key=GO_KEY)
    assert_that(capture_response, instance_of(Payment))
    assert_that(capture_response.order.total_amount, equal_to(amount))
