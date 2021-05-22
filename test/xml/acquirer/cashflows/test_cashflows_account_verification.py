import pytest
from faker import Factory
from hamcrest import assert_that, equal_to, instance_of, is_not

from constants import StoredCredentialTxType
from data.xml_requests import account_verification_request
from model.gateway import ACCOUNT_VERIFICATION_RESPONSE, CREDENTIALONFILE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22004'
COF = CREDENTIALONFILE(
        BRANDTXIDENTIFIER=None,
        ORIGINALBRANDTXIDENTIFIER=None,
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.FIRST_TXN.name,
        STOREDCREDENTIALUSE=None
    )


@pytest.mark.parametrize('cardnumber', ['5555555555554444', '4000000000000002'])
def test_account_verification_cashflows_cof_validated(cardnumber):
    r = account_verification_request(cardnumber=cardnumber, cvv='123')
    r.CREDENTIALONFILE = COF

    response = wn.xml(TERM_ID).account_verification(r)
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('VERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to(None))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


@pytest.mark.parametrize('cardnumber', ['5555555555554444', '4000000000000002'])
def test_account_verification_cashflows_no_cof_validated(cardnumber):
    response = wn.xml(TERM_ID).account_verification(account_verification_request(cardnumber=cardnumber, cvv='123'))
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('VERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to(None))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


def test_account_verification_visa_cashflows_invalid_card_number():
    response = wn.xml(TERM_ID).account_verification(account_verification_request(cardnumber='4180783703403720'))
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('UNVERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to('Invalid Request'))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


def test_account_verification_visa_cashflows_invalid_expiry_date():
    r = account_verification_request(cardnumber='4000000000000002')
    r.CARDEXPIRY = '0133'
    response = wn.xml(TERM_ID).account_verification(r)
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('UNVERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to('Invalid Request'))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


def test_account_verification_visa_cashflows_invalid_cvv():
    response = wn.xml(TERM_ID).account_verification(account_verification_request(cardnumber='4000000000000002'))
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('UNVERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to('CVV validation failed'))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


def test_account_verification_mc_cashflows_invalid_expiry_date():
    r = account_verification_request(cardtype='Mastercard', cardnumber='5555555555554444')
    r.CARDEXPIRY = '0133'
    response = wn.xml(TERM_ID).account_verification(r)
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('VERIFIED'))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


def test_account_verification_mc_cashflows_cvv_validation_failed():
    r = account_verification_request(cardnumber='5555555555554444')
    response = wn.xml(TERM_ID).account_verification(r)
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('UNVERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to('CVV validation failed'))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


def test_account_verification_mc_cashflows_invalid_card_number():
    response = wn.xml(TERM_ID).account_verification(
        account_verification_request(cardnumber='5482931994045914', cvv='321', cardtype='Mastercard'))
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('VERIFIED'))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")
