import random

from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import TransactionType, Currency
from data.xml_requests import securecard_registration, payment_securecard, payment_avs
from model.gateway import PAYMENTRESPONSE, SECURECARDREGISTRATIONRESPONSE, REFUNDRESPONSE, CUSTOMFIELD
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.go
TERM_ID = '21013'

# WARNING! no data stored in related table securepay_transaction


def securepay_payment():
    """
    Payment amounts to simulate approved transactions:
    $1.00 (100)
    $1.08 (108)
    $105.00 (10500)
    $105.08 (10508)
    (or any total ending in 00, 08)
    Payment amounts to simulate declined transactions:
    $1.51 (151)
    $1.05 (105)
    $105.51 (10551)
    $105.05 (10505)
    (or any totals not ending in 00, 08)
    """
    payment_request = payment_avs()
    payment_request.CARDNUMBER = '4444333322221111'  # cardexpiry 08 / 23 (or any date greater then today)
    payment_request.CVV = '123'
    payment_request.AMOUNT = random.choice([1.0, 1.08, 105.0, 105.08])
    payment_request.AUTOREADY = 'C'
    return payment_request

DECLINED_AMOUNT = random.choice([1.51, 1.05, 105.51, 105.05])


def test_securepay_securecard_payment_decline():
    securecard = securecard_registration()

    sc_response = wn.xml(TERM_ID).secure_card_registration(securecard)
    assert_that(sc_response, instance_of(SECURECARDREGISTRATIONRESPONSE))

    p = payment_securecard(cardreference=sc_response.CARDREFERENCE)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))


def test_securepay_keyed_payment_ok():
    p = securepay_payment()
    p.CUSTOMFIELD = [
        CUSTOMFIELD(NAME='USERAGENT', valueOf_=fake.user_agent()),
    ]
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_securepay_keyed_payment_decline():
    p = securepay_payment()
    p.AMOUNT = DECLINED_AMOUNT
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))


def test_securepay_partial_refund_decline():
    p = securepay_payment()
    p.AMOUNT = 105.00
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    amount = round(p.AMOUNT / 2)
    refund_response = wn.xml(TERM_ID).refund(uniqueref, amount, Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_securepay_full_refund_decline():
    p = securepay_payment()
    p.AMOUNT = 105.00
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    refund_response = wn.xml(TERM_ID).refund(uniqueref, p.AMOUNT, Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))
