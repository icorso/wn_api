from faker import Factory
from hamcrest import assert_that, instance_of

from model.gateway import ACHSECUREREGISTRATIONRESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21001'


def test_ach_secure_card_registration():
    achjh_secure_response = wn.xml(TERM_ID).ach_secure_registration()
    assert_that(achjh_secure_response, instance_of(ACHSECUREREGISTRATIONRESPONSE))
