from hamcrest import assert_that, equal_to

from wnclient import WNClient


def test_manage_source_headers():
    header = {'Content-Language': 'fr-Fr'}
    wnclient = WNClient().with_headers(header)
    header.update({'Content-Type': 'application/xml'})
    assert_that(wnclient.xml('1')._session.headers, equal_to(header))


def test_wnclinet_gateway_config():
    wnclinet = WNClient().local.wn

    # default gateway and attributes
    assert_that(wnclinet.gateway.url, equal_to('http://wn:8080'))
    assert_that(wnclinet.gateway.apikey, equal_to('wnkey'))

    # set gateway and url usage in a source
    assert_that(wnclinet.local.ncb.gateway.url, equal_to('http://ncb:8080'))
    assert_that(wnclinet.iron.ncb.xml(terminal_id='1').url,
                equal_to('https://qawsironcb.worldnettps.com/merchant/xmlpayment'))


def test_wnclinet_boarding_config():
    apikey = 'lynxgokey'
    wnclinet = WNClient()
    wnclinet.lynx.go.boarding()

    assert_that(wnclinet.gateway.apikey, equal_to(apikey))
    assert_that(wnclinet.session.headers.get('AuthenticationKey'), equal_to(apikey))
