from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import securecard_registration, payment_securecard, payment_avs
from model.gateway import PAYMENTRESPONSE, SECURECARDREGISTRATIONRESPONSE, REFUNDRESPONSE
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.go
TERM_ID = '21019'

# 2019-03-15 14:26:01,556 INFO  [default task-29] [com.merchant.bank.netaxcept.NetAxceptConnectionPool]
# - Resource initialization/invocation was not successful, url: null/Process.aspx
# Also have not enough terminal credentials for testing


def test_netaxcept_securecard_payment_ok():
    securecard = securecard_registration()

    sc_response = wn.xml(TERM_ID).secure_card_registration(securecard)
    assert_that(sc_response, instance_of(SECURECARDREGISTRATIONRESPONSE))

    p = payment_securecard(cardreference=sc_response.CARDREFERENCE)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_netaxcept_keyed_payment_ok():
    request = payment_avs()
    request.AUTOREADY = 'C'

    response = wn.xml(TERM_ID).payment(request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_netaxcept_partial_refund():
    p = payment_avs()
    p.AUTOREADY = 'C'
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    amount = round(p.AMOUNT / 2)
    refund_response = wn.xml(TERM_ID).refund(uniqueref, amount)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_netaxcept_full_refund():
    p = payment_avs()
    p.AUTOREADY = 'C'
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    refund_response = wn.xml(TERM_ID).refund(uniqueref, p.AMOUNT)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))
