from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.xml_requests import securecard_registration, payment_securecard, payment_avs
from model.gateway import PAYMENTRESPONSE, SECURECARDREGISTRATIONRESPONSE, REFUNDRESPONSE, CUSTOMFIELD
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.go
TERM_ID = '21011'


def moneris_payment():
    payment_request = payment_avs().is_multicurrency(False)
    payment_request.AUTOREADY = 'C'
    payment_request.EMAIL = fake.free_email()
    payment_request.CURRENCY = Currency.JPY.name
    return payment_request


def test_moneris_securecard_payment_declined():
    securecard = securecard_registration()

    sc_response = wn.xml(TERM_ID).secure_card_registration(securecard)
    assert_that(sc_response, instance_of(SECURECARDREGISTRATIONRESPONSE))

    p = payment_securecard(cardreference=sc_response.CARDREFERENCE)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_moneris_keyed_payment_ok():
    p = moneris_payment()
    p.AMOUNT = 7.1
    p.CUSTOMFIELD = [
        CUSTOMFIELD(NAME='USERAGENT', valueOf_=fake.user_agent()),
    ]
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_moneris_keyed_payment_declined_cvv():
    p = moneris_payment()
    p.AMOUNT = 3.2
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))
    assert_that(response.RESPONSETEXT, equal_to('CREDIT CARD - CVV Cryptographic error'))


def test_moneris_partial_refund():
    p = moneris_payment()
    p.AMOUNT = 8.1
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    amount = round(p.AMOUNT / 2)
    refund_response = wn.xml(TERM_ID).refund(uniqueref, amount, Currency.JPY)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_moneris_full_refund():
    p = moneris_payment()
    p.AMOUNT = 5.1
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    refund_response = wn.xml(TERM_ID).refund(uniqueref, p.AMOUNT, Currency.JPY)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))
