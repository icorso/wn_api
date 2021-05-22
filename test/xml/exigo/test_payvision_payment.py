from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import securecard_registration, payment_securecard, payment_avs
from model.gateway import PAYMENTRESPONSE, SECURECARDREGISTRATIONRESPONSE, REFUNDRESPONSE, CUSTOMFIELD
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.go
TERM_ID = '21012'


def payvision_payment():
    payment_request = payment_avs()
    payment_request.AUTOREADY = 'C'
    return payment_request


def test_payvision_securecard_payment_ok():
    securecard = securecard_registration()

    sc_response = wn.xml(TERM_ID).secure_card_registration(securecard)
    assert_that(sc_response, instance_of(SECURECARDREGISTRATIONRESPONSE))

    p = payment_securecard(cardreference=sc_response.CARDREFERENCE)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_payvision_keyed_payment_ok():
    p = payvision_payment()
    p.CUSTOMFIELD = [
        CUSTOMFIELD(NAME='USERAGENT', valueOf_=fake.user_agent()),
    ]
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_payvision_partial_refund():
    p = payvision_payment()
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    amount = round(p.AMOUNT / 2)
    refund_response = wn.xml(TERM_ID).refund(uniqueref, amount)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_payvision_full_refund():
    p = payvision_payment()
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    refund_response = wn.xml(TERM_ID).refund(uniqueref, p.AMOUNT)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))