import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.rest_requests import rest_unreferenced_card_refund, rest_card_details, rest_sale, rest_referenced_refund
from model.rest import transactionResponse, serviceError
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.go
TERM_ID = '21001'
CURRENCY = Currency.USD
INSTAPAYMENT_CARD = '6385087787065456'
JCB_CARD_IN_BIN_RANGE = '3337964780608233'
JCB_CARD_NO_BIN_RANGE = '3158643479721327'


@pytest.mark.parametrize('card_number', [
    '7777770550770642',  # NCB DEBIT
    INSTAPAYMENT_CARD,  # InstaPayment
    '4556381436621737958',  # VISA not in bin range
    '4175006529566174',  # VISA in bin range
])
def test_rest_referenced_refund(card_number):
    s = rest_sale()
    s.paymentMethod.keyedCard.cardNumber = card_number
    s.paymentMethod.keyedCard.cardType = ''

    amount = round(s.amount.amount / 2, 2)
    payment_response = wn.rest(TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(TERM_ID).refund_referenced(uniqueref=payment_response.uniqueRef,
                                                         amount=amount, currency=CURRENCY)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(float(amount/-1)))


@pytest.mark.parametrize('auto_ready', ['false', None])
def test_rest_pending_sale_referenced_refund(auto_ready):
    s = rest_sale()
    s.autoReady = auto_ready

    amount = round(s.amount.amount / 2, 2)
    payment_response = wn.rest(TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund = rest_referenced_refund(uniqueref=payment_response.uniqueRef, amount=amount)
    refund.autoReady = auto_ready
    refund_response = wn.rest(TERM_ID).refund(refund, CURRENCY)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(float(amount/-1)))

    # refund_info = wn.rest(TERM_ID).reporting_list(order_id=s.orderId).transactionSummary[0]
    refund_info = wn.rest(TERM_ID).reporting_list(order_id=s.orderId).transactionSummary[0]
    assert_that(refund_info.transactionType, equal_to('REFUND'))
    assert_that(refund_info.transactionStatus, equal_to('READY'))


def test_rest_visa_unreferenced_refund():
    r = rest_unreferenced_card_refund(currency=Currency.USD)
    r.refundMethod.unreferenced.cardDetails = rest_card_details()
    refund_response = wn.rest(TERM_ID).refund(request=r, currency=Currency.USD)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.authorizedAmount, equal_to(float(r.amount.amount) * -1))


def test_rest_unknown_card_unreferenced_refund():
    r = rest_unreferenced_card_refund(currency=Currency.USD)
    cd = rest_card_details()
    cd.cardNumber = INSTAPAYMENT_CARD
    cd.cardType = ''
    r.refundMethod.unreferenced.cardDetails = cd
    refund_response = wn.rest(TERM_ID).refund(request=r, currency=Currency.USD)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Invalid card type'))


@pytest.mark.parametrize('card_type', ['JCB', ''])
def test_rest_card_type_not_supported_unreferenced_refund(card_type):
    # Refund should be processed but with the warning:
    # WARN  [default task-6] [com.merchant.rest.Payment] - JCB card type is not supported by terminal 21001
    r = rest_unreferenced_card_refund(currency=Currency.USD)
    cd = rest_card_details()
    cd.cardNumber = JCB_CARD_IN_BIN_RANGE  # JCB card type is turned OFF for the terminal, but appears in BIN range
    cd.cardType = card_type
    r.refundMethod.unreferenced.cardDetails = cd
    refund_response = wn.rest(TERM_ID).refund(request=r, currency=Currency.USD)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.authorizedAmount, equal_to(float(r.amount.amount) * -1))


def test_rest_card_type_not_supported_no_bin_range_unreferenced_refund():
    # Refund should be processed but with the warning:
    # WARN  [default task-6] [com.merchant.rest.Payment] - JCB card type is not supported by terminal 21001
    r = rest_unreferenced_card_refund(currency=Currency.USD)
    cd = rest_card_details()
    cd.cardNumber = JCB_CARD_NO_BIN_RANGE  # JCB card type is turned OFF for the terminal, but appears in BIN range
    cd.cardType = 'JCB'
    r.refundMethod.unreferenced.cardDetails = cd
    refund_response = wn.rest(TERM_ID).refund(request=r, currency=Currency.USD)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.authorizedAmount, equal_to(float(r.amount.amount) * -1))