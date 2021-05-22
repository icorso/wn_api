import random

from faker import Factory
from hamcrest import assert_that, instance_of

from data.xml_requests import payment_avs
from model.gateway import PAYMENTRESPONSE
from wnclient import WNClient
fake = Factory.create()

wn = WNClient().local.go
TERM_ID = '21023'

base_payment = payment_avs()
base_payment.AUTOREADY = 'C'
base_payment.REGION = 'IN'
base_payment.CARDNUMBER = random.choice(['4000020951595032', '5333300989521936', '375510513169537'])
base_payment.CVV = '999'


def test_safecharge_keyed_card_payment_ok():
    p = base_payment
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
