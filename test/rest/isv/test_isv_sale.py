from constants import Currency, IsvToken
from data.rest_requests import rest_sale
from wnclient import WNClient

wn = WNClient().vagrant.go
TERM_ID = '21001'
ISV_TOKEN = IsvToken.GO.token_rest_api


def test_rest_isv_token_sale():
    wn.with_headers({'isv-integration-token': ISV_TOKEN})\
        .rest(TERM_ID).sale(currency=Currency.USD, request=rest_sale())