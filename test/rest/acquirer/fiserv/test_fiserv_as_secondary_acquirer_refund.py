from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency, FiServCard, LocalMerchant, ApiKey
from data.rest_requests import rest_unreferenced_card_refund, rest_sale
from model.boarding2 import FdrcTerminal
from model.boarding2 import FiServTerminal
from model.rest import transactionResponse, serviceError, paymentTypeEnum, pinDetails, dukptPinDetails, cardDetails, \
    transactionList
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
wn_boarding = WNClient().vagrant.wn.boarding()
wn_boarding2 = WNClient().vagrant.wn.boarding2()
db = WNClient().db()

FDRC_TERM_ID = '22005'
FISERV_TERM_ID = '22006'
CURRENCY = Currency.USD
BOARDING_KEY = ApiKey.BOARDING_WN_FULL
MERCHANT_ID = LocalMerchant.WN.itemid


def cbic_card_details():
    card = FiServCard.FS1
    return cardDetails(
        cardHolderName=None,
        cardNumber=card.cardnum,
        cardType='CBIC',
        cardAccount=card.cardaccount,
        expiryDate='1122',
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


def test_enable_alternative_routing():
    key = db.get_api_key(BOARDING_KEY)
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=FISERV_TERM_ID, response_type=FiServTerminal,
                                         to_terminal=FDRC_TERM_ID, enable=True, boarding2_key=key)
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=FDRC_TERM_ID, response_type=FdrcTerminal,
                                         to_terminal=FISERV_TERM_ID, value='EBT', boarding2_key=key)


def test_rest_reporting_list_fiserv_secondary_terminal():
    s = fiserv_sale()
    s.account.paymentType = paymentTypeEnum.EBT
    payment_response = wn.rest(FDRC_TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    reporting_response = wn.rest(FISERV_TERM_ID).reporting_list(order_id=s.orderId)
    assert_that(reporting_response, instance_of(transactionList))
    assert_that(reporting_response.transactionSummary[0].uniqueRef, equal_to(payment_response.uniqueRef))
    assert_that(reporting_response.transactionSummary[0].description, equal_to('Approved'))


def test_rest_fdrc_ebt_sale_fiserv_ebt_refund_success():
    # Credit sale to primary FDRC and secondary FiServ
    # Transaction has been refunded in FiServ terminal
    s = fiserv_sale()
    s.account.paymentType = paymentTypeEnum.EBT
    payment_response = wn.rest(FDRC_TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(FISERV_TERM_ID).refund_referenced(uniqueref=payment_response.uniqueRef,
                                                              amount=s.amount.amount, currency=CURRENCY,
                                                              payment_type=paymentTypeEnum.EBT)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(float(s.amount.amount)))


def test_rest_fdrc_ebt_sale_fdrc_ebt_refund_success():
    # Credit sale to primary FDRC and secondary FiServ
    # Transaction has been refunded in FDRC terminal
    s = fiserv_sale()
    s.account.paymentType = paymentTypeEnum.EBT
    payment_response = wn.rest(FDRC_TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(FDRC_TERM_ID).refund_referenced(uniqueref=payment_response.uniqueRef,
                                                              amount=s.amount.amount, currency=CURRENCY,
                                                              payment_type=paymentTypeEnum.EBT)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Invalid Terminal Id for Refund'))


def test_rest_fdrc_ebt_sale_fdrc_refund_credit_terminal_id_error():
    # Credit sale to primary FDRC and secondary FiServ
    # Invalid uniqueRef tag in FDRC terminal
    s = fiserv_sale()
    s.account.paymentType = paymentTypeEnum.EBT
    payment_response = wn.rest(FDRC_TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(FDRC_TERM_ID).refund_referenced(uniqueref=payment_response.uniqueRef,
                                                              amount=s.amount.amount, currency=CURRENCY,
                                                              payment_type=paymentTypeEnum.CREDIT_DEBIT)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Invalid Terminal Id for Refund'))


def test_rest_fdrc_unreferenced_refund_ebt_success():
    # Unreferenced refund to primary FDRC and secondary FiServ
    # Unreferenced refund processed in FiServ terminal
    amount = random_amount()
    refund_request = rest_unreferenced_card_refund(amount=amount, currency=Currency.USD)
    refund_request.account.paymentType = paymentTypeEnum.EBT
    refund_request.refundMethod.unreferenced.cardDetails = cbic_card_details()
    refund_response = wn.rest(FDRC_TERM_ID).refund(request=refund_request)

    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.authorizedAmount, equal_to(float(amount) * -1))


def test_rest_fdrc_unreferenced_refund_ebt_error():
    # Unreferenced refund to FDRC terminal and not supported secondary card type EBT
    amount = random_amount()
    refund_request = rest_unreferenced_card_refund(amount=amount, currency=Currency.USD)
    refund_request.account.paymentType = paymentTypeEnum.EBT
    refund_response = wn.rest(FDRC_TERM_ID).refund(request=refund_request)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Invalid card type'))


def test_rest_fdrc_unreferenced_refund_ebt_to_deactivated_terminal():
    # FiServ terminal is deactivated
    # Unreferenced refund to primary FDRC terminal
    wn_boarding.delete_terminal(FISERV_TERM_ID)
    amount = random_amount()
    refund_request = rest_unreferenced_card_refund(amount=amount, currency=Currency.USD)
    refund_request.account.paymentType = paymentTypeEnum.EBT
    refund_request.refundMethod.unreferenced.cardDetails = cbic_card_details()
    refund_response = wn.rest(FDRC_TERM_ID).refund(request=refund_request)

    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Alternative payment type is not supported'))

    wn_boarding.activate_terminal(FISERV_TERM_ID)


def test_rest_fdrc_unreferenced_refund_alt_payment_type_error():
    # Unreferenced refund to primary FDRC, secondary acquirer is not set
    # Cars > Allow PaymentType routing is turned off
    key = db.get_api_key(BOARDING_KEY)
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=FISERV_TERM_ID, response_type=FdrcTerminal,
                                         to_terminal=FDRC_TERM_ID, enable=False, boarding2_key=key)
    amount = random_amount()
    refund_response = wn.rest(FDRC_TERM_ID).refund_unreferenced(
        amount=amount, payment_type=paymentTypeEnum.EBT)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Alternative payment type is not supported'))
