import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import TransactionType, Currency, CashFlowsSecureCard
from data.xml_requests import securecard_registration, payment_avs, stored_subscription, payment_securecard
from model.gateway import PAYMENTRESPONSE, SECURECARDREGISTRATIONRESPONSE, CUSTOMFIELD, \
    ADDSTOREDSUBSCRIPTIONRESPONSE
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.go
TERM_ID = '21023'


def allpago_payment():
    """
    Terminal and currency should be Mexico / MXN
    """
    payment_request = payment_avs(currency=Currency.MXN, amount=0.1)
    payment_request.CVV = '123'
    payment_request.AUTOREADY = 'C'
    return payment_request


@pytest.mark.parametrize('merchant_ref, name, length', {
    ('ss_limited', 'Limited stored subscription', 3),
    ('ss_unlimited', 'Unlimited stored subscription', 0),
    ('ss_limited_before_cof', 'Limited stored subscription before CoF', 3),
    ('ss_unlimited_before_cof', 'Unlimited stored subscription before CoF', 0),
})
def test_add_stored_subscriptions(merchant_ref, name, length):
    ss = stored_subscription()
    ss.MERCHANTREF = merchant_ref
    ss.NAME = name
    ss.LENGTH = length
    response = wn.xml(TERM_ID).add_stored_subscription(request=ss, currency=Currency.MXN)
    assert_that(response, instance_of(ADDSTOREDSUBSCRIPTIONRESPONSE))


@pytest.mark.parametrize('card', CashFlowsSecureCard)
def test_allpago_securecard_registration(card):
    sc = securecard_registration(cvv=card.cvv)
    sc.CARDNUMBER = card.cardnumber
    sc.MERCHANTREF = card.merchant_ref
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


def test_allpago_keyed_payment_ok():
    p = allpago_payment()
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_allpago_keyed_payment_custom_field():
    p = allpago_payment()
    p.CUSTOMFIELD = [CUSTOMFIELD(NAME='PRODUCT', valueOf_=fake.text(20)),
                     CUSTOMFIELD(NAME='MERCHANT_SITENAME', valueOf_=fake.text(20))]
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_allpago_recurring_payment_initial():
    terminal = wn.boarding().get_terminal(TERM_ID)
    terminal.bankSettings.allowRecurring = True
    wn.boarding().update_terminal(terminal)

    p = allpago_payment()
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_allpago_recurring_payment_referenced():
    terminal = wn.boarding().get_terminal(TERM_ID)
    terminal.bankSettings.allowRecurring = False
    wn.boarding().update_terminal(terminal)

    p1 = allpago_payment()
    response1 = wn.xml(TERM_ID).payment(p1)

    p = allpago_payment()
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    p.CARDNUMBER = p1.CARDNUMBER
    p.CARDEXPIRY = p1.CARDEXPIRY
    p.RECURRINGTXNREF = response1.UNIQUEREF
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    terminal.bankSettings.allowRecurring = False
    wn.boarding().update_terminal(terminal)


def test_cashflows_securecard_payment_ecommerce_CIT():
    card = CashFlowsSecureCard.VISA_INST
    search_response = wn.xml(TERM_ID).secure_card_search(card.merchant_ref)

    p = payment_securecard(cardreference=search_response.CARDREFERENCE)
    p.CURRENCY = Currency.MXN.name
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))
    assert_that(response.RESPONSETEXT, equal_to('empty CVV for VISA,MASTER, AMEX not allowed'))