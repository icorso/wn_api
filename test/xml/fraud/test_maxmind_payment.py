import random

import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import TransactionType, TerminalType, SecureCard, Currency, EdccCard
from data.boarding.terminal import terminal_draft_256_billing
from data.xml_requests import payment_avs, payment_applepay_visa, payment_chp, payment_securecard, preauth
from model.boarding import terminal
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE, CARDCURRENCYRATERESPONSE, \
    FOREIGNCURRENCYINFORMATION, PREAUTHRESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21001'
EDCC_TERM_ID = '21009'
TERM_ID_MULTICURRENCY = '21002'
VISA_DECLINED = ['4716564020255842', '4716565746302560', '4716561433580311', '4716562511346815', '4716566251064728']
MC_DECLINED = ['5338738114454702', '5338734358808885', '5338735177212688', '5338731017881618', '5338738220454562']


@pytest.mark.parametrize('terminal_type, transaction_type', [(TerminalType.MOTO, TransactionType.MOTO),
                                                             (TerminalType.CHP, TransactionType.CHP)
])
def test_maxmind_moto_chp_payment(terminal_type, transaction_type):
    """There should be no request to MaxMind in the logs"""
    update_terminal_response = wn.boarding().update_terminal_max_mind(TERM_ID, True, True, 100, silence=True)
    assert_that(update_terminal_response, instance_of(terminal))
    request = payment_avs()
    if transaction_type == 0:
        request = payment_chp()

    request.TRANSACTIONTYPE = transaction_type
    request.TERMINALTYPE = terminal_type

    response = wn.xml(terminal_id=TERM_ID).payment(request=request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_maxmind_internet_payment_approved():
    """Check logs for MaxMind data and open_transaction:max_mind_risk_score, fraud_status fields"""
    wn.boarding().update_terminal_max_mind(TERM_ID, True, True, 100, silence=True)

    request = payment_avs()
    request.TRANSACTIONTYPE = TransactionType.INTERNET
    request.TERMINALTYPE = TerminalType.INTERNET

    response = wn.xml(terminal_id=TERM_ID).payment(request=request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_maxmind_internet_preauth_approved():
    """Check logs for MaxMind data and open_transaction:max_mind_risk_score, fraud_status fields"""
    wn.boarding().update_terminal_max_mind(TERM_ID, True, True, 100, silence=True)

    request = preauth()
    request.ADDRESS1 = fake.street_address()
    request.POSTCODE = '48706'
    request.IPADDRESS = fake.ipv4()
    request.CITY = fake.city()
    request.REGION = fake.state_abbr()
    request.COUNTRY = 'US'
    request.AMOUNT = 50

    request.TRANSACTIONTYPE = TransactionType.INTERNET
    request.TERMINALTYPE = TerminalType.INTERNET

    response = wn.xml(terminal_id=TERM_ID).preauth(request=request)
    assert_that(response, instance_of(PREAUTHRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_maxmind_payment_input_invalid_warning():
    """Check logs for MaxMind warning and open_transaction.fraud_status should be 3 and max_mind_risk_score=-1.0
    We have an error from Max Mind : Encountered value at /billing/region that does not meet the required
    constraints."""
    wn.boarding().update_terminal_max_mind(TERM_ID, True, False, 0, silence=True)

    request = payment_avs()
    request.REGION = 'Some region'
    request.TRANSACTIONTYPE = TransactionType.INTERNET
    request.TERMINALTYPE = TerminalType.INTERNET

    response = wn.xml(terminal_id=TERM_ID).payment(request=request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_maxmind_internet_payment_declined_by_risk_score():
    """Check logs for MaxMind data and open_transaction:max_mind_risk_score, fraud_status fields"""
    wn.boarding().update_terminal_max_mind(TERM_ID, True, True, 0.23, silence=True)

    request = payment_avs()
    request.TRANSACTIONTYPE = TransactionType.INTERNET
    request.TERMINALTYPE = TerminalType.INTERNET

    response = wn.xml(terminal_id=TERM_ID).payment(request=request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))
    assert_that(response.RESPONSETEXT, equal_to('RISK REJECTION'))
    wn.boarding().update_terminal_max_mind(TERM_ID, silence=True)


def test_maxmind_internet_payment_declined_by_cvv_and_risk_score():
    """Check logs for MaxMind data and open_transaction:max_mind_risk_score, fraud_status fields"""

    request = payment_avs()
    request.CARDNUMBER = random.choice(VISA_DECLINED)
    request.TRANSACTIONTYPE = TransactionType.INTERNET
    request.TERMINALTYPE = TerminalType.INTERNET

    response = wn.xml(terminal_id=TERM_ID).payment(request=request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))


def test_maxmind_edcc_payment():
    wn.boarding().update_terminal_max_mind(EDCC_TERM_ID, True, True, 100, silence=True)
    edcc_response = wn.xml(terminal_id=EDCC_TERM_ID).get_card_currency_rate(EdccCard.GBP_VISA.cardnum[:6], 1.17)
    assert_that(edcc_response, instance_of(CARDCURRENCYRATERESPONSE))

    fa = FOREIGNCURRENCYINFORMATION(
        CARDCURRENCY=edcc_response.CARDCURRENCY,
        CARDAMOUNT=edcc_response.FOREIGNAMOUNT,
        CONVERSIONRATE=edcc_response.CONVERSIONRATE,
    )

    p = payment_avs()
    p.CARDNUMBER = EdccCard.GBP_VISA.cardnum
    p.AMOUNT = 1.17
    p.FOREIGNCURRENCYINFORMATION = fa
    payment_response = wn.xml(terminal_id=EDCC_TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))


def test_maxmind_approved_multicurrency_payment():
    t = wn.boarding().get_terminal(TERM_ID_MULTICURRENCY)
    t.securityFraud.maxMindActive = True
    t.securityFraud.maxMindRejectOnError = True
    t.securityFraud.maxMindRiskScoreThreshold = 100
    t.unionPayProcessing.draft256Billing = terminal_draft_256_billing()
    wn.boarding().update_terminal(t, silence=True)

    p = payment_avs().is_multicurrency(True)
    p.CURRENCY = Currency.USD.name
    p.TERMINALTYPE = TerminalType.INTERNET
    p.TRANSACTIONTYPE = TransactionType.INTERNET
    response = wn.xml(terminal_id=TERM_ID_MULTICURRENCY).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_maxmind_recurring_securecard_payment():
    p = payment_securecard(cardreference=SecureCard.VISA.card_ref)
    p.TERMINALTYPE = TerminalType.INTERNET,
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_maxmind_refund():
    p = payment_avs()
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    uniqueref = payment_response.UNIQUEREF
    amount = p.AMOUNT / 2
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount, currency=Currency.EUR)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_maxmind_applepay():
    response = wn.xml(terminal_id=TERM_ID).payment(payment_applepay_visa())
    assert_that(response, instance_of(PAYMENTRESPONSE))
