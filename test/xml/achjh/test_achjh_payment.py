from faker import Factory
from hamcrest import assert_that, instance_of

from data.xml_requests import ach_payment, ach_secure_payment
from model.gateway import PAYMENTACHRESPONSE, ACHSECUREREGISTRATIONRESPONSE
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21001'


def test_ach_payment_ok():
    p = ach_payment()
    response = wn.xml(TERM_ID).ach_payment(request=p)
    assert_that(response, instance_of(PAYMENTACHRESPONSE))


def test_ach_payment_declined():
    p = ach_payment()
    p.AMOUNT = random_amount(minorunits=4)  # invalid routing number
    response = wn.xml(TERM_ID).ach_payment(request=p)
    assert_that(response, instance_of(PAYMENTACHRESPONSE))


def test_ach_payment_returned_nsf():
    p = ach_payment()
    p.AMOUNT = random_amount(minorunits=53)  # returned nsf at report processing
    response = wn.xml(TERM_ID).ach_payment(request=p)
    assert_that(response, instance_of(PAYMENTACHRESPONSE))


def test_ach_payment_return_code_r02():
    p = ach_payment()
    p.AMOUNT = random_amount(minorunits=62)  # return code R02
    response = wn.xml(TERM_ID).ach_payment(request=p)
    assert_that(response, instance_of(PAYMENTACHRESPONSE))


def test_ach_payment_refund_returned_nsf():
    p = ach_payment()
    p.AMOUNT = random_amount(minorunits=52)  # report processing > settlement > refund > report processing
    response = wn.xml(TERM_ID).ach_payment(request=p)
    assert_that(response, instance_of(PAYMENTACHRESPONSE))


def test_ach_payment_gray_area():
    p = ach_payment()
    p.AMOUNT = random_amount(digits=2, minorunits=90)  # report processing > settlement > report processing
    response = wn.xml(TERM_ID).ach_payment(request=p)
    assert_that(response, instance_of(PAYMENTACHRESPONSE))


def test_ach_secure_card_payment():
    achjh_secure_response = wn.xml(TERM_ID).ach_secure_registration()
    assert_that(achjh_secure_response, instance_of(ACHSECUREREGISTRATIONRESPONSE))

    p = ach_secure_payment(achjh_secure_response.ACHREFERENCE, random_amount(minorunits=25))
    response = wn.xml(TERM_ID).ach_payment(request=p)
    assert_that(response, instance_of(PAYMENTACHRESPONSE))
