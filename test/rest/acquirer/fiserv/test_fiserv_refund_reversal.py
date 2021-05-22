from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, is_not

from constants import Currency, FiServCard, ApiKey, LocalMerchant
from data.rest_requests import rest_sale, rest_unreferenced_card_refund, rest_reversal
from model.boarding2 import FiServTerminal
from model.rest import transactionResponse, serviceError, pinDetails, dukptPinDetails, cardDetails
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
wn_boarding = WNClient().vagrant.wn.boarding()
wn_boarding2 = WNClient().vagrant.wn.boarding2()
db = WNClient().db()
BOARDING_KEY = ApiKey.BOARDING_WN_FULL
TERM_ID = '22006'
CURRENCY = Currency.USD
MERCHANT_ID = LocalMerchant.WN.itemid


def cbic_card_details():
    card = FiServCard.rand()
    return cardDetails(
        cardNumber=card.cardnum,
        cardType='CBIC',
        cardAccount=card.cardaccount,
        expiryDate='1222',
        pinDetails=pinDetails(dukptPinDetails(
            pin=card.pin,
            pinKsn=card.ksn
        ))
    )


def fiserv_sale():
    p = rest_sale()
    p.without_field('customer', 'autoReady')
    p.account.terminalType = 'CHP'
    p.account.deviceId = 'ict_220_1'
    p.deviceType = 'INGENICO_ICT220'
    p.paymentMethod.keyedCard = cbic_card_details()
    p.requestType = 'PURCHASE'
    return p


def test_disable_alternative_routing():
    key = db.get_api_key(BOARDING_KEY)
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=TERM_ID, response_type=FiServTerminal,
                                         to_terminal=TERM_ID, enable=False, boarding2_key=key)


def test_fiserv_keyed_reversal():
    sale_response = wn.rest(TERM_ID).sale(request=fiserv_sale())
    assert_that(sale_response.uniqueRef, is_not(None))
    reversal_response = wn.rest(TERM_ID).reversal(rest_reversal(sale_response.uniqueRef))

    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))
    assert_that(reversal_response.authorizedAmount, equal_to(sale_response.authorizedAmount))


def test_rest_fiserv_unreferenced_refund_success():
    amount = random_amount()
    refund_request = rest_unreferenced_card_refund(amount=amount, currency=CURRENCY)
    refund_request.refundMethod.unreferenced.cardDetails = cbic_card_details()
    refund_response = wn.rest(TERM_ID).refund(request=refund_request)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.authorizedAmount, equal_to(float(amount) * -1))


def test_rest_fiserv_partial_refund_not_supported():
    amount = 0.12
    payment_response = wn.rest(TERM_ID).sale(request=fiserv_sale())
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(TERM_ID).refund_referenced(uniqueref=payment_response.uniqueRef, amount=amount)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Invalid Terminal Id for Refund'))


def test_rest_fiserv_normal_full_refund_not_supported():
    s = fiserv_sale()
    payment_response = wn.rest(TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(TERM_ID).refund_referenced(uniqueref=payment_response.uniqueRef, amount=s.amount.amount)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Invalid Terminal Id for Refund'))
