import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency, SecureCard
from data.xml_requests import payment_chp, payment_chp_ncb, unreferenced_refund, payment_chp_jets
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE, UNREFERENCEDREFUNDRESPONSE, ERROR
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.ncb
TERM_ID = '23001'


@pytest.mark.parametrize('card_number', [
    SecureCard.VISA_DEBIT.cardnumber,
    SecureCard.MASTERCARD_DEBIT.cardnumber,
    '7777770550770642',    # ncb keyed
    '5603488746985'])      # maestro
def test_ncb_chp_payment_debit_card(card_number):
    trackdata = ';%s=%s10114991888?' % (card_number, fake.credit_card_expire(date_format='%y%m'))

    p = payment_chp(currency=Currency.JMD)
    p.TRACKDATA = trackdata
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    refund_response = wn.xml(TERM_ID).refund(uniqueref=payment_response.UNIQUEREF,
                                             amount=round(p.AMOUNT/2, 2), currency=Currency.JMD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


@pytest.mark.parametrize('card_number', ['4303219179808797', '6690016894469491'])
def test_ncb_jets_ncb_refund_not_allowed(card_number):
    trackdata = ';%s=%s10114991888?' % (card_number, fake.credit_card_expire(date_format='%y%m'))

    p = payment_chp(currency=Currency.JMD)
    p.TRACKDATA = trackdata
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    refund_response = wn.xml(TERM_ID).refund(uniqueref=payment_response.UNIQUEREF,
                                             amount=round(p.AMOUNT/2, 2), currency=Currency.JMD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


@pytest.mark.parametrize('card_number', ['4303219179808797', '6690016894469491'])
def test_ncb_jets_ncb_full_refund(card_number):
    trackdata = ';%s=%s10114991888?' % (card_number, fake.credit_card_expire(date_format='%y%m'))

    p = payment_chp(currency=Currency.JMD)
    p.TRACKDATA = trackdata
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    refund_response = wn.xml(TERM_ID).refund(uniqueref=payment_response.UNIQUEREF, amount=p.AMOUNT, currency=Currency.JMD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_ncb_full_refund():
    payment_request = payment_chp(currency=Currency.JMD)
    response = wn.xml(TERM_ID).payment(payment_request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    response = wn.xml(TERM_ID).refund(uniqueref=response.UNIQUEREF, amount=round(payment_request.AMOUNT, 2), currency=Currency.JMD)
    assert_that(response, instance_of(REFUNDRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_ncb_chp_discover_payment():
    p = payment_chp(cardtype='discover', currency=Currency.JMD)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_ncb_chp_discover_partial_refund():
    p = payment_chp(cardtype='discover', currency=Currency.JMD)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))

    uniqueref = response.UNIQUEREF
    amount = p.AMOUNT / 2
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount, Currency.JMD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_ncb_chp_discover_full_refund():
    p = payment_chp(cardtype='discover', currency=Currency.JMD)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))

    uniqueref = response.UNIQUEREF
    amount = p.AMOUNT
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount, currency=Currency.JMD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_ncb_unreferenced_refund_not_allowed():
    p = unreferenced_refund(currency=Currency.JMD)
    refund_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(refund_response, instance_of(ERROR))
    assert_that(refund_response.ERRORSTRING, equal_to('UNREFERENCED REFUNDS NOT ALLOWED'))
