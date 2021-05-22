from faker import Factory
from hamcrest import assert_that, instance_of

from constants import ApiKey
from data.rest2_credentials_requests import rest2_credentials_keyed, rest2_update_credentials
from model.rest2.secure_credentials import SecureCredentials
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '22001'
KEY = db.get_api_key(ApiKey.API_WN_FULL)
wn = WNClient().vagrant.wn.rest2(terminal_id=TERM_ID)


def test_credentials_update_cardholder_name():
    request = rest2_credentials_keyed(cardtype='visa')
    response = wn.credentials_store(request=request, api2_key=KEY)
    assert_that(response, instance_of(SecureCredentials))

    update_request = rest2_update_credentials(cardtype='visa', cvv='999')
    update_response = wn.credentials_update(request=update_request, merchant_reference=request.merchant_reference,
                                            api2_key=KEY, silence=False)
    # TODO assertion
