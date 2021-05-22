from faker import Factory
from hamcrest import assert_that, instance_of

from constants import LocalMerchant, ApiKey
from model.boarding2 import User
from wnclient import WNClient

wn = WNClient().vagrant.go.boarding2()
db = WNClient().db()
GO_KEY = ApiKey.BOARDING_GO_FULL
fake = Factory().create()
TERM_ID = '21001'


def test_tsys_saratoga_get_terminal_valid():
    key = db.get_api_key(GO_KEY)
    response = wn.get_user(LocalMerchant.GO.itemid, 'K0MS0BVW2I', User, key, silence=False)
    assert_that(response, instance_of(User))
