import pytest
from hamcrest import assert_that, equal_to, not_none, instance_of

from constants import SecureCard, Currency
from data.rest_requests import rest_sale, rest_tip, rest_emv_tlv_sale, rest_securecard_sale, rest_taxes
from model.rest import transactionResponse, tipType, serviceError, tax
from utils import random_amount, SurchargeAmount, random_surcharge_percent
from wnclient import WNClient

wn = WNClient().vagrant.go
wn_boarding = WNClient().vagrant.go.boarding()
TERM_ID = '21001'


@pytest.mark.parametrize('cardtype', [
    'amex',
    'visa',
    'mastercard',
    'discover',
    'jcb',
    'diners'
])
def test_rest_surcharge_supported_credit_cards(cardtype):
    surcharge = SurchargeAmount(random_amount(), random_surcharge_percent())
    wn_boarding.update_terminal_surcharge(TERM_ID, allow_surcharge=True, surcharge_percent=surcharge.percentage)

    s = rest_sale(cardtype=cardtype, amount=surcharge.total_amount)
    s.bypassSurcharge = False
    response = wn.rest(TERM_ID, content_type='json').sale(s)
    assert_that(response.surcharge, not_none(), 'Surcharge tag not present')
    assert_that(response.surcharge.amount, equal_to(surcharge.surcharge))
    assert_that(response.surcharge.percentage, equal_to(surcharge.percentage))
    assert_that(response.surcharge.currency, equal_to(Currency.USD.name))

    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.uniqueRef)
    assert_that("%.3f" % db_surcharge.amount, equal_to("%.3f" % surcharge.surcharge))


@pytest.mark.parametrize('card', [SecureCard.VISA_DEBIT, SecureCard.MASTERCARD_DEBIT])
def test_rest_surcharge_debit_cards_not_supported(card):
    surcharge = SurchargeAmount(random_amount(), percentage=4)
    wn_boarding.update_terminal_surcharge(TERM_ID, allow_surcharge=True, surcharge_percent=surcharge.percentage)
    s = rest_sale(amount=surcharge.total_amount)
    s.paymentMethod.keyedCard.cardNumber = card.cardnumber
    s.paymentMethod.keyedCard.cardType = card.name
    s.bypassSurcharge = False
    response = wn.rest(TERM_ID).sale(s)
    assert_that(response, instance_of(serviceError))
    assert_that(response.message, equal_to('Card type does not support surcharge'))


def test_rest_surcharge_amount_rounding_no_error():
    surcharge = SurchargeAmount(4.78, percentage=4)
    wn_boarding.update_terminal_surcharge(TERM_ID, allow_surcharge=True, surcharge_percent=surcharge.percentage)
    s = rest_sale(amount=surcharge.total_amount)

    s.bypassSurcharge = False
    response = wn.rest(TERM_ID).sale(s)
    assert_that(response.surcharge, not_none(), 'Surcharge tag not present')
    assert_that(response.surcharge.amount, equal_to(surcharge.surcharge))

    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.uniqueRef)
    assert_that("%.3f" % db_surcharge.amount, equal_to("%.3f" % surcharge.surcharge))


def test_test_surcharge_with_percentage_tip_payment():
    # terminal tip settings: tip type=percentage, tip value=1
    p = rest_sale(amount=8.00)
    tip = rest_tip(amount=0.08, tip_type=tipType.PERCENTAGE)
    tip.percentage = 1
    p.tip = tip
    response = wn.rest(terminal_id=TERM_ID).sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


def test_surcharge_emv_payment():
    surcharge = SurchargeAmount(random_amount(), random_surcharge_percent())
    wn_boarding.update_terminal_surcharge(TERM_ID, allow_surcharge=True, surcharge_percent=surcharge.percentage)

    p = rest_emv_tlv_sale(amount=surcharge.total_amount)
    response = wn.rest(terminal_id=TERM_ID, content_type='xml').sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    # bug in deserialization - uniqueRef is None in the response
    # db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.uniqueRef)
    # assert_that(db_surcharge.amount, equal_to(surcharge.surcharge))


def test_rest_surcharge_secure_card_credit():
    surcharge = SurchargeAmount(random_amount(), random_surcharge_percent())
    wn_boarding.update_terminal_surcharge(TERM_ID, allow_surcharge=True, surcharge_percent=surcharge.percentage)

    s = rest_securecard_sale(SecureCard.VISA.card_ref, amount=surcharge.total_amount)
    s.bypassSurcharge = False
    response = wn.rest(TERM_ID, content_type='json').sale(s)
    assert_that(response.surcharge, not_none(), 'Surcharge tag not present')
    assert_that(response.surcharge.percentage, equal_to(surcharge.percentage))
    assert_that(response.surcharge.currency, equal_to(Currency.USD.name))

    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.uniqueRef)
    assert_that(str(db_surcharge.amount), equal_to("%.3f" % surcharge.surcharge))


def test_rest_surcharge_secure_card_debit():
    surcharge = SurchargeAmount(random_amount(), random_surcharge_percent())
    wn_boarding.update_terminal_surcharge(TERM_ID, allow_surcharge=True, surcharge_percent=surcharge.percentage)

    s = rest_securecard_sale(SecureCard.VISA_DEBIT.card_ref, amount=surcharge.total_amount)
    s.bypassSurcharge = False
    response = wn.rest(TERM_ID).sale(s)
    assert_that(response, instance_of(serviceError))
    assert_that(response.message, equal_to('Card type does not support surcharge'))
