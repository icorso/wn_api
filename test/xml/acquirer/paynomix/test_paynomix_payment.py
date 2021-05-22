from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency, PaynomixCard
from data.xml_requests import payment, payment_avs, account_verification_request
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE, ACCOUNT_VERIFICATION_RESPONSE
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22015'


def test_paynomix_auth():
    p = payment()
    p.AUTOREADY = 'Y'
    p.CARDNUMBER = PaynomixCard.rand().cardnumber
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_paynomix_auth_without_cardholder_name():
    p = payment()
    p.AUTOREADY = 'Y'
    p.CARDNUMBER = PaynomixCard.rand().cardnumber
    p.CARDHOLDERNAME = None
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_paynomix_sale():
    p = payment()
    p.AUTOREADY = 'C'
    p.CARDNUMBER = PaynomixCard.rand().cardnumber
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_paynomix_sale_partial_refund():
    p = payment(amount=random_amount(digits=2))
    p.AUTOREADY = 'C'
    p.CARDHOLDERNAME = None
    p.CARDNUMBER = PaynomixCard.rand().cardnumber
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    uniqueref = response.UNIQUEREF
    amount = p.AMOUNT / 2
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_paynomix_auth_partial_refund():
    p = payment(amount=random_amount(digits=2))
    p.AUTOREADY = 'Y'
    p.CARDHOLDERNAME = None
    p.CARDNUMBER = PaynomixCard.rand().cardnumber
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    uniqueref = response.UNIQUEREF
    amount = p.AMOUNT / 2
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))
    # This uncaptured Charge was created by a PaymentIntent. You must cancel the
    # PaymentIntent to reverse the authorization instead of refunding the Charge directly.


def test_paynomix_sale_full_refund():
    """Refund"""
    p = payment(amount=random_amount(digits=2))
    p.AUTOREADY = 'C'
    p.CARDNUMBER = PaynomixCard.rand().cardnumber

    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    uniqueref = response.UNIQUEREF
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, p.AMOUNT, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_paynomix_auth_full_refund():
    """Void"""
    p = payment()
    p.AUTOREADY = 'Y'
    p.CARDNUMBER = PaynomixCard.rand().cardnumber

    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    uniqueref = response.UNIQUEREF
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, p.AMOUNT, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_paynomix_declined():
    p = payment_avs()
    p.AMOUNT = random_amount(minorunits=1)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))
    assert_that(response.RESPONSETEXT, equal_to('Declined'))


def test_paynomix_account_verification():
    response = wn.xml(TERM_ID).account_verification(account_verification_request())
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('UNVERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to('Declined'))
