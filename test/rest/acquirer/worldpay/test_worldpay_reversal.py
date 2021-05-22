from faker import Factory
from hamcrest import assert_that, is_not, instance_of, equal_to

from constants import ApiKey, Currency, LocalMerchant
from data.rest_requests import rest_reversal, rest_sale
from model.rest import transactionResponse
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '20008'
CURRENCY = Currency.USD
MERCHANT_ID = LocalMerchant.WN.itemid

wn = WNClient().local.wn.rest(TERM_ID)


def test_worldpay_reversal():
    sale_response = wn.sale(request=rest_sale())

    assert_that(sale_response.uniqueRef, is_not(None))
    reversal_response = wn.reversal(rest_reversal(sale_response.uniqueRef))

    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))
    assert_that(reversal_response.authorizedAmount, equal_to(sale_response.authorizedAmount))
