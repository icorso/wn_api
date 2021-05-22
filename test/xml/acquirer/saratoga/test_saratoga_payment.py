import random

from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import TransactionType, TerminalType, StoredCredentialTxType, StoredCredentialUse, SecureCard, Currency
from data.xml_requests import payment_avs, payment, payment_applepay_visa, payment_chp, payment_securecard
from model.gateway import PAYMENTRESPONSE, CUSTOMFIELD, REFUNDRESPONSE, CREDENTIALONFILE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21001'
TERM_ID_CAD = '21015'
TERM_ID_MULTICURRENCY = '21002'
VISA_DECLINED = ['4716564020255842', '4716565746302560', '4716561433580311', '4716562511346815', '4716566251064728']
MC_DECLINED = ['5338738114454702', '5338734358808885', '5338735177212688', '5338731017881618', '5338738220454562']


def test_saratoga_moto_approved_payment():
    p = payment(currency=Currency.USD)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_chp_approved_payment():
    p = payment_chp()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_chp_canada_mastercard_approved_payment():
    p = payment_chp(cardtype='mastercard')
    p.CURRENCY = Currency.CAD.name
    response = wn.xml(terminal_id=TERM_ID_CAD).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_moto_approved_multicurrency_payment():
    p = payment()
    response = wn.xml(terminal_id=TERM_ID_MULTICURRENCY).payment(request=p, is_multicurrency=True)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_moto_inactive_terminal_payment():
    p = payment()
    response = wn.xml(terminal_id='21001').payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_moto_declined_payment():
    p = payment_avs()
    p.CARDNUMBER = random.choice(VISA_DECLINED)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_referral_payment():
    p = payment_avs()
    p.AMOUNT = 1000.02
    p.CARDNUMBER = random.choice(VISA_DECLINED)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('R'))
    assert_that(response.RESPONSETEXT, equal_to('Refer to Issuer\'s special conditions'))


def test_saratoga_pickup_payment():
    p = payment_avs()
    p.AMOUNT = 1000.04
    p.CARDNUMBER = random.choice(VISA_DECLINED)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('C'))
    assert_that(response.RESPONSETEXT, equal_to('Pick Up Card'))


def test_saratoga_recurring_declined_avs_payment():
    p = payment_avs()
    p.TERMINALTYPE = TerminalType.INTERNET,
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    p.CARDNUMBER = random.choice(VISA_DECLINED)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_recurring_declined_avs_cof_payment():
    p = payment_avs()
    p.TERMINALTYPE = TerminalType.INTERNET,
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    p.CARDNUMBER = random.choice(VISA_DECLINED)
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        ORIGINALBRANDTXIDENTIFIER='123456',
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name,
        STOREDCREDENTIALUSE=StoredCredentialUse.RECURRING.name
    )
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_recurring_declined_securecard_payment():
    p = payment_securecard(cardreference=SecureCard.VISA.card_ref)
    p.AMOUNT = 1000.17
    p.TERMINALTYPE = TerminalType.INTERNET,
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))


def test_saratoga_recurring_declined_custom_field_payment():
    """For hard decline update the simulator with codes, e.g.
        13 - Invalid Amount
        12 - Invalid or Expired Transaction
        See chapter "Hard Decline" of FlexPay spec
         https://support.flexpay.io/support/solutions/articles/27000041851-flexpay-api-integration
    """
    p = payment_avs()
    p.TERMINALTYPE = TerminalType.INTERNET
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    p.CARDNUMBER = random.choice(VISA_DECLINED)
    p.CUSTOMFIELD = [CUSTOMFIELD(NAME='USERAGENT', valueOf_=fake.user_agent()[:100])]
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))


def test_saratoga_refund():
    p = payment_avs()
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    uniqueref = payment_response.UNIQUEREF
    amount = p.AMOUNT / 2
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_saratoga_applepay():
    response = wn.xml(terminal_id=TERM_ID).payment(payment_applepay_visa())
    assert_that(response, instance_of(PAYMENTRESPONSE))
