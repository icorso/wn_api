import random

from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import payment_avs, refund
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.go
TERM_ID = '48001'


def integrapay_payment():
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
    payment_request.CVV = '123'
    payment_request.AUTOREADY = 'C'
    payment_request.AMOUNT = fake.pydecimal(1, 2, True) + 1
    return payment_request

DECLINED_AMOUNT = random.choice([{'Invalid Credit Card': 1.31}])


def test_integrapay_keyed_avs_payment_ok():
    p = integrapay_payment()
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_integrapay_full_refund_ok():
    amount = fake.pydecimal(1, 2, True) + 1
    p = integrapay_payment()
    p.AUTOREADY = 'N'
    p.AMOUNT = amount
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    r = refund(uniqueref=response.UNIQUEREF, amount=amount)
    refund_response = wn.xml(TERM_ID).payment(r)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_integrapay_paprtial_refund_ok():
    amount = fake.pydecimal(1, 2, True) + 1
    p = integrapay_payment()
    p.AUTOREADY = 'N'
    p.AMOUNT = amount
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    r = refund(uniqueref=response.UNIQUEREF, amount=round((amount / 2), 2))
    refund_response = wn.xml(TERM_ID).payment(r)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))
