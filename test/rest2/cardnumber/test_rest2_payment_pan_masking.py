import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey, MsrPayload, PosDevice
from data.rest2_credentials_requests import rest2_credentials_keyed
from data.rest2_payment_requests import rest2_credentials_payment, rest2_payment_moto, rest2_payment_offline, \
    rest2_unreferenced_refund_keyed, rest2_payment_update, rest2_payment_msr_encrypted
from model.rest2 import Payment, CustomField, Error, Address, Device, OfflineProcessing, IpAddress, Refund
from model.rest2.secure_credentials import SecureCredentials
from utils import masked_pan, split_string
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '21001'
KEY = db.get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)


@pytest.mark.parametrize('divider', ['', '-', ' '])
def test_payment_order_id_pan_not_allow(divider):
    request = rest2_payment_moto()
    pan = split_string(request.customer_account.card_details.card_number, divider)
    request.order.order_id = pan
    response = wn.payment(request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('invalid or unknown'))
    assert_that(response.details[0].source._property, equal_to('orderId'))


@pytest.mark.parametrize('divider', ['', '-', ' '])
def test_payment_string_fields_pan_masking(divider):
    request = rest2_payment_moto()
    pan = split_string(request.customer_account.card_details.card_number, divider)
    request.operator = pan
    request.order.description = pan

    request.customer.name = pan
    request.customer.email = f'{pan}@local.host'

    request.customer.billing_address = Address(
        line1=pan,
        line2=pan,
        postal_code=pan,
        city=pan,
        state=pan,
    )
    request.customer.shipping_address = Address(
        line1=pan,
        line2=pan,
        postal_code=pan,
        city=pan,
        state=pan,
    )

    request.customer_account.cardholder_name = pan
    # request.customer_account.card_details.device = Device(
    #     type='WISEPAD',
    #     category='UNATTENDED'
    # )

    response = wn.payment(request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))


@pytest.mark.parametrize('divider', ['', '-', ' '])
def test_offline_payment_pan_masking(divider):
    request = rest2_payment_offline()
    pan = split_string(request.customer_account.card_details.card_number, divider)
    request.offline_processing.approval_code = pan

    response = wn.payment(request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))


def test_payment_phone_field_pan_invalid():
    request = rest2_payment_moto()
    pan = request.customer_account.card_details.card_number
    request.customer.phone = pan
    response = wn.payment(request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('invalid format'))
    assert_that(response.details[0].source._property, equal_to('phone'))


@pytest.mark.parametrize('divider', ['', '-', ' '])
def test_payment_custom_field_pan_masking_valid(divider):
    request = rest2_payment_moto()
    split_pan = split_string(request.customer_account.card_details.card_number, divider)
    pan = request.customer_account.card_details.card_number
    request.additional_data_fields = [
        CustomField(name='uid', value=split_pan)
    ]
    response = wn.payment(request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
    assert_that(response.additional_data_fields[0].value, equal_to(masked_pan(pan)))


@pytest.mark.parametrize('divider', ['', '-', ' '])
def test_credentials_payment_pan_masking_valid(divider):
    sc = rest2_credentials_keyed()
    response = wn.credentials_store(request=sc, api2_key=KEY, silence=False)
    assert_that(response, instance_of(SecureCredentials))
    pan = split_string(sc.customer_account.card_details.card_number, divider)

    cp = rest2_credentials_payment(response.credentials_number)
    cp.additional_data_fields = [
        CustomField(name='uid', value=pan)
    ]
    cp.order.description = pan
    payment_response = wn.payment(request=cp, api2_key=KEY)
    assert_that(payment_response, instance_of(Payment))
    # manually check [M-API] Request payload unmarshalled successfully log entry for masking


def test_unreferenced_refund_pan_masking_valid():
    request = rest2_unreferenced_refund_keyed()
    pan = request.customer_account.card_details.card_number

    request.operator = pan
    request.refund_reason = pan

    request.customer.name = pan
    request.customer.email = f'{pan}@local.host'

    request.customer.billing_address = Address(
        line1=pan,
        line2=pan,
        postal_code=pan,
        city=pan,
        state=pan,
    )
    request.customer.shipping_address = Address(
        line1=pan,
        line2=pan,
        postal_code=pan,
        city=pan,
        state=pan,
    )

    request.customer_account.cardholder_name = pan

    refund_response = wn.unreferenced_refund(request, api2_key=KEY, silence=False)
    assert_that(refund_response, instance_of(Refund))
    assert_that(refund_response.operator, equal_to(masked_pan(pan)))
    assert_that(refund_response.refund_reason, equal_to(masked_pan(pan)))
    assert_that(refund_response.customer_account.cardholder_name, equal_to(masked_pan(pan)))
    assert_that(refund_response.customer_account.masked_pan, equal_to(masked_pan(pan)))


def test_payment_update_pan_masking_valid():
    # should not be masked
    request = rest2_payment_moto()
    pan = request.customer_account.card_details.card_number
    payment_response = wn.payment(request=request, api2_key=KEY, silence=False)
    assert_that(payment_response, instance_of(Payment))

    request = rest2_payment_update()
    request.operator = pan
    request.total_amount = None
    request.customer.phone = pan
    request.customer.notification_email = f'{pan}@local.host'

    response = wn.payment_update(uniqueref=payment_response.unique_reference, request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))


def test_payment_msr_not_masked():
    p = rest2_payment_msr_encrypted(encrypted_data=MsrPayload.VISA.encrypted,
                                    ksn='88888835400002200001',
                                    device_type=PosDevice.WISEPAD,
                                    additional_tlv_data='9F390191')
    p.operator = MsrPayload.VISA.cardnumber
    response = wn.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
