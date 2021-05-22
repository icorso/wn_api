from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import TransactionType, Currency
from data.xml_requests import securecard_registration, payment_securecard, payment_avs, payment
from model.gateway import PAYMENTRESPONSE, SECURECARDREGISTRATIONRESPONSE, REFUNDRESPONSE, CUSTOMFIELD
from utils import random_card
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.go
TERM_ID = '21008'

'''
https://www.cybersource.com/developers/getting_started/test_and_manage/l
Valid cards:
CYBERSOURCESOAP_CARD = '4000100011112224'

'''

CARD_NUM = '4111111111111111'


def test_cybersourcesoap_securecard_payment_ok():
    securecard = securecard_registration()
    securecard.CARDNUMBER = CARD_NUM

    sc_response = wn.xml(TERM_ID).secure_card_registration(securecard)
    assert_that(sc_response, instance_of(SECURECARDREGISTRATIONRESPONSE))

    response = wn.xml(TERM_ID).payment(payment_securecard(cardreference=sc_response.CARDREFERENCE))
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_cybersourcesoap_payment_ok():
    request = payment_avs()
    request.ORDERID = str(fake.random_number(7, True))
    request.AUTOREADY = 'C'
    request.CARDNUMBER = CARD_NUM

    response = wn.xml(TERM_ID).payment(request)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_cybersourcesoap_payment_declined():
    request = payment_avs()
    request.ORDERID = str(fake.random_number(7, True))
    request.AUTOREADY = 'C'
    request.CARDNUMBER = CARD_NUM
    request.EMAIL = None

    response = wn.xml(TERM_ID).payment(request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))


def test_cybersourcesoap_payment_recurring_declined():
    request = payment_avs()
    request.TRANSACTIONTYPE = TransactionType.RECURRING
    request.ORDERID = str(fake.random_number(7, True))
    request.AUTOREADY = 'C'
    request.CARDNUMBER = random_card().cardnumber
    request.EMAIL = None
    request.CUSTOMFIELD = [CUSTOMFIELD(NAME='USERAGENT', valueOf_=fake.user_agent()[:100])]

    response = wn.xml(TERM_ID).payment(request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))


def test_cybersourcesoap_partial_refund():
    p = payment_avs()
    p.ORDERID = str(fake.random_number(7, True))
    p.AUTOREADY = 'C'
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    amount = round(p.AMOUNT / 2)
    refund_response = wn.xml(TERM_ID).refund(uniqueref, amount, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))
