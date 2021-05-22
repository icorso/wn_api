import random

from faker import Factory
from hamcrest import equal_to, assert_that, instance_of

from constants import TransactionType
from data.xml_requests import payment, refund, securecard_registration, payment_securecard
from model.gateway import REFUNDRESPONSE, PAYMENTRESPONSE, SECURECARDREGISTRATIONRESPONSE
from wnclient import WNClient
fake = Factory.create()

wn = WNClient()
TERM_ID = '21005'

'''
Valid cards:
378282246310005	American Express
371449635398431	American Express
36259600000004	Diners Club*
6011111111111117	Discover
3530111333300000	JCB
6304000000000000	Maestro
5555555555554444	Mastercard
2223000048400011	Mastercard
'''

base_payment = payment()
base_payment.AUTOREADY = 'C'
base_payment.CARDNUMBER = random.choice(['4111111111111111', '4005519200000004', '4012000033330026', '4009348888881881',
                                         '4012000077777777', '4217651111111119', '4500600000000061', '4012888888881881',
                                         '4217651111111119', '4500600000000061'])
base_payment.CVV = '999'


def test_braintree_keyed_card_payment_ok():
    response = wn.local.go.xml(TERM_ID).payment(base_payment)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_braintree_keyed_card_payment_cvv_not_verified():
    p = payment()
    p.AUTOREADY = 'C'
    p.CARDNUMBER = '4111111111111111'
    p.CVV = '201'
    response = wn.local.go.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_braintree_keyed_card_payment_declined():
    p = payment()
    p.CARDNUMBER = '4111111111111111'
    p.AMOUNT = 2086.00
    p.AUTOREADY = 'C'
    response = wn.local.go.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSETEXT, equal_to('PayPal Transaction Limit Exceeded The settings o'))


def test_braintree_settlement_declined():
    p = payment()
    p.CARDNUMBER = '4111111111111111'
    p.AMOUNT = 4003.00  # Already Captured
    p.AUTOREADY = 'C'
    response = wn.local.go.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_braintree_settlement_pending():
    p = payment()
    p.CARDNUMBER = '4111111111111111'
    p.AMOUNT = 4002.00  # Settlement Pending
    p.AUTOREADY = 'C'
    response = wn.local.go.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_braintree_secure_card_registration_success():
    sc = securecard_registration()
    sc.CARDNUMBER = base_payment.CARDNUMBER
    response = wn.local.go.xml(TERM_ID).payment(sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


def test_braintree_secure_card_payment_success():
    p = payment_securecard(cardreference='2967536794691477', amount=fake.pydecimal(1, 2, True))
    p.AUTOREADY='C'
    p.CVV = '999'
    response = wn.local.go.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_braintree_refund_settled_transaction_ok():
    p = refund(uniqueref='BA0KWGJQYR', amount=0.02)
    response = wn.local.go.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(REFUNDRESPONSE))


def test_braintree_refund_not_settled_transaction_declined():
    p = base_payment
    response = wn.local.go.xml(TERM_ID).payment(p)

    p = refund(uniqueref=response.UNIQUEREF, amount=round(base_payment.AMOUNT, 2))
    response = wn.local.go.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(REFUNDRESPONSE))
    assert_that(response.RESPONSETEXT, equal_to('Declned'))

