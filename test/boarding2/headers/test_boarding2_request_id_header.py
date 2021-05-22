from faker import Factory
from hamcrest import assert_that, instance_of

from constants import ApiKey
from model.boarding2 import AccessToken
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.wn
db = WNClient().db()
WN_KEY = ApiKey.BOARDING_WN_FULL


def test_authorization_key_valid():
    key = db.get_api_key(WN_KEY)
    # headers = {'X-Cloud-Trace-Context': "%s/%s" % (str(fake.random_number(32)), 'REST' + str(fake.random_number(16)))}
    headers = {'X-Cloud-Trace-Context': "%s/%s" % ('REST', 123)}

    response = wn.with_headers(headers).boarding2().authenticate(key, silence=False)
    assert_that(response, instance_of(AccessToken))
