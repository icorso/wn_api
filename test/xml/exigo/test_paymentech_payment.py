from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import payment_avs
from model.gateway import PAYMENTRESPONSE
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().hound.go
TERM_ID = '352020'


def paymentech_payment():
    payment_request = payment_avs()
    payment_request.AUTOREADY = 'C'
    payment_request.EMAIL = fake.free_email()
    return payment_request


def test_paymentech_keyed_payment_error():
    # got 412 error
    p = paymentech_payment()
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
