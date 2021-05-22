from faker import Factory
from hamcrest import assert_that, equal_to, instance_of, has_length

from constants import SecureCard
from data.rest_requests import rest_keyed_securecard
from model.rest import secureCardRegisterRestResponse, secureCardRestResponse
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21001'


def test_rest_get_securecard_success():
    securecard_response = wn.rest(TERM_ID).get_securecard(SecureCard.MASTERCARD.merchant_ref)
    assert_that(securecard_response, instance_of(secureCardRestResponse))
    assert_that(securecard_response.secureCard.merchantReference, equal_to(SecureCard.MASTERCARD.merchant_ref))


def test_rest_securecard_registration_success():
    r = rest_keyed_securecard()
    securecard_response = wn.rest(TERM_ID).create_securecard(r)
    assert_that(securecard_response, instance_of(secureCardRegisterRestResponse))
    assert_that(securecard_response.description, equal_to('Successful result'))
    assert_that(securecard_response.merchantRef, equal_to(r.merchantReference))
    assert_that(securecard_response.cardReference, has_length(16))

    securecard_get_response = wn.rest(TERM_ID).get_securecard(r.merchantReference)
    assert_that(securecard_get_response, instance_of(secureCardRestResponse))
    assert_that(securecard_get_response.description, equal_to('Secure Card was found'))
    assert_that(securecard_get_response.secureCard.merchantReference, equal_to(r.merchantReference))
    assert_that(securecard_get_response.secureCard.tokenMethod.keyedSecureCard.cardHolderName,
                equal_to(r.tokenMethod.keyedSecureCard.cardHolderName))


def test_rest_securecard_update_success():
    r = rest_keyed_securecard()
    securecard_response = wn.rest(TERM_ID).create_securecard(r)
    assert_that(securecard_response, instance_of(secureCardRegisterRestResponse))

    u = rest_keyed_securecard()
    u.cardReference = r.cardReference
    u.merchantReference = r.merchantReference
    securecard_update_response = wn.rest(TERM_ID).update_securecard(u)
    assert_that(securecard_update_response, instance_of(secureCardRegisterRestResponse))
    assert_that(securecard_update_response.description, equal_to('Successful result'))
