from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.xml_requests import payment_chp, payment_avs, payment, unreferenced_refund
from model.gateway import PAYMENTRESPONSE, PREAUTHRESPONSE, REFUNDRESPONSE, UNREFERENCEDREFUNDRESPONSE, ERROR
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22005'


def test_fdrc_keyed_card_payment():
    response = wn.xml(terminal_id=TERM_ID).payment()
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_fdrc_keyed_card_avs_payment():
    response = wn.xml(terminal_id=TERM_ID).payment(payment_avs())
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_fdrc_chp_payment():
    response = wn.xml(TERM_ID).payment(payment_chp())
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_fdrc_declined_chp_payment():
    response = wn.xml(TERM_ID).payment(payment_chp(amount=1000.15))
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_fdrc_preauth():
    response = wn.xml(TERM_ID).preauth()
    assert_that(response, instance_of(ERROR))


def test_fdrc_full_refund():
    """Void"""
    p = payment()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    uniqueref = response.UNIQUEREF
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, p.AMOUNT, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_fdrc_unreferenced_refund():
    p = unreferenced_refund(currency=Currency.USD)
    refund_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(refund_response, instance_of(UNREFERENCEDREFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_fdrc_referral():
    p = payment()
    p.AMOUNT = random_amount(minorunits=2)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('R'))
    assert_that(response.RESPONSETEXT, equal_to('Referred - Skip Trace Info'))
