import random

from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import payment_avs, payment_chp
from model.gateway import PAYMENTRESPONSE
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.go
TERM_ID = '21009'


def integrapay_payment():
    """
    Authorization declined amounts:
        31 = Invalid card
        54 = Expired card
        51 = Declined
        61 = Insufficient Funds
        96 = Technical failure
    Capture declined amount (cents):
        11 = Failed invalid amount (“F” response)
        12 = Failed declined (“F” response)
        13 = Temporarily unable to process (“R” response)
    """
    payment_request = payment_avs()
    payment_request.CVV = '123'
    payment_request.AUTOREADY = 'N'
    payment_request.AMOUNT = fake.pydecimal(1, 2, True) + 1
    return payment_request

DECLINED_AMOUNT = random.choice([{'Invalid Credit Card': 1.31}])


def test_integrapay_keyed_avs_payment_ok():
    p = integrapay_payment()
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_integrapay_declined_payment_invalid_card():
    p = integrapay_payment()
    p.AMOUNT = 1.31
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))
    assert_that(response.RESPONSETEXT, equal_to('Invalid credit card'))


def test_integrapay_declined_capture_payment_invalid_amount():
    """ F response """
    p = integrapay_payment()
    p.AMOUNT = 1.13
    p.AUTOREADY = 'Y'
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_integrapay_declined_capture_payment_temp_unable_process():
    """ R response """
    p = integrapay_payment()
    p.AMOUNT = 2.13
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_integrapay_preauth_payment_ok():
    p = integrapay_payment()
    p.AUTOREADY = 'N'
    p.AMOUNT = fake.pydecimal(1, 2, True) + 1
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_integrapay_chp_payment_ok():
    p = payment_chp()
    p.AMOUNT = fake.pydecimal(1, 2, True) + 1
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    # <RESPONSETEXT>[Card.Ccv]CCV number is required</RESPONSETEXT>
