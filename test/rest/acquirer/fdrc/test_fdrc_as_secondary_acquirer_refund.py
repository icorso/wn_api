from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, contains_string

from constants import Currency, FiServCard, ApiKey, LocalMerchant
from data.rest_requests import rest_sale, rest_unreferenced_card_refund, rest_transaction_update
from model.boarding2 import FdrcTerminal
from model.boarding2 import FiServTerminal
from model.rest import transactionResponse, serviceError, paymentTypeEnum, pinDetails, dukptPinDetails, cardDetails, \
    transactionList, customerDetails, response, tipType
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
wn_boarding = WNClient().vagrant.wn.boarding()
wn_boarding2 = WNClient().vagrant.wn.boarding2()
db = WNClient().db()

BOARDING_KEY = ApiKey.BOARDING_WN_FULL
FDRC_TERM_ID = '22005'
FISERV_TERM_ID = '22006'
CURRENCY = Currency.USD
MERCHANT_ID=LocalMerchant.GOEPAY.itemid


def cbic_card_details():
    card = FiServCard.rand()
    return cardDetails(
        cardNumber=card.cardnum,
        cardType='CBIC',
        cardAccount=card.cardaccount,
        pinDetails=pinDetails(dukptPinDetails(
            pin=card.pin,
            pinKsn=card.ksn
        ))
    )


def test_enable_alternative_routing():
    key = db.get_api_key(BOARDING_KEY)
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=FISERV_TERM_ID, response_type=FiServTerminal,
                                         to_terminal=FDRC_TERM_ID, boarding2_key=key)
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=FDRC_TERM_ID, response_type=FdrcTerminal,
                                         value=paymentTypeEnum.EBT, to_terminal=FISERV_TERM_ID, boarding2_key=key)


