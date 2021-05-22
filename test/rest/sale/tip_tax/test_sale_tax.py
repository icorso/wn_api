from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.rest_requests import rest_sale, rest_taxes
from model.rest import transactionResponse, tax
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.go
TERM_ID = '21001'


def test_tax_rest_payment():
    amount = 12
    tax_percent = 20
    tax_amount = round((amount * tax_percent) / 100, 2)
    t1 = tax(amount_member=tax_amount, currency='USD', percentage=tax_percent, name='VAT')
    p = rest_sale(amount=amount + tax_amount)
    taxes = rest_taxes(t1)
    p.taxes = taxes
    p.account.terminalType = 'CHP'

    response = wn.rest(terminal_id=TERM_ID, content_type='json').sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))
