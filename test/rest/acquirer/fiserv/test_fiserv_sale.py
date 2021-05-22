import random

import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import FiServCard
from data.rest_requests import rest_sale, rest_reversal, rest_voucher, rest_unreferenced_card_refund, rest_emv_tlv_sale
from model.rest import dukptPinDetails, pinDetails, transactionResponse, refundMethod, refundUnreferenced, voucher, \
    serviceError
from wnclient import WNClient

wn = WNClient().vagrant.wn
TERM_ID = '22008'
fake = Factory.create()


def fiserv_keyed_payment():
    card = FiServCard.rand()

    p = rest_sale()
    p.without_field('customer', 'autoReady')
    p.account.terminalType = 'CHP'
    p.account.deviceId = 'ict_220_1'
    p.deviceType = 'INGENICO_ICT220'
    p.paymentMethod.keyedCard.cardHolderName = None
    p.paymentMethod.keyedCard.cardType = 'CBIC'
    p.paymentMethod.keyedCard.cardNumber = card.cardnum
    p.paymentMethod.keyedCard.cardAccount = card.cardaccount
    p.paymentMethod.keyedCard.cvv = None
    p.paymentMethod.keyedCard.pinDetails = pinDetails(dukptPinDetails(
        pin=card.pin,
        pinKsn=card.ksn
    ))
    p.requestType = 'PURCHASE'
    return p


def test_fiserv_sale_keyed_approved():
    response = wn.rest(TERM_ID).sale(fiserv_keyed_payment())
    assert_that(response, instance_of(transactionResponse))


def test_fiserv_sale_emv_not_support():
    response = wn.rest(TERM_ID).sale(rest_emv_tlv_sale())
    assert_that(response, instance_of(serviceError))
    assert_that(response.message, equal_to('Terminal does not support EMV Requests'))


@pytest.mark.parametrize('amount', [1000.43])
def test_fiserv_sale_keyed_declined(amount):
    payment = fiserv_keyed_payment()
    payment.amount.amount = amount
    response = wn.rest(TERM_ID).sale(payment)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('D'))


def test_fiserv_voucher_sale():
    response = wn.rest(TERM_ID).sale(rest_voucher(FiServCard.FS1))
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


def test_fiserv_voucher_refund():
    request = rest_unreferenced_card_refund()
    request.deviceType = 'INGENICO_ICT220'
    request.account.deviceId = 'ict_220_1'
    request.refundMethod = refundMethod(
            unreferenced=refundUnreferenced(
                voucher=voucher(
                    cardAccount=FiServCard.FS1.cardaccount,
                    cardNumber=FiServCard.FS1.cardnum,
                    cardType='CBIC',
                    voucherApprovalCode='123456',
                    voucherNumber='123456789012345'
                ),
                reason=fake.text(20),
                orderId='REST_' + str(fake.random_number(7, False))

        )
    )
    response = wn.rest(TERM_ID).refund(request)
    assert_that(response, instance_of(transactionResponse))


def test_fiserv_reversal_ok():
    sale_response = wn.rest(TERM_ID).sale(fiserv_keyed_payment())
    assert_that(sale_response, instance_of(transactionResponse))

    reversal_request = rest_reversal(uniqueref=sale_response.uniqueRef)
    reversal_request.account.terminalType = 'CHP'
    reversal_response = wn.rest(TERM_ID).reversal(reversal_request)
    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))


def test_fiserv_full_refund_ok():
    sale_request = fiserv_keyed_payment()
    sale_response = wn.rest(TERM_ID).sale(sale_request)
    assert_that(sale_response, instance_of(transactionResponse))

    refund_response = wn.rest(TERM_ID).refund_referenced(sale_response.uniqueRef, sale_request.amount.amount)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
