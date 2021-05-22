import random

import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import TransactionType, TerminalType, Currency, CashFlowsSecureCard
from data.xml_requests import payment_avs, payment, unreferenced_refund, payment_securecard, securecard_registration
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE, UNREFERENCEDREFUNDRESPONSE, SECURECARDREGISTRATIONRESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22001'
VISA_CARDS = ['4658074914430378', '4491954376604191', '4305505400565786', '4783947410989336']
VISA_DECLINED = ['4716564020255842', '4716565746302560', '4716561433580311', '4716562511346815', '4716566251064728']
MC_DECLINED = ['5338738114454702', '5338734358808885', '5338735177212688', '5338731017881618', '5338738220454562']


@pytest.mark.parametrize('card', CashFlowsSecureCard)
def test_elavon_securecard_registration(card):
    sc = securecard_registration(cvv=card.cvv)
    sc.CARDNUMBER = card.cardnumber
    sc.MERCHANTREF = card.merchant_ref
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


def test_elavon_moto_approved_payment():
    p = payment()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_elavon_recurring_override_approved_payment():
    terminal = wn.boarding().get_terminal(TERM_ID)
    terminal.bankSettings.allowRecurring = False
    wn.boarding().update_terminal(terminal)

    sc = wn.xml(TERM_ID).secure_card_search(CashFlowsSecureCard.VISA_UNSC.merchant_ref)
    sc_payment = wn.xml(terminal_id=TERM_ID).payment(payment_securecard(cardreference=sc.CARDREFERENCE))

    p = payment()
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    p.CARDNUMBER = CashFlowsSecureCard.VISA_UNSC.cardnumber
    p.CARDEXPIRY = sc.CARDEXPIRY
    p.RECURRINGTXNREF = sc_payment.UNIQUEREF
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    terminal.bankSettings.allowRecurring = True
    wn.boarding().update_terminal(terminal)


def test_elavon_avs_payment():
    wn.boarding().update_terminal_avs(TERM_ID)
    p = payment_avs()
    p.TERMINALTYPE = TerminalType.INTERNET,
    p.TRANSACTIONTYPE = TransactionType.INTERNET
    p.CARDNUMBER = random.choice(VISA_CARDS)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    # Should be AVS data in the logs:
    # <AVS><AVSIndicator>1</AVSIndicator><AVSData1>_ADDRESS1_</AVSData1><AVSData2>_POSTCODE_</AVSData2></AVS>

    wn.boarding().update_terminal_avs(TERM_ID, enable_avs=False)


def test_elavon_referenced_refund():
    p = payment_avs()
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    uniqueref = payment_response.UNIQUEREF
    amount = p.AMOUNT / 2
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_elavon_full_refund():
    """Void"""
    p = payment()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    uniqueref = response.UNIQUEREF
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, p.AMOUNT, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_elavon_unreferenced_refund():
    p = unreferenced_refund()
    p.CARDDETAILS.CARDNUMBER = random.choice(VISA_CARDS)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(UNREFERENCEDREFUNDRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_elavon_referral():
    p = payment(amount=1.02)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('R'))
    assert_that(response.RESPONSETEXT, equal_to('REFERRAL'))


def test_elavon_declined():
    p = payment(amount=1.03)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))
    assert_that(response.RESPONSETEXT, equal_to('CVV FAILURE'))

