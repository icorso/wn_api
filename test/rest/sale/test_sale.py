import pytest
from hamcrest import assert_that, equal_to, instance_of

from constants import Currency
from data.rest_requests import rest_sale, rest_androidpay_sale, rest_emv_tlv_sale, rest_applepay_sale, rest_track2_sale
from model.rest import terminalType, transactionResponse
from wnclient import WNClient

wn = WNClient().vagrant.go
TERM_ID = '21001'


@pytest.mark.parametrize('cardtype', ['visa', 'amex', 'mastercard', 'discover'])
def test_rest_sale_main_cardtypes(cardtype):
    wn.rest(TERM_ID).sale(currency=Currency.USD, request=rest_sale(cardtype=cardtype))


def test_rest_unknown_card_keyed_sale():
    r = rest_sale()
    r.paymentMethod.keyedCard.cardNumber = '6385087787065456'
    r.paymentMethod.keyedCard.cardType = ''
    wn.rest(TERM_ID).sale(r)


def test_rest_wrong_card_type_keyed_sale():
    r = rest_sale(cardtype='mastercard')
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(transactionResponse))


def test_rest_unknown_card_track2_sale():
    r = rest_track2_sale()
    # raw track data ;6385087787065456=25121011796251900000?
    r.paymentMethod.track2.encryptedData = 'B3F237FDC311B6241A4A73A243080C5FA2196F4B62DE2C0F'
    wn.rest(TERM_ID).sale(r)


def test_rest_emv_sale():
    wn.rest(TERM_ID).sale(rest_emv_tlv_sale(currency=Currency.USD))


def test_androidpay_rest_sale():
    payment = rest_androidpay_sale()
    wn.go.rest('21003').sale(payment)


def test_applepay_rest_sale():
    payment = rest_applepay_sale()
    payment.account.terminalType = terminalType.INTERNET
    payment.amount.amount = 66.00
    wn.go.rest('21003').sale(payment)


def test_settlement():
    response = wn.http.test_settle(params={'terminal_id': TERM_ID})
    assert_that(response.status_code, equal_to(200))


def test_login():
    wn.http.login('0', 'super', '1')