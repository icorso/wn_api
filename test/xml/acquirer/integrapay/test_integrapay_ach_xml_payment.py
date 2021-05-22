from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.xml_requests import direct_debit_payment
from model.gateway import PAYMENTACHRESPONSE
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.go
TERM_ID = '21009'


def test_ach_integrapay_payment_ok():
    p = direct_debit_payment()
    p.CURRENCY = Currency.USD.name
    p.AMOUNT = random_amount()
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTACHRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_ach_integrapay_payment_with_securecard_ok():
    p = direct_debit_payment()
    p.CURRENCY = 'USD'
    p.ACCOUNT_NUMBER = '2967537600014656'
    p.ACH_SECURE = 'Y'
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTACHRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
