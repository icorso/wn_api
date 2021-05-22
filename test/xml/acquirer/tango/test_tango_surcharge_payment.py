from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.xml_requests import payment, preauth
from model.gateway import PAYMENTRESPONSE, PREAUTHRESPONSE
from utils import SurchargeAmount, random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21004'
CURRENCY = Currency.CAD
SUR_PERCENT = 4
AMOUNT = random_amount(currency=CURRENCY)


def test_tango_surcharge_payment():
    surcharge = SurchargeAmount(AMOUNT, SUR_PERCENT)

    p = payment()
    p.AMOUNT = surcharge.total_amount
    p.AUTOREADY = 'C'
    p.CURRENCY = Currency.CAD.name
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.SURCHARGE_FEE, equal_to(surcharge.surcharge))


def test_tango_surcharge_preauth():
    surcharge = SurchargeAmount(AMOUNT, SUR_PERCENT)

    p = preauth()
    p.AMOUNT = surcharge.total_amount
    p.CURRENCY = Currency.CAD.name
    response = wn.xml(terminal_id=TERM_ID).preauth(request=p)
    assert_that(response, instance_of(PREAUTHRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.SURCHARGE_FEE, equal_to(surcharge.surcharge))
