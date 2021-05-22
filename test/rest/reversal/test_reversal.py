from hamcrest import assert_that, is_not, instance_of, equal_to

from data.rest_requests import rest_sale, rest_reversal
from model.rest import transactionResponse
from wnclient import WNClient

wn = WNClient().vagrant.go
TERM_ID = '21001'


def test_reversal_ok():
    sale_response = wn.rest(TERM_ID).sale(rest_sale())

    assert_that(sale_response.uniqueRef, is_not(None))
    reversal_response = wn.rest(TERM_ID).reversal(rest_reversal(sale_response.uniqueRef))

    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))


def test_reversal_closed_transaction():
    reversal_response = wn.rest(TERM_ID).reversal(rest_reversal('G5X8BW45BM'))

    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))
