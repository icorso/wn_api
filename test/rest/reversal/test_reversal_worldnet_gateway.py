import pytest
from hamcrest import assert_that, is_not, instance_of, equal_to

from constants import Currency, Acquirer
from data.rest_requests import rest_sale, rest_reversal
from model.rest import transactionResponse
from wnclient import WNClient

wn = WNClient().vagrant.wn


@pytest.mark.parametrize('acquirer, terminal, currency', [
    (Acquirer.CASHFLOWS, '20009', Currency.EUR),
    (Acquirer.WORLDPAY, '20008', Currency.USD),
    (Acquirer.AIB, '22003', Currency.USD),
    (Acquirer.FIRSTCITIZENS, '20006', Currency.USD),
    (Acquirer.CREDORAX, '20005', Currency.USD),
    (Acquirer.ELAVONPOS, '22002', Currency.USD),
    (Acquirer.ELAVON, '22001', Currency.USD)
])
def test_reversal_ok(acquirer, terminal, currency):
    s = rest_sale()
    s.account.terminalType = 'INTERNET'
    sale_response = wn.rest(terminal).sale(currency=currency, request=s)
    assert_that(sale_response.uniqueRef, is_not(None))

    r = rest_reversal(sale_response.uniqueRef)
    r.amount.amount = 0.1
    r.account.terminalType = 'INTERNET'
    reversal_response = wn.rest(terminal).reversal(request=r)

    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))

