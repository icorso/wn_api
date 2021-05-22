from faker import Factory
from hamcrest import assert_that, equal_to, instance_of

from data.rest_requests import rest_keyed_securecard
from model.rest import secureCardRegisterRestResponse
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22001'


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
    # TODO add fields
