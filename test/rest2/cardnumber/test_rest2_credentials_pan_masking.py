import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey
from data.rest2_credentials_requests import rest2_credentials_keyed, rest2_update_credentials
from model.rest2 import CustomField, Error
from model.rest2.secure_credentials import SecureCredentials
from utils import split_string
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '22001'
KEY = db.get_api_key(ApiKey.API_WN_FULL)
wn = WNClient().vagrant.wn.rest2(terminal_id=TERM_ID)


@pytest.mark.parametrize('divider', ['', '-', ' '])
def test_credentials_store_merchant_reference_pan_not_allowed(divider):
    request = rest2_credentials_keyed(cardtype='visa')
    request.merchant_reference = split_string(request.customer_account.card_details.card_number, divider)
    response = wn.credentials_store(request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('Inappropriate card number usage'))


@pytest.mark.parametrize('cardnumber', ['679999123456', '4012888818888', '38000000000006'])
def test_credentials_store_short_cardnumber_pan_not_allowed(cardnumber):
    request = rest2_credentials_keyed(cardtype='visa')
    request.customer_account.card_details.card_number = cardnumber
    request.merchant_reference = cardnumber
    response = wn.credentials_store(request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('Inappropriate card number usage'))


def test_credentials_store_cardholder_name_pan_not_allowed():
    request = rest2_credentials_keyed(cardtype='visa')
    request.customer_account.cardholder_name = request.customer_account.card_details.card_number
    response = wn.credentials_store(request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('Inappropriate card number usage'))


def test_credentials_store_cardholder_name_not_exact_pan_not_allowed():
    request = rest2_credentials_keyed(cardtype='visa')
    request.customer_account.cardholder_name = 'ab' + request.customer_account.card_details.card_number + ' xz'
    response = wn.credentials_store(request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('Inappropriate card number usage'))


@pytest.mark.parametrize('field', ['name', 'phone', 'email'])
def test_credentials_store_customer_pan_not_allowed(field):
    request = rest2_credentials_keyed(cardtype='visa')
    setattr(request.customer, field, request.customer_account.card_details.card_number)
    response = wn.credentials_store(request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('Inappropriate card number usage'))


@pytest.mark.parametrize('field', ['line1', 'line2', 'postal_code', 'city', 'state'])
def test_credentials_store_billing_address_pan_not_allowed(field):
    request = rest2_credentials_keyed(cardtype='visa')
    setattr(request.customer.billing_address, field, request.customer_account.card_details.card_number)
    response = wn.credentials_store(request=request, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('Inappropriate card number usage'))


def test_credentials_store_custom_field_pan_not_allowed():
    request = rest2_credentials_keyed(cardtype='visa')
    scf = CustomField(name='SecureCardField', value=str(request.customer_account.card_details.card_number))
    request.additional_data_fields = [scf]
    response = wn.credentials_store(request=request,
                                    api2_key=KEY, silence=False)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('Inappropriate card number usage'))


@pytest.mark.parametrize('field', ['name', 'phone', 'email'])
def test_credentials_update_customer_pan_not_allowed(field):
    request = rest2_credentials_keyed(cardtype='visa')
    response = wn.credentials_store(request=request, api2_key=KEY, silence=True)
    assert_that(response, instance_of(SecureCredentials))

    update_request = rest2_update_credentials(cardtype='visa', cvv='999')
    setattr(update_request.customer, field, update_request.customer_account.card_number)
    update_response = wn.credentials_update(request=update_request, merchant_reference=request.merchant_reference,
                                            api2_key=KEY, silence=False)

    assert_that(update_response, instance_of(Error))
    assert_that(update_response.details[0].error_message, equal_to('Inappropriate card number usage'))


def test_credentials_update_custom_field_and_cardnumber_pan_not_allowed():
    request = rest2_credentials_keyed(cardtype='visa')
    response = wn.credentials_store(request=request, api2_key=KEY, silence=True)
    assert_that(response, instance_of(SecureCredentials))

    update_request = rest2_update_credentials(cardtype='visa', cvv='999')
    scf = CustomField(name='SecureCardField', value=str(update_request.customer_account.card_number))
    update_request.additional_data_fields = [scf]
    update_response = wn.credentials_update(request=update_request, merchant_reference=request.merchant_reference,
                                            api2_key=KEY, silence=False)

    assert_that(update_response, instance_of(Error))
    assert_that(update_response.details[0].error_message, equal_to('Inappropriate card number usage'))


def test_credentials_update_custom_field_only_not_allowed():
    request = rest2_credentials_keyed(cardtype='visa')
    response = wn.credentials_store(request=request, api2_key=KEY, silence=True)
    assert_that(response, instance_of(SecureCredentials))

    update_request = rest2_update_credentials(cardtype='visa', cvv='999')
    scf = CustomField(name='SecureCardField', value=str(request.customer_account.card_details.card_number))
    update_request.additional_data_fields = [scf]
    update_request.customer_account = request.customer_account.card_details
    update_response = wn.credentials_update(request=update_request, merchant_reference=request.merchant_reference,
                                            api2_key=KEY, silence=False)

    assert_that(update_response, instance_of(Error))
    assert_that(update_response.details[0].error_message, equal_to('Inappropriate card number usage'))
