from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, contains_string

from constants import ApiKey, PosDevice, EmvTlv, Currency
from data.rest2_payment_requests import rest2_payment_moto, rest2_payment_msr_encrypted, rest2_payment_emv
from model.rest2 import Error
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '21001'
TSYS_TERM_ID = '21005'
MC_TERM_ID = '21002'
KEY = WNClient().db().get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)
wn_boarding = WNClient().vagrant.go.boarding()


def test_refund_reverse_valid():
    response = wn.payment(request=rest2_payment_moto(), api2_key=KEY)
    assert_that(response, instance_of(Payment))

    refund_amount = round(response.order.total_amount / 2)
    refund_response = wn.payment_refund(response.unique_reference, refund_amount, api2_key=KEY)
    assert_that(refund_response, instance_of(Payment))

    reversal_response = wn.refund_reverse(
        uniqueref=refund_response.unique_reference,
        api2_key=KEY, silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.transaction_result.status, equal_to('VOID'))
    assert_that(reversal_response.transaction_result.type, equal_to('REFUND'))


def test_reverse_already_refunded_txn():
    response = wn.payment(request=rest2_payment_moto(), api2_key=KEY)
    assert_that(response, instance_of(Payment))

    refund_amount = round(response.order.total_amount / 2)
    refund_response = wn.payment_refund(response.unique_reference, refund_amount, api2_key=KEY)
    assert_that(refund_response, instance_of(Payment))

    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY, silence=False)
    assert_that(reversal_response, instance_of(Error))
    assert_that(reversal_response.details[0].error_message, contains_string('Transaction is already refunded'))


def test_payment_full_reverse_multicurrency_terminal():
    p = rest2_payment_moto(currency=Currency.GBP)
    p.customer_account.card_details.card_number = '5166749338101778'  # 4569883295200822
    response = wn.with_terminal(MC_TERM_ID).payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))

    reversal_response = wn.with_terminal(MC_TERM_ID).payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY, silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.transaction_result.status, equal_to('VOID'))
    assert_that(reversal_response.transaction_result.authorized_amount, equal_to(response.order.total_amount))


def test_payment_partial_reverse_not_supported():
    response = wn.payment(request=rest2_payment_moto(), api2_key=KEY)
    assert_that(response, instance_of(Payment))

    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=round(response.order.total_amount/2),
        api2_key=KEY, silence=False)
    assert_that(reversal_response, instance_of(Error))
    assert_that(reversal_response.details[0].error_message, contains_string('Partial Reversal is not supported for'))


def test_payment_partial_reverse_valid():
    response = wn.with_terminal(TSYS_TERM_ID).payment(request=rest2_payment_moto(), api2_key=KEY)
    assert_that(response, instance_of(Payment))

    reversal_amount = round(response.order.total_amount/3)
    reversal_response = wn.with_terminal(TSYS_TERM_ID).payment_reverse(
        uniqueref=response.unique_reference,
        amount=reversal_amount,
        api2_key=KEY, silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.order.total_amount, equal_to(response.order.total_amount - reversal_amount))


def test_payment_partial_reverse_payload_type_not_supported():
    request = rest2_payment_moto()
    response = wn.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))

    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY,
        customer_account=request.customer_account,
        silence=False)
    assert_that(reversal_response, instance_of(Error))
    assert_that(reversal_response.details[0].error_message, equal_to('Unable to resolve type identifier'))
    assert_that(reversal_response.details[0].source.expected, equal_to('Known types: [MAG_STRIPE, EMV]'))


def test_payment_partial_reverse_mag_strip_payload():
    request = rest2_payment_msr_encrypted('C3436C5CC89E6FD358AA8EBDEE8B0D9ADA83667F068A0D44',
                                          device_type=PosDevice.WISEPAD,
                                          ksn='88888835400002200001')
    response = wn.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))

    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY,
        customer_account=request.customer_account,
        silence=False)
    assert_that(reversal_response, instance_of(Error))
    assert_that(reversal_response.details[0].error_message, equal_to('Unable to resolve type identifier'))
    assert_that(reversal_response.details[0].source.expected, equal_to('Known types: [MAG_STRIPE, EMV]'))


def test_payment_partial_reverse_emv_payload():
    request = rest2_payment_emv(tlv_string=EmvTlv.CONTACTLESS_ICC.value,
                                device_type=PosDevice.WISEPAD,
                                ksn='88888835400002200001')
    response = wn.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))
    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY,
        customer_account=request.customer_account,
        silence=False)
    assert_that(reversal_response, instance_of(Error))
    assert_that(reversal_response.details[0].error_message, equal_to('Unable to resolve type identifier'))
    assert_that(reversal_response.details[0].source.expected, equal_to('Known types: [MAG_STRIPE, EMV]'))
