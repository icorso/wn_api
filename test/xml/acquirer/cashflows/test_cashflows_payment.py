import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency, CashFlowsSecureCard
from data.xml_requests import payment
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
CURRENCY = Currency.EUR
TERM_ID = '22004'


def test_cashflows_approval():
    p = payment(currency=CURRENCY)
    p.CARDNUMBER = CashFlowsSecureCard.VISA_UNSC.cardnumber
    p.CVV = CashFlowsSecureCard.VISA_UNSC.cvv
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_cashflows_settlement_admin():
    p = payment(currency=CURRENCY)
    p.AMOUNT = random_amount(minorunits=9)
    p.CARDNUMBER = CashFlowsSecureCard.VISA_UNSC.cardnumber
    p.CVV = CashFlowsSecureCard.VISA_UNSC.cvv
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_cashflows_partial_refund():
    p = payment(currency=CURRENCY)
    p.CARDNUMBER = CashFlowsSecureCard.VISA_UNSC.cardnumber
    p.CVV = CashFlowsSecureCard.VISA_UNSC.cvv

    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    uniqueref = response.UNIQUEREF
    amount = p.AMOUNT / 2
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount, currency=Currency.EUR)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_cashflows_full_refund():
    """Void"""
    p = payment(currency=CURRENCY)
    p.CARDNUMBER = CashFlowsSecureCard.VISA_UNSC.cardnumber
    p.CVV = CashFlowsSecureCard.VISA_UNSC.cvv

    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    uniqueref = response.UNIQUEREF
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, p.AMOUNT, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


@pytest.mark.parametrize('minorunits, response_text', [
    (1, 'Declined'),
    (3, 'CVV FAILURE'),
    (4, 'CashFlows Error S203'),
    (5, 'Transaction Blocked by CashFlows'),
    (6, 'CashFlows Error Vx26'),
    (7, 'Validation'),
    (8, 'Cancel'),
    (9, 'CashFlows Error null')
])
def test_cashflows_declined(minorunits, response_text):
    """  Minorunits  Cashflows response
        1 D|05084694505|400|D102|Not Authorised|
        3 A|05084928665|400|D102|Authorised|
        4 S|05084951676|000|S203|Response timeout|
        5 B|05084850045|000|D102|Blocked|
        6 V|05085036768|000|Vx26|Validation|
        7 V|05085089125|000|Vx01|Validation|
        8 C|05085138366|000|D102|Cancel|
        9 S|05085175873|null|null|null|
    """
    p = payment(currency=CURRENCY)
    p.CARDNUMBER = CashFlowsSecureCard.VISA_UNSC.cardnumber
    p.CVV = CashFlowsSecureCard.VISA_UNSC.cvv
    p.AMOUNT = random_amount(minorunits=minorunits)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))
    assert_that(response.RESPONSETEXT, equal_to(response_text))


def test_cashflows_referral():
    p = payment(currency=CURRENCY)
    p.AMOUNT = random_amount(minorunits=2)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('R'))
    assert_that(response.RESPONSETEXT, equal_to('Not Authorised'))
