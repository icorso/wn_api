from faker import Factory
from hamcrest import assert_that, instance_of

from data.xml_requests import securecard_registration, payment_securecard
from model.gateway import SECURECARDREGISTRATIONRESPONSE, PAYMENTRESPONSE
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.go
TERM_ID = '21009'


def test_integrapay_secure_card_registration_success():
    sc = securecard_registration()
    response = wn.local.go.xml(TERM_ID).payment(sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


def test_integrapay_secure_card_payment_success():
    sc = securecard_registration()
    response = wn.local.go.xml(TERM_ID).payment(sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))

    p = payment_securecard(cardreference=response.CARDREFERENCE,
                           amount=fake.pydecimal(1, 2, True))
    p.AUTOREADY='C'
    p.CVV = '999'
    response = wn.local.go.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