def test_rest_reporting_list_fdrc_secondary_terminal():
    s = rest_sale()
    s.account.paymentType = paymentTypeEnum.CREDIT_DEBIT
    payment_response = wn.rest(FISERV_TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    reporting_response = wn.rest(FDRC_TERM_ID).reporting_list()
    assert_that(reporting_response, instance_of(transactionList))
    assert_that(reporting_response.transactionSummary[0].uniqueRef, equal_to(payment_response.uniqueRef))
    assert_that(reporting_response.transactionSummary[0].description, contains_string('OK'))


def test_rest_transaction_update_fdrc_secondary_terminal():
    email = fake.free_email()
    mobile_number = str(fake.random_number(10))

    sale_request = rest_sale()
    sale_request.paymentMethod.keyedCard.cardType = ''
    sale_request.account.paymentType = paymentTypeEnum.CREDIT_DEBIT
    s = wn.rest(FISERV_TERM_ID).sale(request=sale_request)
    assert_that(s, instance_of(transactionResponse))

    r = rest_transaction_update()
    r.customerDetails = customerDetails(eMail=email, mobileNumber=mobile_number)
    r.uniqueRef = s.uniqueRef
    tu_response = wn.rest(FISERV_TERM_ID).transaction_update(request=r)

    db_respnonse = wn.db(terminal_number=FDRC_TERM_ID).get_transaction(uniqueref=s.uniqueRef)
    assert_that(tu_response, instance_of(response))
    assert_that(tu_response.description, equal_to('Notifications applied and sent'))
    assert_that(db_respnonse.cardholderemail, equal_to(email))
    assert_that(db_respnonse.mobilenumber, equal_to(mobile_number))


def test_rest_tip_adjustment_fdrc_secondary_acquirer():
    amount = random_amount()
    sale_request = rest_sale(amount)
    sale_request.account.paymentType = paymentTypeEnum.CREDIT_DEBIT
    s = wn.rest(FISERV_TERM_ID).sale(request=sale_request)
    assert_that(s, instance_of(transactionResponse))

    tip_amount = random_amount()
    response = wn.rest(FISERV_TERM_ID).tip_adjustment(uniqueref=s.uniqueRef, tip_type=tipType.FIXED_AMOUNT, amount=tip_amount)
    assert_that(response.description, equal_to('Tip adjustment performed successfully.'))
    db_txn = wn.db(terminal_number=FDRC_TERM_ID).get_transaction(uniqueref=s.uniqueRef)
    db_txn_tip = wn.db(terminal_number=FDRC_TERM_ID).get_transaction_tip(uniqueref=s.uniqueRef)

    assert_that(db_txn.amount, equal_to(amount + tip_amount))
    assert_that(db_txn_tip.amount, equal_to(tip_amount))


def test_rest_fiserv_credit_sale_fdrc_credit_refund_success():
    # Credit sale to primary FiServ and secondary FDRC
    # Transaction has been refunded in FDRC terminal
    s = rest_sale()
    s.account.paymentType = paymentTypeEnum.CREDIT_DEBIT
    amount = round(s.amount.amount / 2, 2)
    payment_response = wn.rest(FISERV_TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(FDRC_TERM_ID).refund_referenced(uniqueref=payment_response.uniqueRef,
                                                              amount=amount, currency=CURRENCY,
                                                              payment_type=paymentTypeEnum.CREDIT_DEBIT)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(float(amount)))


def test_rest_fiserv_credit_sale_fiserv_credit_refund_success():
    # Credit sale request to primary FiServ and secondary FDRC
    # Transaction has been refunded in FiServ terminal
    s = rest_sale()
    s.account.paymentType = paymentTypeEnum.CREDIT_DEBIT
    amount = '{:2f}'.format(s.amount.amount / 2, 2)
    payment_response = wn.rest(FISERV_TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(FISERV_TERM_ID).refund_referenced(uniqueref=payment_response.uniqueRef,
                                                              amount=amount, currency=CURRENCY,
                                                              payment_type=paymentTypeEnum.CREDIT_DEBIT)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(float(amount)))


def test_rest_fiserv_credit_sale_fiserv_credit_full_refund_success():
    # Credit sale request to primary FiServ and secondary FDRC
    # Transaction has been voided in FiServ terminal
    s = rest_sale()
    s.account.paymentType = paymentTypeEnum.CREDIT_DEBIT
    payment_response = wn.rest(FISERV_TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(FISERV_TERM_ID).refund_referenced(uniqueref=payment_response.uniqueRef,
                                                              amount=s.amount.amount, currency=CURRENCY,
                                                              payment_type=paymentTypeEnum.CREDIT_DEBIT)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(float(s.amount.amount)))


def test_rest_fiserv_credit_sale_fiserv_refund_ebt_uniqueref_error():
    # Credit sale to primary FiServ and secondary FDRC
    # Invalid uniqueRef tag error in FiServ terminal
    s = rest_sale()
    s.account.paymentType = paymentTypeEnum.CREDIT_DEBIT
    amount = 0.12
    payment_response = wn.rest(FISERV_TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(FISERV_TERM_ID).refund_referenced(uniqueref=payment_response.uniqueRef,
                                                    amount=amount, currency=CURRENCY, payment_type=paymentTypeEnum.EBT)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.authorizedAmount, equal_to(float(s.amount.amount) - amount))


def test_rest_fdrc_credit_sale_fiserv_refund_ebt_uniqueref_error():
    # Credit sale to primary FDRC and secondary FiServ
    # Invalid uniqueRef tag error in FiServ terminal
    s = rest_sale()
    s.account.paymentType = paymentTypeEnum.CREDIT_DEBIT
    amount = round(s.amount.amount / 2, 2)
    payment_response = wn.rest(FDRC_TERM_ID).sale(request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(FISERV_TERM_ID).refund_referenced(uniqueref=payment_response.uniqueRef,
                                                              amount=amount, currency=CURRENCY,
                                                              payment_type=paymentTypeEnum.EBT)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Invalid uniqueRef tag'))


def test_rest_fiserv_normal_full_refund():
    # Normal unreferenced refund in FiServ terminal, secondary acquirer is not set
    # Cars > Allow PaymentType routing is turned off
    key = db.get_api_key(BOARDING_KEY)
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=FISERV_TERM_ID, response_type=FiServTerminal,
                                         enable=False, to_terminal=FDRC_TERM_ID, boarding2_key=key)

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
    payment_response = wn.rest(FISERV_TERM_ID).sale(request=p)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(FISERV_TERM_ID).refund_referenced(uniqueref=payment_response.uniqueRef, amount=p.amount.amount)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Alternative payment type is not supported'))


def test_rest_fiserv_unreferenced_refund_credit_success():
    # Unreferenced refund to primary FiServ and secondary FDRC
    # Unreferenced refund processed in FDRC terminal
    amount = random_amount()
    refund_request = rest_unreferenced_card_refund(amount=amount, currency=Currency.USD)
    refund_request.account.paymentType = paymentTypeEnum.CREDIT_DEBIT
    refund_response = wn.rest(FISERV_TERM_ID).refund(request=refund_request)

    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.authorizedAmount, equal_to(float(amount) * -1))


