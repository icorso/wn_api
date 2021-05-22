from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import preauth
from model.gateway import PREAUTHRESPONSE, PREAUTHCOMPLETIONRESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22001'


def test_elavon_preauth_ok():
    response = wn.xml(TERM_ID).preauth()
    assert_that(response, instance_of(PREAUTHRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_elavon_preauth_completion():
    preauth_request = preauth()
    preauth_response = wn.xml(TERM_ID).preauth(preauth_request)

    response = wn.xml(TERM_ID).preauthcompletion(amount=preauth_request.AMOUNT, uniquerf=preauth_response.UNIQUEREF)
    assert_that(response, instance_of(PREAUTHCOMPLETIONRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


