import pytest
from faker import Factory
from hamcrest import assert_that, equal_to, instance_of, is_not

from constants import StoredCredentialTxType
from data.xml_requests import account_verification_request
from model.gateway import ACCOUNT_VERIFICATION_RESPONSE, CREDENTIALONFILE
from wnclient import WNClient

wn = WNClient().local.wn

fake = Factory.create()

TERM_ID = '20001'


@pytest.mark.parametrize('cardnumber', ['5555555555554444', '4000000000000002'])
def test_account_verification_elavon_cof_validated(cardnumber):
    r = account_verification_request(cardnumber=cardnumber, cvv='123')
    r.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.FIRST_TXN.name,
    )

    response = wn.xml(TERM_ID).account_verification(r)
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('VERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to(None))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


@pytest.mark.parametrize('cardnumber', ['5555555555554444', '4000000000000002'])
def test_account_verification_elavon_no_cof_validated(cardnumber):
    response = wn.xml(TERM_ID).account_verification(account_verification_request(cardnumber=cardnumber, cvv='123'))
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('VERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to(None))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


def test_account_verification_visa_elavon_invalid_card_number():
    response = wn.xml(TERM_ID).account_verification(account_verification_request(cardnumber='4180783703403720'))
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('UNVERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to('DECLINED'))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")
