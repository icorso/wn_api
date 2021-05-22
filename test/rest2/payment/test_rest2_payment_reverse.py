from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, contains_string

from constants import ApiKey, PosDevice, EmvTlv, Currency, MsrPayload
from data.rest2_payment_requests import rest2_payment_moto, rest2_payment_msr_encrypted, rest2_payment_emv
from model.rest2 import Error
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '22004'
MC_TERM_ID = '21002'
KEY = WNClient().db().get_api_key(ApiKey.API_WN_FULL)
wn = WNClient().vagrant.wn.rest2(terminal_id=TERM_ID)
wn_mc = WNClient().vagrant.go.rest2(terminal_id=MC_TERM_ID)
wn_boarding = WNClient().vagrant.go.boarding()


def test_payment_full_reverse_valid():
    response = wn.payment(request=rest2_payment_moto(), api2_key=KEY)
    assert_that(response, instance_of(Payment))

    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY, silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.transaction_result.status, equal_to('VOID'))
    assert_that(reversal_response.transaction_result.authorized_amount, equal_to(response.order.total_amount))


def test_payment_reverse_settled_transaction():
    # enter manually
    amount = 4.92
    uniqueref = 'GRQYEYUR81'
    reversal_response = wn.payment_reverse(
        uniqueref=uniqueref,
        amount=amount,
        api2_key=KEY, silence=False)
    assert_that(reversal_response, instance_of(Error))
    assert_that(reversal_response.details[0].error_message, contains_string('Transaction not found'))


def test_payment_full_reverse_multicurrency_terminal():
    p = rest2_payment_moto(currency=Currency.USD)
    # p.customer_account.card_details.card_number = '5166749338101778' # 4569883295200822
    response = wn_mc.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))

    reversal_response = wn_mc.payment_reverse(
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


def test_msr_payment_reverse_emv_payload():
    card = MsrPayload.VISA
    request = rest2_payment_msr_encrypted(card.encrypted, device_type=PosDevice.WISEPAD, ksn='88888835400002200001')
    response = wn.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))

    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY,
        customer_account=rest2_payment_emv(tlv_string=EmvTlv.CONTACTLESS_ICC.value, device_type=PosDevice.WISEPAD, ksn='88888835400002200001').customer_account,
        silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.customer_account.masked_pan, equal_to(card.get_masked_pan()))


def test_payment_reverse_emv_payload_without_customer_account():
    request = rest2_payment_emv(tlv_string=EmvTlv.CONTACTLESS_ICC.value, device_type=PosDevice.WISEPAD, ksn='88888835400002200001')
    response = wn.payment(request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY,
        silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.customer_account.masked_pan, equal_to(MsrPayload.VISA.get_masked_pan()))


def test_msr_payment_reverse_another_msr_payload():
    card = MsrPayload.VISA
    reverse_card = MsrPayload.MASTERCARD
    request = rest2_payment_msr_encrypted(card.encrypted, device_type=PosDevice.WISEPAD, ksn='88888835400002200001')
    response = wn.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))

    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY,
        customer_account=rest2_payment_msr_encrypted(reverse_card.encrypted, device_type=PosDevice.WISEPAD, ksn='88888835400002200001').customer_account,
        silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.customer_account.masked_pan, equal_to(reverse_card.get_masked_pan()))
