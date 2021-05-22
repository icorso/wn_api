from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey
from data.rest2_payment_requests import rest2_payment_offline
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '21001'
KEY = db.get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)
wn_boarding = WNClient().vagrant.go.boarding()


def test_payment_offline_valid():
    approval_code = fake.random_number(5)
    r = rest2_payment_offline(approval_code=approval_code)
    response = wn.payment(request=r, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.result_message, equal_to('OFFLINE AUTH'))
    assert_that(response.transaction_result.approval_code, equal_to(str(approval_code)))
