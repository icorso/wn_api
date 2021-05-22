from data.rest_requests import rest_sale
from wnclient import WNClient

wnclient = WNClient().local.go
TERM_ID = '48001'


def test_integrapay_sale_create():
    p = rest_sale()
    p.autoReady = 'C'
    wnclient.rest(TERM_ID).sale(p)
