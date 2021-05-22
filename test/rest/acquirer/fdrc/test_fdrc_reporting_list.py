from faker import Factory
from hamcrest import assert_that, equal_to, instance_of, contains_string

from data.rest_requests import rest_sale
from model.rest import transactionList, transactionResponse
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.goepay
TERM_ID = '22004'


def test_rest_fdrc_reporting_list():
    sale = rest_sale()
    sale_response = wn.rest(TERM_ID).sale(request=sale)
    assert_that(sale_response, instance_of(transactionResponse))
    s = wn.rest(TERM_ID).reporting_list(terminal_number=TERM_ID, order_id=sale.orderId)
    assert_that(s, instance_of(transactionList))
    assert_that(s.transactionSummary[0].uniqueRef, equal_to(sale_response.uniqueRef))
    assert_that(s.transactionSummary[0].description, contains_string('OK'))

