from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.xml_requests import payment, payment_chp, unreferenced_refund
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE, UNREFERENCEDREFUNDRESPONSE
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.go
TERM_ID = '21016'


def test_sierra_moto_approved_payment():
    p = payment()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_sierra_chp_approved_payment():
    p = payment_chp()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_sierra_referral_payment():
    p = payment()
    p.AMOUNT = random_amount(minorunits=2)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('R'))


def test_sierra_declined_payment():
    p = payment(cardtype='visa')
    p.AMOUNT = random_amount(minorunits=1)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))


def test_sierra_full_refund():
    """Void"""
    p = payment()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    uniqueref = response.UNIQUEREF
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, p.AMOUNT, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_sierra_unreferenced_refund():
    p = unreferenced_refund(currency=Currency.USD)
    refund_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(refund_response, instance_of(UNREFERENCEDREFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))
