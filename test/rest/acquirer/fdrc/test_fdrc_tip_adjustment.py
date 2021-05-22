from hamcrest import assert_that, equal_to, instance_of

from constants import Currency
from data.rest_requests import rest_sale
from model.rest import tipType, transactionResponse
from utils import random_amount
from wnclient import WNClient

wn = WNClient().vagrant.wn
TERM_ID = '22005'


def test_rest_tip_adjustment_fixed_amount():
    amount = random_amount()
    refund_amount = round(amount / 2, 2)
    tip_amount = random_amount()
    s = wn.rest(TERM_ID).sale(rest_sale(amount))
    assert_that(s, instance_of(transactionResponse))

    r = wn.rest(TERM_ID).refund_referenced(uniqueref=s.uniqueRef, amount=refund_amount)
    assert_that(r, instance_of(transactionResponse))

    response = wn.rest(TERM_ID).tip_adjustment(uniqueref=s.uniqueRef, tip_type=tipType.FIXED_AMOUNT, amount=tip_amount)
    assert_that(response.description, equal_to('Tip adjustment performed successfully.'))
    db_txn = wn.db(terminal_number=TERM_ID).get_transaction(uniqueref=s.uniqueRef)
    db_txn_tip = wn.db(terminal_number=TERM_ID).get_transaction_tip(uniqueref=s.uniqueRef)

    assert_that(db_txn.amount, equal_to((amount - refund_amount) + tip_amount))
    assert_that(db_txn_tip.amount, equal_to(tip_amount))


def test_rest_tip_adjustment_percentage():
    s = wn.rest(TERM_ID).sale(rest_sale(10))
    assert_that(s, instance_of(transactionResponse))

    r = wn.rest(TERM_ID).refund_referenced(uniqueref=s.uniqueRef, amount=3)
    assert_that(r, instance_of(transactionResponse))

    response = wn.rest(TERM_ID).tip_adjustment(uniqueref=s.uniqueRef, tip_type=tipType.PERCENTAGE, amount=3.5, percentage=50)
    assert_that(response.description, equal_to('Tip adjustment performed successfully.'))


def test_rest_tip_adjustment_fdrc_amex():
    # Partial reversal not supported for AMEX card, a refund should be created
    currency = Currency.USD
    refund_amount = 3
    s = wn.rest(TERM_ID).sale(rest_sale(10, cardtype='AMEX'))
    assert_that(s, instance_of(transactionResponse))

    response = wn.rest(TERM_ID).tip_adjustment(uniqueref=s.uniqueRef, tip_type=tipType.FIXED_AMOUNT, amount=5)
    assert_that(response.description, equal_to('Tip adjustment performed successfully.'))

    r = wn.rest(TERM_ID).refund_referenced(uniqueref=s.uniqueRef, currency=currency, amount=refund_amount)
    assert_that(r, instance_of(transactionResponse))
    assert_that(r.code, equal_to('A'))
    assert_that(r.authorizedAmount, equal_to(refund_amount * -1))
