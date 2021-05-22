import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, is_not

from constants import Currency, PosDevice, EmvTlv, ApiKey, LocalMerchant, PaynomixCard
from data.rest_requests import rest_unreferenced_card_refund, rest_emv_tlv_sale, rest_referenced_refund, rest_reversal, \
    rest_sale
from model.boarding2 import FdrcTerminal
from model.rest import transactionResponse
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '22015'
CURRENCY = Currency.USD

wn = WNClient().vagrant.wn.rest(TERM_ID)


def test_referenced_partial_refund():
    refund_amount = 0.52
    s = rest_sale(amount=random_amount(digits=2))
    s.paymentMethod.keyedCard.cardNumber = PaynomixCard.rand().cardnumber
    sale_response = wn.sale(request=s)

    assert_that(sale_response.uniqueRef, is_not(None))
    refund_response = wn.refund_referenced(uniqueref=sale_response.uniqueRef, amount=refund_amount)

    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(round(sale_response.authorizedAmount - refund_amount, 2)))


def test_unreferenced_refund():
    amount = random_amount()
    refund_response = wn.refund_unreferenced(amount=amount)

    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(amount * -1))
