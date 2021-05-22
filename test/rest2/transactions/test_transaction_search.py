from faker import Factory
from faker import Factory
from hamcrest import assert_that, has_length, greater_than

from constants import ApiKey
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '21001'
KEY = db.get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)
wn_boarding = WNClient().vagrant.go.boarding()


def test_transactions_search_valid():
    response = wn.search(api2_key=KEY, silence=False, terminal=TERM_ID,
                         afterDate='2020-01-01T20:26:56+00:00',
                         beforeDate='2020-12-31T00:00:00+00:00')
    assert_that(response.data, has_length(greater_than(0)))
