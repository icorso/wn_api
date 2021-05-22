import pytest
from hamcrest import assert_that, is_not, instance_of, equal_to

from constants import Currency, Acquirer
from data.rest_requests import rest_sale, rest_reversal
from model.rest import transactionResponse
from wnclient import WNClient

wn = WNClient().vagrant.go


@pytest.mark.parametrize('acquirer, terminal, currency', [
    (Acquirer.TSYS_SARATOGA, '21001', Currency.USD),
    (Acquirer.NMI, '21003', Currency.USD),
    (Acquirer.TSYS, '21006', Currency.USD)
])
def test_reversal_ok(acquirer, terminal, currency):
    s = rest_sale()
    sale_response = wn.rest(terminal).sale(currency=currency, request=s)
    assert_that(sale_response.uniqueRef, is_not(None))

    r = rest_reversal(sale_response.uniqueRef)
    reversal_response = wn.rest(terminal).reversal(request=r)

    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))
    assert_that(reversal_response.authorizedAmount, equal_to(float(s.amount.amount)))

