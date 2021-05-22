from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey
from data.rest2_payment_requests import rest2_payment_moto, rest2_unreferenced_refund_keyed
from model.rest2 import Refund
from model.rest2.payment import Payment
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '21001'
KEY = WNClient().db().get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)
wn_boarding = WNClient().vagrant.go.boarding()


def test_unreferenced_keyed_refund_ok():
    refund_request = rest2_unreferenced_refund_keyed()
    refund_response = wn.unreferenced_refund(refund_request, api2_key=KEY, silence=False)
    assert_that(refund_response, instance_of(Refund))
    assert_that(refund_response.transaction_result.status, equal_to('READY'))
    assert_that(refund_response.transaction_result.authorized_amount, equal_to(refund_request.refund_amount * -1))
