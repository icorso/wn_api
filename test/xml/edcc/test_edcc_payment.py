from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.xml_requests import payment_edcc
from model.gateway import PAYMENTRESPONSE, CARDCURRENCYRATERESPONSE, ERROR
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21009'
VISA_EDCC = '4485910301709438'  # GPB > USD


def test_get_card_currency_rate():
    card_amount = random_amount()
    response = wn.xml(TERM_ID).get_card_currency_rate(VISA_EDCC[:6], card_amount)
    assert_that(response, instance_of(CARDCURRENCYRATERESPONSE))
    assert_that(response.CARDCURRENCY, equal_to('GBP'))
    assert_that(response.EXCHANGERATESOURCENAME, equal_to('Tsys Saratoga'))


def test_edcc_payment_valid():
    card_amount = random_amount(digits=2)
    response = wn.xml(TERM_ID).get_card_currency_rate(VISA_EDCC[:6], card_amount)

    p = payment_edcc(amount=card_amount,
                     cardnumber=VISA_EDCC,
                     conversion_rate=response.CONVERSIONRATE,
                     card_currency=Currency.GBP,
                     terminal_currency=Currency.USD)
    p.CARDHOLDERNAME = VISA_EDCC
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))


def test_edcc_payment_incorrect_rate():
    card_amount = random_amount(digits=2)
    response = wn.xml(TERM_ID).get_card_currency_rate(VISA_EDCC[:6], card_amount)

    p = payment_edcc(amount=card_amount,
                     cardnumber=VISA_EDCC,
                     conversion_rate=response.CONVERSIONRATE / 2,
                     card_currency=Currency.GBP,
                     terminal_currency=Currency.USD)
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(ERROR))
    assert_that(payment_response.ERRORSTRING, equal_to('Invalid Conversion Rate'))

