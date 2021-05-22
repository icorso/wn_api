from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.xml_requests import payment
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22006'


def test_credorax_declined():
    p = payment()
    # p.AMOUNT = 1000.14  # Invalid Card Number
    # p.AMOUNT = 1000.05  # Do not Honour
    # p.AMOUNT = 1000.05  # CVV FAILURE
    p.AMOUNT = 1000.19  # System error
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))
    assert_that(response.RESPONSETEXT, equal_to('System Error; Re-enter transaction'))


def test_credorax_approval():
    p = payment()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_credorax_partial_refund():
    p = payment()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    uniqueref = response.UNIQUEREF
    amount = p.AMOUNT / 2
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_credorax_full_refund():
    """Void"""
    p = payment()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    uniqueref = response.UNIQUEREF
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, p.AMOUNT, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))
