from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.rest_requests import rest_reversal
from data.xml_requests import payment, unreferenced_refund
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE, UNREFERENCEDREFUNDRESPONSE
from model.rest import transactionResponse
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.go
TERM_ID = '21016'
VISA_CARDS = ['4658074914430378', '4491954376604191', '4305505400565786', '4783947410989336']


def test_tsys_referenced_card_refund():
    p = payment()
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    uniqueref = payment_response.UNIQUEREF
    amount = p.AMOUNT / 2
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_tsys_void_referenced_card_refund():
    p = payment()
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    uniqueref = payment_response.UNIQUEREF
    amount = p.AMOUNT / 2
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))

    reversal_response = wn.rest(terminal_id=TERM_ID).reversal(rest_reversal(refund_response.UNIQUEREF))
    assert_that(reversal_response, instance_of(transactionResponse))


def test_tsys_unreferenced_refund():
    p = unreferenced_refund()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(UNREFERENCEDREFUNDRESPONSE))


def test_tsys_void_unreferenced_refund():
    p = unreferenced_refund()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(UNREFERENCEDREFUNDRESPONSE))

    reversal_response = wn.rest(terminal_id=TERM_ID).reversal(rest_reversal(response.UNIQUEREF))
    assert_that(reversal_response, instance_of(transactionResponse))
