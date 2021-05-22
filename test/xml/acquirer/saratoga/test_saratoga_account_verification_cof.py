import random

from faker import Factory
from hamcrest import assert_that, equal_to, instance_of

from data.xml_requests import account_verification_request
from model.gateway import ACCOUNT_VERIFICATION_RESPONSE
from wnclient import WNClient

wn = WNClient().vagrant.go

fake = Factory.create()

TERM_ID = '21001'
VISA_DECLINED = ['4716564020255842', '4716565746302560', '4716561433580311', '4716562511346815', '4716566251064728']


def test_account_verification_saratoga_no_cof_validated():
    response = wn.xml(TERM_ID).account_verification(account_verification_request())
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('VERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to(None))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


def test_account_verification_saratoga_cvv_failed():
    response = wn.xml(TERM_ID).account_verification(account_verification_request(cardnumber=random.choice(VISA_DECLINED)))
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('UNVERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to('Incorrect CVV'))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")
