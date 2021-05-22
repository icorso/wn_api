import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey
from data.rest2_payment_requests import rest2_payment_moto, rest2_payment_offline
from model.rest2 import Error
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '22001'
GO_TERM_ID = '21001'
KEY = db.get_api_key(ApiKey.API_WN_FULL)
GO_KEY = db.get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.wn.rest2(terminal_id=TERM_ID)
go = WNClient().vagrant.go.rest2(terminal_id=GO_TERM_ID)
wn_boarding = WNClient().vagrant.wn.boarding()
go_boarding = WNClient().vagrant.go.boarding()
"""
Testing of openapi improvements payments/pre-auth/refunds, see issue #27488
"""


@pytest.mark.parametrize('auto_capture, status', [(True, 'READY'), (False, 'PENDING')])
def test_payment_auto_capture_preauth_not_allowed(auto_capture, status):
    wn_boarding.update_terminal_integration(TERM_ID, 'autoReady', True, silence=True)
    wn_boarding.update_terminal_bank_settings(TERM_ID, 'allowPreAuth', False, silence=True)
    request = rest2_payment_moto()
    request.auto_capture = auto_capture
    response = wn.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.type, equal_to('SALE'))
    assert_that(response.transaction_result.status, equal_to(status))


@pytest.mark.parametrize('auto_capture, status, transaction_type', [
    (True, 'READY', 'SALE'),
    (False, 'PENDING', 'PREAUTH')
])
def test_payment_auto_capture_preauth_allowed(auto_capture, status, transaction_type):
    wn_boarding.update_terminal_integration(TERM_ID, 'autoReady', True, silence=True)
    wn_boarding.update_terminal_bank_settings(TERM_ID, 'allowPreAuth', True, silence=True)
    request = rest2_payment_moto()
    request.auto_capture = auto_capture
    response = wn.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.type, equal_to(transaction_type))
    assert_that(response.transaction_result.status, equal_to(status))


def test_payment_process_as_sale_auto_capture_off():
    wn_boarding.update_terminal_integration(TERM_ID, 'autoReady', True, silence=True)
    wn_boarding.update_terminal_bank_settings(TERM_ID, 'allowPreAuth', True, silence=True)
    request = rest2_payment_moto()
    request.auto_capture = False
    request.process_as_sale = True
    response = wn.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message,
                equal_to('The auto capture indicator must be set to TRUE to process a Sale'))


def test_payment_process_as_sale_not_supported():
    wn_boarding.update_terminal_integration(TERM_ID, 'autoReady', False, silence=True)
    wn_boarding.update_terminal_bank_settings(TERM_ID, 'allowPreAuth', True, silence=True)
    request = rest2_payment_moto()
    request.auto_capture = True
    request.process_as_sale = True
    response = wn.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message,
                equal_to('Terminal does not support Sale transactions'))


@pytest.mark.parametrize('auto_capture, status', [
    (True, 'READY'),
    (False, 'PENDING')
])
def test_payment_offline_auto_capture(auto_capture, status):
    request = rest2_payment_offline()
    request.auto_capture = auto_capture
    response = go.payment(request=request, api2_key=GO_KEY)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.result_message, equal_to('OFFLINE AUTH'))
    assert_that(response.transaction_result.type, equal_to('SALE'))
    assert_that(response.transaction_result.status, equal_to(status))


def test_referenced_refund_auto_capture_off():
    go_boarding.update_terminal_integration(GO_TERM_ID, 'autoReady', False, silence=True)
    go_boarding.update_terminal_bank_settings(GO_TERM_ID, 'allowPreAuth', False, silence=True)
    request = rest2_payment_moto()
    request.auto_capture = False
    response = go.payment(request=request, api2_key=GO_KEY)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.type, equal_to('SALE'))
    assert_that(response.transaction_result.status, equal_to('PENDING'))

    refund_response = go.payment_refund(response.unique_reference, round(response.order.total_amount/2, 2), api2_key=GO_KEY)
    assert_that(refund_response, instance_of(Payment))
    assert_that(refund_response.transaction_result.status, equal_to('READY'))
