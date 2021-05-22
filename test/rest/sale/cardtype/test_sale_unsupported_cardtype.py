import pytest
from hamcrest import assert_that, equal_to, instance_of

from data.rest_requests import rest_sale
from model.rest import serviceError, transactionResponse
from wnclient import WNClient

wn = WNClient().vagrant.go
wn_boarding = WNClient().vagrant.go.boarding()
TERM_ID = '21001'


@pytest.mark.parametrize('cardtype', ['visa', 'mastercard', 'amex'])
def test_rest_sale(cardtype):
    wn_boarding.with_terminal(TERM_ID).update_terminal_cards(TERM_ID, ['jcb'], silence=True)
    response = wn.rest(TERM_ID).sale(rest_sale(cardtype=cardtype))
    assert_that(response, instance_of(serviceError))
    assert_that(response.message, equal_to('Invalid card type'))
    wn_boarding.with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)


def test_rest_unknown_card_keyed_sale():
    """should process as first available cardtype"""
    wn_boarding.with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)
    r = rest_sale()
    r.paymentMethod.keyedCard.cardNumber = '6385087787065456'
    r.paymentMethod.keyedCard.cardType = ''
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(transactionResponse))
