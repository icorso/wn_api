from faker import Factory
from hamcrest import assert_that, is_not, instance_of, equal_to

from constants import PaynomixCard
from data.rest_requests import rest_reversal, rest_sale
from data.xml_requests import payment
from model.rest import transactionResponse, serviceError
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '22015'
wn = WNClient().vagrant.wn


def test_paynomix_auth_reversal():
    p = rest_sale()
    p.account.terminalType = 'INTERNET'
    p.paymentMethod.keyedCard.cardNumber = PaynomixCard.rand().cardnumber

    sale_response = wn.rest(TERM_ID).sale(p)
    assert_that(sale_response.uniqueRef, is_not(None))

    r = rest_reversal(sale_response.uniqueRef)
    r.account.terminalType = 'INTERNET'
    reversal_response = wn.rest(TERM_ID).reversal(r)

    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))
    assert_that(reversal_response.authorizedAmount, equal_to(sale_response.authorizedAmount))


def test_paynomix_sale_reversal():
    p = payment()
    p.AUTOREADY = 'C'
    p.CARDNUMBER = PaynomixCard.rand().cardnumber
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response.RESPONSECODE, equal_to('A'))

    r = rest_reversal(response.UNIQUEREF)
    r.account.terminalType = 'INTERNET'
    reversal_response = wn.rest(TERM_ID).reversal(r)

    assert_that(reversal_response, instance_of(serviceError))
    assert_that(reversal_response.message, equal_to('Transaction can not be voided: transaction status is COMPLETE'))
