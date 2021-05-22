from hamcrest import assert_that, instance_of

from data.xml_requests import securecard_registration
from model.gateway import SECURECARDREGISTRATIONRESPONSE
from wnclient import WNClient

wn = WNClient().vagrant.go
TERM_ID = '21004'


def test_securecard_registration_ok():
    sc = securecard_registration(cvv='999')
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


