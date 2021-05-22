import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency, Acquirer
from data.rest_requests import rest_unreferenced_card_refund, rest_card_details, rest_sale
from model.rest import transactionResponse, serviceError
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.wn
TERM_ID = '20001'


@pytest.mark.parametrize('acquirer, terminal, currency', [
    (Acquirer.CASHFLOWS, '20009', Currency.EUR),
    (Acquirer.WORLDPAY, '20008', Currency.USD),
    (Acquirer.AIB, '20007', Currency.USD),
    (Acquirer.CREDORAX, '20005', Currency.USD),
    (Acquirer.ELAVONPOS, '20004', Currency.USD),
    (Acquirer.ELAVON, '20001', Currency.USD)
])
def test_rest_referenced_refund(acquirer, terminal, currency):
    s = rest_sale()
    amount = round(s.amount.amount / 2, 2)
    payment_response = wn.rest(terminal).sale(currency=currency, request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(terminal).refund_referenced(uniqueref=payment_response.uniqueRef, amount=amount,
                                                          currency=currency)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(float(amount/-1)))


def test_rest_firstcitizen_full_refund():
    terminal = '20006'
    currency = Currency.USD
    s = rest_sale()
    payment_response = wn.rest(terminal).sale(currency=currency, request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(terminal).refund_referenced(uniqueref=payment_response.uniqueRef, amount=s.amount.amount,
                                                          currency=currency)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(s.amount.amount))


def test_rest_firstcitizen_partial_refund_not_supported():
    terminal = '20006'
    currency = Currency.USD
    s = rest_sale()
    amount = round(s.amount.amount / 2, 2)

    payment_response = wn.rest(terminal).sale(currency=currency, request=s)
    assert_that(payment_response, instance_of(transactionResponse))

    refund_response = wn.rest(terminal).refund_referenced(uniqueref=payment_response.uniqueRef, amount=amount,
                                                          currency=currency)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Can\'t refund transaction'))


@pytest.mark.parametrize('acquirer, terminal, currency', [
    (Acquirer.CREDORAX, '20005', Currency.USD),
    (Acquirer.ELAVON, '20001', Currency.USD)
])
def test_rest_worldnet_unreferenced_refund_supported(acquirer, terminal, currency):
    r = rest_unreferenced_card_refund(currency=currency)
    r.refundMethod.unreferenced.cardDetails = rest_card_details(cardtype='visa')
    refund_response = wn.rest(terminal).refund(request=r, currency=currency)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.authorizedAmount, equal_to(float(r.amount.amount) * -1))


@pytest.mark.parametrize('acquirer, terminal, currency', [
    (Acquirer.CASHFLOWS, '20009', Currency.EUR),
    (Acquirer.WORLDPAY, '20008', Currency.USD),
    (Acquirer.AIB, '20007', Currency.USD),
    (Acquirer.FIRSTCITIZENS, '20006', Currency.USD),
    (Acquirer.ELAVONPOS, '20004', Currency.USD),
])
def test_rest_worldnet_unreferenced_refund_not_supported(acquirer, terminal, currency):
    r = rest_unreferenced_card_refund(currency=currency)
    r.refundMethod.unreferenced.cardDetails = rest_card_details(cardtype='visa')
    refund_response = wn.rest(terminal).refund(request=r, currency=currency)
    assert_that(refund_response, instance_of(serviceError))
    assert_that(refund_response.message, equal_to('Unreferenced refund should be enabled'))
