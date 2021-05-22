from faker import Factory
from hamcrest import assert_that, instance_of

from model.gateway import PREAUTHRESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21001'


def test_saratoga_preauth_ok():
    response = wn.xml(TERM_ID).preauth()
    assert_that(response, instance_of(PREAUTHRESPONSE))


