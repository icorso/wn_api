import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import payment, account_verification_request
from model.gateway import PAYMENTRESPONSE, PREAUTHRESPONSE, ACCOUNT_VERIFICATION_RESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.go
TERM_ID = '21001'


@pytest.mark.parametrize('header', [
    # TERM_ID, '"', ''
    '{&quot;/xmlpayment&quot;:[&quot;User-Agent&quot;,&quot;merchant&quot;]}'
])
def test_terminal_header_payment(header):
    # {"/xmlpayment":["User-Agent","terminal"]}
    # should be logged as: 2020-06-01 14:05:48,006 INFO  [default task-2] [com.merchant.filter.
    # RequestHeadersLoggingFilter] - Request - servletPath=/xmlpayment - RemoteAddr=127.0.0.1 -
    #  ContentLength=688 - Headers={"User-Agent":["python-requests/2.20.0"],"terminal":["21001"]}
    p = payment()
    response = wn.with_headers({'terminal': header}).xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_all_headers_payment():
    # System settings LOGGING_REQUEST_HEADERS={"/xmlpayment":["ALL"]} logs all headers sent;
    # should be logged all header
    p = payment()
    response = wn.with_headers({'terminal': TERM_ID, 'merchant': 'Global 1', 'LastHeader': 'last header value'})\
        .xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_preauth_terminal_header():
    response = wn.with_headers({'terminal': TERM_ID, 'merchant': 'Global 1', 'LastHeader': 'last header value'})\
        .xml(TERM_ID).preauth()
    assert_that(response, instance_of(PREAUTHRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_terminal_cloud_header_normal():
    # 2020-09-10 10:26:14,698 DEBUG [str(fake.random_number(32)] [default task-13] [com.merchant.XMLPaymentServlet] - Document Valid
    # ...
    # 2020-09-10 10:26:15,527 DEBUG [str(fake.random_number(32)] [default task-13] [com.worldnettps.common.CustomHttpHandler] - Deleting request id:6003852278
    # 2020-09-10 10:26:15,527 DEBUG [str(fake.random_number(32)] [default task-13] [com.worldnettps.common.CustomHttpHandler] - processing time:855 ms
    response = wn.with_headers({'X-Cloud-Trace-Context': "%s/%s" % (str(fake.random_number(32)), 'XML' + str(fake.random_number(17)))}).xml(terminal_id=TERM_ID)\
        .account_verification(account_verification_request())
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_terminal_cloud_header_500_symbols():
    response = wn.with_headers({'X-Cloud-Trace-Context': "%s/%s" % (str(fake.random_number(500)), 'XML' + str(fake.random_number(500)))})\
        .xml(terminal_id=TERM_ID).account_verification(account_verification_request())
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))


def test_terminal_cloud_header_empty():
    response = wn.with_headers({'X-Cloud-Trace-Context': "%s/%s" % ('', '')})\
        .xml(terminal_id=TERM_ID).account_verification(account_verification_request())
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))


@pytest.mark.parametrize('symbol', ['ç', '\'', '"'])
def test_terminal_cloud_header_empty(symbol):
    response = wn.with_headers({'X-Cloud-Trace-Context': "%s/%s" % (symbol, symbol)})\
        .xml(terminal_id=TERM_ID).account_verification(account_verification_request())
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))