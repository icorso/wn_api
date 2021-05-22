from hamcrest import assert_that, equal_to, not_none, instance_of

from constants import Currency
from data.rest_requests import rest_sale, rest_tip, rest_taxes
from model.rest import transactionResponse, tipType, tax
from utils import SurchargeAmount
from wnclient import WNClient

wn = WNClient().vagrant.go
wn_boarding = WNClient().vagrant.go.boarding()
TERM_ID = '21001'
CURRENCY = Currency.USD.name


def test_tax_rest_payment():
    amount = 12
    tax_percent = 20
    tax_amount = round((amount * tax_percent) / 100, 2)
    amounts = SurchargeAmount(amount=amount + tax_amount, percentage=4)
    wn_boarding.update_terminal_surcharge(TERM_ID, True, amounts.percentage)
    p = rest_sale(amount=amounts.total_amount)
    p.taxes = rest_taxes(tax(amount_member=tax_amount, currency=CURRENCY, percentage=tax_percent, name='TAX20'))
    p.bypassSurcharge = False

    response = wn.rest(terminal_id=TERM_ID, content_type='json').sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))
    assert_that(response.surcharge, not_none(), 'Surcharge tag not present')
    assert_that(response.surcharge.percentage, equal_to(amounts.percentage))
    assert_that(response.surcharge.currency, equal_to(Currency.USD.name))

    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.uniqueRef)
    assert_that("%.3f" % db_surcharge.amount, equal_to("%.3f" % amounts.surcharge))


def test_fixed_tip_rest_payment():
    amount = 8.81
    tip = 1.32
    amounts = SurchargeAmount(amount=amount + tip, percentage=4)
    wn_boarding.update_terminal_surcharge(TERM_ID, True, amounts.percentage)
    p = rest_sale(amount=amounts.total_amount)
    p.tip = rest_tip(amount=tip, tip_type=tipType.FIXED_AMOUNT)
    p.bypassSurcharge = False

    response = wn.rest(terminal_id=TERM_ID, content_type='json').sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))
    assert_that(response.surcharge, not_none(), 'Surcharge tag not present')
    assert_that(response.surcharge.percentage, equal_to(amounts.percentage))
    assert_that(response.surcharge.currency, equal_to(Currency.USD.name))

    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.uniqueRef)
    assert_that("%.3f" % db_surcharge.amount, equal_to("%.3f" % amounts.surcharge))


def test_surcharge_percentage_tip_rest_payment():
    amount = 8.81
    tip = 1.32
    amounts = SurchargeAmount(amount=amount + tip, percentage=4)
    wn_boarding.update_terminal_surcharge(TERM_ID, True, amounts.percentage)
    p = rest_sale(amount=amounts.total_amount)
    p.tip = rest_tip(amount=tip, tip_type=tipType.FIXED_AMOUNT)

    response = wn.rest(terminal_id=TERM_ID, content_type='json').sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))
    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.uniqueRef)
    assert_that("%.3f" % db_surcharge.amount, equal_to("%.3f" % amounts.surcharge))