def test_rest_fiserv_credit_unreferenced_refund_not_supported_card_type():
    # Unreferenced refund in primary FiServ and secondary FDRC
    # Refund request's card doesn't supported in FDRC terminal
    wn_boarding.update_terminal_cards(terminal_number=FDRC_TERM_ID, cardtype=['visa'], silence=False)
    amount = random_amount()
    refund_request = rest_unreferenced_card_refund(cardtype='mastercard', amount=amount, currency=Currency.USD)
    refund_request.account.paymentType = paymentTypeEnum.CREDIT_DEBIT
    refund_response = wn.rest(FISERV_TERM_ID).refund(request=refund_request)

    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Invalid card type'))
    wn_boarding.update_terminal_cards(terminal_number=FDRC_TERM_ID, silence=True)


def test_rest_fiserv_unreferenced_refund_alt_payment_type_error():
    # Unreferenced refund in FiServ, secondary acquirer is not set
    # Cards > Allow PaymentType routing is turned off
    key = db.get_api_key(BOARDINGY_KEY)
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=FISERV_TERM_ID, response_type=FiServTerminal,
                                         to_terminal=FDRC_TERM_ID, enable=False, boarding2_key=key)

    amount = random_amount()
    refund_response = wn.rest(FISERV_TERM_ID).refund_unreferenced(
        amount=amount, payment_type=paymentTypeEnum.CREDIT_DEBIT)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Alternative payment type is not supported'))
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=FISERV_TERM_ID, response_type=FiServTerminal,
                                         to_terminal=FDRC_TERM_ID, enable=True, boarding2_key=key)


def test_rest_fiserv_unreferenced_refund_credit_to_deactivated_terminal():
    # FDRC terminal is deactivated
    # Unreferenced refund to primary FiServ terminal
    wn_boarding.delete_terminal(FDRC_TERM_ID)
    amount = random_amount()
    refund_request = rest_unreferenced_card_refund(amount=amount, currency=Currency.USD)
    refund_request.account.paymentType = paymentTypeEnum.CREDIT_DEBIT
    refund_response = wn.rest(FISERV_TERM_ID).refund(request=refund_request)

    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Alternative payment type is not supported'))
    wn_boarding.activate_terminal(FDRC_TERM_ID)


def test_rest_fiserv_unreferenced_refund_credit_unref_refund_not_supported():
    # FDRC terminal has 'Allow Unreferenced Refunds' turned off
    # Unreferenced refund to primary FiServ terminal
    amount = random_amount()
    refund_request = rest_unreferenced_card_refund(amount=amount, currency=Currency.USD)
    refund_request.account.paymentType = paymentTypeEnum.CREDIT_DEBIT
    refund_response = wn.rest(FISERV_TERM_ID).refund(request=refund_request)

    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Unreferenced refund should be enabled'))
