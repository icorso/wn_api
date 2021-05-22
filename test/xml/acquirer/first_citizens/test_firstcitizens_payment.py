from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.xml_requests import payment, payment_avs
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE, ERROR
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22016'


def test_firstcitizens_approval():
    p = payment()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_firstcitizens_partial_refund_not_allowed():
    p = payment()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    refund_response = wn.xml(terminal_id=TERM_ID).refund(response.UNIQUEREF, round(p.AMOUNT/2))
    assert_that(refund_response, instance_of(ERROR))
    assert_that(refund_response.ERRORSTRING, equal_to('An error has occurred, please retry'))


def test_firstcitizens_full_refund():
    """Void"""
    p = payment()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    refund_response = wn.xml(terminal_id=TERM_ID).refund(response.UNIQUEREF, p.AMOUNT)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_firstcitizens_declined():
    p = payment_avs()
    p.AMOUNT = random_amount(minorunits=4)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))
    assert_that(response.RESPONSETEXT, equal_to('CVV FAILURE'))


def test_firstcitizens_referral():
    p = payment_avs()
    p.AMOUNT = random_amount(minorunits=1)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('R'))
    assert_that(response.RESPONSETEXT, equal_to('Transaction blocked by issuer'))
