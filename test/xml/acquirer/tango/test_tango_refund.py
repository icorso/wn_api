from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.xml_requests import payment_avs, unreferenced_refund
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE, UNREFERENCEDREFUNDRESPONSE, ERROR
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21004'


def test_tango_referenced_refund_create():
    p = payment_avs()
    p.AUTOREADY = 'C'
    p.CURRENCY = Currency.CAD.name
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    uniqueref = payment_response.UNIQUEREF
    amount = p.AMOUNT / 2
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_tango_unreferenced_refund_create():
    r = unreferenced_refund(currency=Currency.CAD)
    refund_response = wn.xml(terminal_id=TERM_ID).payment(request=r)
    assert_that(refund_response, instance_of(UNREFERENCEDREFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_tango_unreferenced_refund_cancel():
    r = unreferenced_refund(currency=Currency.CAD)
    refund_response = wn.xml(terminal_id=TERM_ID).payment(request=r)
    assert_that(refund_response, instance_of(UNREFERENCEDREFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))

    void_response = wn.xml(terminal_id=TERM_ID).refund(refund_response.UNIQUEREF, refund_response.AMOUNT, currency=Currency.CAD)
    assert_that(void_response, instance_of(ERROR))
    assert_that(refund_response.ERRORSTRING, equal_to('Invalid UNIQUEREF field'))
