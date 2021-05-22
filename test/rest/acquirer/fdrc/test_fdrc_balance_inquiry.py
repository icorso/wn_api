from hamcrest import assert_that, equal_to, instance_of

from data.rest_requests import rest_balance_inquiry
from model.rest import serviceError
from wnclient import WNClient

wn = WNClient().local.goepay
TERM_ID = '22004'


def test_balance_inquiry_keyedcard():
    response = wn.rest(TERM_ID).balance_inquiry(rest_balance_inquiry())
    assert_that(response, instance_of(serviceError))
    assert_that(response.message, equal_to('Balance Inquiry request is allowed for CBIC cards only '))