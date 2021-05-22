from copy import deepcopy

from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey, PosDevice, EmvTlv, MsrPayload
from data.rest2_payment_requests import rest2_payment_moto, rest2_payment_msr_encrypted, rest2_payment_emv
from model.rest2 import Error
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '22004'
KEY = WNClient().db().get_api_key(ApiKey.API_WN_FULL)
wn = WNClient().vagrant.wn.rest2(terminal_id=TERM_ID)


def test_elavon_pos_payment_reverse_no_customer_account():
    response = wn.payment(request=rest2_payment_moto(), api2_key=KEY)
    assert_that(response, instance_of(Payment))

    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY, silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.transaction_result.status, equal_to('VOID'))
    assert_that(reversal_response.transaction_result.authorized_amount, equal_to(response.order.total_amount))


def test_payment_reverse_mag_strip_payload():
    card = MsrPayload.VISA
    request = rest2_payment_msr_encrypted(card.encrypted, device_type=PosDevice.WISEPAD, ksn='88888835400002200001')
    response = wn.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))

    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY,
        customer_account=request.customer_account,
        silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.customer_account.masked_pan, equal_to(card.get_masked_pan()))


def test_payment_reverse_emv_payload_with_customer_account():
    request = rest2_payment_emv(tlv_string=EmvTlv.CONTACTLESS_ICC.value, device_type=PosDevice.WISEPAD, ksn='88888835400002200001')
    response = wn.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))
    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY,
        customer_account=request.customer_account,
        silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.customer_account.masked_pan, equal_to(MsrPayload.VISA.get_masked_pan()))


def test_elavon_pos_payment_reverse_emv_payload_without_customer_account():
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


def test_payment_reverse_changed_emv_data():
    # 9F10 tag original value = 0210a00003240000000000000000000000ff
    #           changed value = 0220ab0003250000000000000000000011ff
    # changed value should be send to Elavon POS in payment reverse auth message
    request = rest2_payment_emv(tlv_string=EmvTlv.CONTACTLESS_ICC.value, device_type=PosDevice.WISEPAD, ksn='88888835400002200001')
    reverse_request = rest2_payment_emv(tlv_string=EmvTlv.CONTACTLESS_ICC_9F10_CHANGED.value,
                                        device_type=PosDevice.WISEPAD, ksn='88888835400002200001')
    response = wn.payment(request=request, api2_key=KEY)
    assert_that(response, instance_of(Payment))
    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY,
        customer_account=reverse_request.customer_account,
        silence=False)
    assert_that(reversal_response, instance_of(Payment))
    assert_that(reversal_response.customer_account.masked_pan, equal_to(MsrPayload.VISA.get_masked_pan()))


def test_payment_reverse_invalid_emv_payload():
    request = rest2_payment_emv(tlv_string=EmvTlv.CONTACTLESS_ICC.value, device_type=PosDevice.WISEPAD, ksn='88888835400002200001')
    response = wn.payment(request=request, api2_key=KEY)
    wrong_tlv_string = deepcopy(request.customer_account)
    wrong_tlv_string.tlv = '877774'
    assert_that(response, instance_of(Payment))

    reversal_response = wn.payment_reverse(
        uniqueref=response.unique_reference,
        amount=response.order.total_amount,
        api2_key=KEY,
        customer_account=wrong_tlv_string,
        silence=False)
    assert_that(reversal_response, instance_of(Error))
    assert_that(reversal_response.details[0].error_message, equal_to('Mandatory EMV tags [C0, C2] are missing'))

