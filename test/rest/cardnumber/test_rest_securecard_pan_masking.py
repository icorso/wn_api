import pytest
from faker import Factory
from hamcrest import assert_that, equal_to, instance_of

from data.rest_requests import rest_keyed_securecard, rest_token_method_keyed_secure_card
from model.rest import secureCardRegisterRestResponse, serviceError, customField, customFieldsType
from utils import split_string
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22001'


def test_rest_keyed_securecard_registration_merchant_reference_pan_not_allowed():
    r = rest_keyed_securecard()
    r.merchantReference = r.tokenMethod.keyedSecureCard.cardNumber
    securecard_response = wn.rest(TERM_ID).create_securecard(r)
    assert_that(securecard_response, instance_of(serviceError))
    assert_that(securecard_response.message, equal_to('Inappropriate card number usage'))


@pytest.mark.parametrize('divider', ['', ' ', '-'])
def test_rest_keyed_securecard_registration_cardholder_pan_not_allowed(divider):
    r = rest_keyed_securecard()
    r.tokenMethod.keyedSecureCard.cardHolderName = split_string(r.tokenMethod.keyedSecureCard.cardNumber, divider)
    securecard_response = wn.rest(TERM_ID).create_securecard(r)
    assert_that(securecard_response, instance_of(serviceError))
    assert_that(securecard_response.message, equal_to('Inappropriate card number usage'))


@pytest.mark.parametrize('field', ['city', 'mobileNumber', 'ipAddress', 'region'])
def test_rest_keyed_securecard_registration_customer_fields_pan_not_allowed(field):
    r = rest_keyed_securecard()
    setattr(r.customer, field, r.tokenMethod.keyedSecureCard.cardNumber)
    securecard_response = wn.rest(TERM_ID).create_securecard(r)
    assert_that(securecard_response, instance_of(serviceError))
    assert_that(securecard_response.message, equal_to('Inappropriate card number usage'))


def test_rest_keyed_securecard_registration_email_pan_not_allowed():
    r = rest_keyed_securecard()
    r.customer.eMail = r.tokenMethod.keyedSecureCard.cardNumber + '@local.host'
    securecard_response = wn.rest(TERM_ID).create_securecard(r)
    assert_that(securecard_response, instance_of(serviceError))
    assert_that(securecard_response.message, equal_to('Inappropriate card number usage'))


def test_rest_keyed_securecard_registration_custom_field_pan_not_allowed():
    r = rest_keyed_securecard()
    r.customFields = customFieldsType([customField(name='SecureCardField', value=r.tokenMethod.keyedSecureCard.cardNumber)])
    securecard_response = wn.rest(TERM_ID).create_securecard(r)
    assert_that(securecard_response, instance_of(serviceError))
    assert_that(securecard_response.message, equal_to('Inappropriate card number usage'))


def test_rest_securecard_update_custom_field_and_card_number_not_allowed():
    r = rest_keyed_securecard()
    securecard_response = wn.rest(TERM_ID).create_securecard(r)
    assert_that(securecard_response, instance_of(secureCardRegisterRestResponse))

    u = rest_keyed_securecard()
    u.cardReference = r.cardReference
    u.merchantReference = r.merchantReference
    u.customFields = customFieldsType([customField(name='SecureCardField', value=u.tokenMethod.keyedSecureCard.cardNumber)])

    securecard_update_response = wn.rest(TERM_ID).update_securecard(u)
    assert_that(securecard_update_response, instance_of(serviceError))
    assert_that(securecard_update_response.message, equal_to('Inappropriate card number usage'))


def test_rest_securecard_update_custom_field_only_not_allowed():
    r = rest_keyed_securecard()
    securecard_response = wn.rest(TERM_ID).create_securecard(r)
    assert_that(securecard_response, instance_of(secureCardRegisterRestResponse))

    u = r
    u.cardReference = r.cardReference
    u.merchantReference = r.merchantReference
    u.customFields = customFieldsType([customField(name='SecureCardField', value=u.tokenMethod.keyedSecureCard.cardNumber)])

    securecard_update_response = wn.rest(TERM_ID).update_securecard(u)
    assert_that(securecard_update_response, instance_of(serviceError))
    assert_that(securecard_update_response.message, equal_to('Inappropriate card number usage'))
