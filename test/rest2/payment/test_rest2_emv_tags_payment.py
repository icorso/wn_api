import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey, EmvTlv, PosDevice, CardReadMethod
from data.rest2_payment_requests import rest2_payment_emv, rest2_payment_emv_tags
from model.rest2 import Error
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '21001'
db = WNClient().db(terminal_number=TERM_ID)
KEY = db.get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)
wn_boarding = WNClient().vagrant.go.boarding()


def test_payment_emv_tags_missing_mandatory():
    p = rest2_payment_emv_tags(device_type=PosDevice.WISEPAD, ksn='88888835400002200001')
    response = wn.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Error))
