from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import TransactionType, Currency
from data.xml_requests import securecard_registration, payment_securecard, payment
from model.gateway import PAYMENTRESPONSE, SECURECARDREGISTRATIONRESPONSE, REFUNDRESPONSE
from wnclient import WNClient

fake = Factory.create()

wn = WNClient()
TERM_ID = '21011'


def test_maxconnect_securecard_payment_ok():
    securecard = securecard_registration(cardtype='visa')

    sc_response = wn.local.go.xml(TERM_ID).secure_card_registration(securecard)
    assert_that(sc_response, instance_of(SECURECARDREGISTRATIONRESPONSE))

    p = payment_securecard(cardreference=sc_response.CARDREFERENCE)
    p.CURRENCY = 'JPY'
    response = wn.local.go.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_maxconnect_keyed_payment_ok():
    request = payment()
    request.CURRENCY = 'JPY'
    request.ORDERID = str(fake.random_number(7, True))
    request.AUTOREADY = 'C'
    request.AMOUNT = 1000
    request.CARDEXPIRY = '0619'

    response = wn.local.go.xml(TERM_ID).payment(request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_maxconnect_keyed_payment_declined():
    request = payment()
    request.CURRENCY = 'JPY'
    request.TRANSACTIONTYPE = TransactionType.RECURRING
    request.ORDERID = str(fake.random_number(7, True))
    request.AUTOREADY = 'C'
    request.AMOUNT = 2000
    response = wn.local.go.xml(TERM_ID).payment(request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))


def test_maxconnect_partial_refund():
    p = payment()
    p.CURRENCY = 'JPY'
    p.AUTOREADY = 'C'
    payment_response = wn.local.go.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    amount = round(p.AMOUNT / 2)
    refund_response = wn.local.go.xml(TERM_ID).refund(uniqueref, amount)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_maxconnect_full_refund():
    p = payment()
    p.AMOUNT = 3
    p.CURRENCY = 'JPY'
    p.AUTOREADY = 'C'
    payment_response = wn.local.go.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    refund_response = wn.local.go.xml(TERM_ID).refund(uniqueref, p.AMOUNT, currency=Currency.JPY)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))
