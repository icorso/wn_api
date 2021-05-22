from faker import Factory
from hamcrest import assert_that, equal_to, instance_of

from data.xml_requests import account_verification_request
from model.gateway import ACCOUNT_VERIFICATION_RESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22005'


def test_account_verification_fdrc_no_cof_validated():
    response = wn.xml(TERM_ID).account_verification(account_verification_request())
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('VERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to(None))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")
