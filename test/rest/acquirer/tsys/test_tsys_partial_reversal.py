from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, is_

from data.rest_requests import rest_sale, rest_tip
from model.rest import tipType, transactionResponse
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21006'


def test_tsys_percentage_tip_rest_payment():
    amount = 10
    p = rest_sale(amount=amount)
    tip = rest_tip(amount=0.2, tip_type=tipType.PERCENTAGE)
    tip.percentage = 2
    p.tip = tip
    p.account.terminalType = 'CHP'

    response = wn.rest(terminal_id=TERM_ID, content_type='json').sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


def test_tsys_partial_reversal_equal_tip_amount():
    amount = 42.2
    tip_amount = amount / 2
    p = rest_sale(amount=amount)
    tip = rest_tip(amount=tip_amount, tip_type=tipType.FIXED_AMOUNT)
    p.tip = tip
    p.account.terminalType = 'CHP'

    response = wn.rest(terminal_id=TERM_ID, content_type='json').sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))

    r = wn.rest(TERM_ID).refund_referenced(uniqueref=response.uniqueRef, amount=tip_amount)
    assert_that(r, instance_of(transactionResponse))

    db_txn = wn.db(terminal_number=TERM_ID).get_transaction(uniqueref=response.uniqueRef)
    db_txn_tip = wn.db(terminal_number=TERM_ID).get_transaction_tip(uniqueref=response.uniqueRef)
    assert_that(db_txn.amount, equal_to(amount - tip_amount))
    assert_that(db_txn_tip.amount, equal_to(0))


def test_tsys_partial_reversal_less_than_tip_amount():
    amount = 42.2
    tip_amount = round(amount / 2, 2)
    reverse_amount = round(amount / 3, 2)
    p = rest_sale(amount=amount)
    tip = rest_tip(amount=tip_amount, tip_type=tipType.FIXED_AMOUNT)
    p.tip = tip
    p.account.terminalType = 'CHP'

    response = wn.rest(terminal_id=TERM_ID, content_type='json').sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))

    r = wn.rest(TERM_ID).refund_referenced(uniqueref=response.uniqueRef, amount=reverse_amount)
    assert_that(r, instance_of(transactionResponse))

    db_txn = wn.db(terminal_number=TERM_ID).get_transaction(uniqueref=response.uniqueRef)
    db_txn_tip = wn.db(terminal_number=TERM_ID).get_transaction_tip(uniqueref=response.uniqueRef)
    assert_that(db_txn.amount, equal_to(round(amount - reverse_amount, 2)))
    assert_that(db_txn_tip.amount, equal_to(round(tip_amount - reverse_amount, 2)))


def test_tsys_partial_reversal_greater_than_tip_amount():
    amount = 42.2
    tip_amount = round(amount / 2, 2)
    reverse_amount = round(amount / 1.2, 2)
    p = rest_sale(amount=amount)
    tip = rest_tip(amount=tip_amount, tip_type=tipType.FIXED_AMOUNT)
    p.tip = tip
    p.account.terminalType = 'CHP'

    response = wn.rest(terminal_id=TERM_ID, content_type='json').sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))

    r = wn.rest(TERM_ID).refund_referenced(uniqueref=response.uniqueRef, amount=reverse_amount)
    assert_that(r, instance_of(transactionResponse))

    db_txn = wn.db(terminal_number=TERM_ID).get_transaction(uniqueref=response.uniqueRef)
    db_txn_tip = wn.db(terminal_number=TERM_ID).get_transaction_tip(uniqueref=response.uniqueRef)
    assert_that(db_txn.amount, equal_to(round(amount - reverse_amount, 2)))
    assert_that(db_txn_tip.amount, equal_to(0))


def test_tsys_partial_reversal_without_tip():
    amount = random_amount()
    refund_amount = round(random_amount() / 2, 2)
    p = rest_sale(amount=amount)
    p.account.terminalType = 'CHP'

    response = wn.rest(terminal_id=TERM_ID, content_type='json').sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))

    r = wn.rest(TERM_ID).refund_referenced(uniqueref=response.uniqueRef, amount=refund_amount)
    assert_that(r, instance_of(transactionResponse))

    db_txn = wn.db(terminal_number=TERM_ID).get_transaction(uniqueref=response.uniqueRef)
    assert_that(db_txn.amount, equal_to(round(amount - refund_amount, 2)))


def test_tsys_full_refund_without_tip():
    amount = random_amount()
    p = rest_sale(amount=amount)
    p.account.terminalType = 'CHP'

    response = wn.rest(terminal_id=TERM_ID, content_type='json').sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))

    r = wn.rest(TERM_ID).refund_referenced(uniqueref=response.uniqueRef, amount=amount)
    assert_that(r, instance_of(transactionResponse))

    db_txn = wn.db(terminal_number=TERM_ID).get_transaction(uniqueref=response.uniqueRef)
    assert_that(db_txn.amount, equal_to(amount))


def test_tsys_full_refund_with_tip():
    amount = random_amount()
    tip_amount = round(amount / 2, 2)
    p = rest_sale(amount=amount)
    tip = rest_tip(amount=tip_amount, tip_type=tipType.FIXED_AMOUNT)
    p.tip = tip
    p.account.terminalType = 'CHP'

    response = wn.rest(terminal_id=TERM_ID, content_type='json').sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))

    r = wn.rest(TERM_ID).refund_referenced(uniqueref=response.uniqueRef, amount=amount)
    assert_that(r, instance_of(transactionResponse))

    db_txn = wn.db(terminal_number=TERM_ID).get_transaction(uniqueref=response.uniqueRef)
    db_txn_tip = wn.db(terminal_number=TERM_ID).get_transaction_tip(uniqueref=response.uniqueRef)
    assert_that(db_txn.amount, equal_to(amount))
    assert_that(db_txn_tip.amount, is_(tip_amount))
