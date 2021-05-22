from hamcrest import assert_that, equal_to, instance_of

from constants import PaynomixCard
from data.rest_requests import rest_sale
from model.rest import transactionResponse
from utils import random_amount
from wnclient import WNClient

wn = WNClient().vagrant.wn
TERM_ID = '22015'


def test_rest_keyed_card_sale():
    p = rest_sale(amount=random_amount(digits=2))
    p.account.terminalType = 'INTERNET'
    p.paymentMethod.keyedCard.cardNumber = PaynomixCard.rand().cardnumber
    response = wn.rest(TERM_ID).sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


def test_rest_sale_without_cardholder_name():
    p = rest_sale(amount=random_amount(digits=2))
    p.account.terminalType = 'INTERNET'
    p.paymentMethod.keyedCard.cardNumber = PaynomixCard.rand().cardnumber
    p.paymentMethod.keyedCard.cardHolderName = None
    response = wn.rest(TERM_ID).sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))
