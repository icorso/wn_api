import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency, SecureCard
from data.rest_requests import rest_reversal
from data.xml_requests import payment_chp, payment_chp_ncb, unreferenced_refund
from model.gateway import PAYMENTRESPONSE, ERROR
from model.rest import transactionResponse, serviceError
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.ncb
TERM_ID = '24001'
CURRENCY = Currency.JMD


def test_rest_ncb_reversal_ok():
    p = payment_chp_ncb()
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    reversal_response = wn.rest(TERM_ID).reversal(rest_reversal(response.UNIQUEREF))
    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))


@pytest.mark.parametrize('card_number', ['4303219179808797', '6690016894469491'])
def test_rest_ncb_jets_ncb_debit_refunds_not_allowed(card_number):
    trackdata = ';%s=%s10114991888?' % (card_number, fake.credit_card_expire(date_format='%y%m'))

    p = payment_chp(currency=CURRENCY)
    p.TRACKDATA = trackdata
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    refund_response = wn.rest(TERM_ID).refund_referenced(uniqueref=payment_response.UNIQUEREF,
                                                         amount=round(p.AMOUNT/2, 2), currency=CURRENCY)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Can\'t refund transaction'))


@pytest.mark.parametrize('card_number', ['4303219179808797', '6690016894469491'])
def test_rest_ncb_jets_ncb_debit_unreferenced_refunds_not_allowed(card_number):
    p = unreferenced_refund()
    p.CARDDETAILS.CARDNUMBER = card_number
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('UNREFERENCED REFUNDS NOT ALLOWED'))


@pytest.mark.parametrize('card_number', ['4303219179808797', '6690016894469491'])
def test_rest_ncb_jets_ncb_debit_reversal(card_number):
    trackdata = ';%s=%s10114991888?' % (card_number, fake.credit_card_expire(date_format='%y%m'))

    p = payment_chp(currency=CURRENCY)
    p.TRACKDATA = trackdata
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    refund_response = wn.rest(TERM_ID).reversal(rest_reversal(payment_response.UNIQUEREF))
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))


@pytest.mark.parametrize('card_number', [SecureCard.VISA_DEBIT.cardnumber, SecureCard.MASTERCARD_DEBIT.cardnumber])
def test_rest_allowed_debit_cards_refunds(card_number):
    trackdata = ';%s=%s10114991888?' % (card_number, fake.credit_card_expire(date_format='%y%m'))

    p = payment_chp(currency=CURRENCY)
    amount = round(p.AMOUNT / 2, 2)
    p.TRACKDATA = trackdata
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    refund_response = wn.rest(TERM_ID).refund_referenced(uniqueref=payment_response.UNIQUEREF, amount=amount, currency=CURRENCY)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(float(amount/-1)))

