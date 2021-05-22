from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey
from model.boarding2 import AccessToken
from model.boarding2 import Error
from wnclient import WNClient

wn = WNClient().vagrant.wn.boarding2()
db = WNClient().db()
WN_KEY = ApiKey.BOARDING_WN_FULL


def test_authorization_key_invalid():
    response = wn.authenticate('wrong_key')
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('The API Key is invalid'))


def test_authorization_host_invalid():
    key = db.get_api_key(WN_KEY)
    response = WNClient().local.go.boarding2().authenticate(key)
    assert_that(response, instance_of(Error))
    assert_that(response.details[0].error_message, equal_to('Invalid host'))


def test_authorization_key_valid():
    key = db.get_api_key(WN_KEY)
    response = wn.authenticate(key, silence=False)
    assert_that(response, instance_of(AccessToken))
