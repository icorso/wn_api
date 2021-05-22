from hamcrest import assert_that, equal_to, instance_of

from data.rest_requests import rest_sale
from model.rest import tipType, transactionResponse
from utils import random_amount
from wnclient import WNClient

wn = WNClient().vagrant.go
TERM_ID = '21006'


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

    assert_that(db_txn.amount, equal_to(round((amount - refund_amount) + tip_amount, 2)))
    assert_that(db_txn_tip.amount, equal_to(tip_amount))


def test_rest_tip_adjustment_percentage():
    s = wn.rest(TERM_ID).sale(rest_sale(10))
    assert_that(s, instance_of(transactionResponse))

    r = wn.rest(TERM_ID).refund_referenced(uniqueref=s.uniqueRef, amount=3)
    assert_that(r, instance_of(transactionResponse))

    response = wn.rest(TERM_ID).tip_adjustment(uniqueref=s.uniqueRef, tip_type=tipType.PERCENTAGE, amount=3.5, percentage=50)
    assert_that(response.description, equal_to('Tip adjustment performed successfully.'))
