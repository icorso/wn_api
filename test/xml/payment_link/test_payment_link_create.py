from faker import Factory
from hamcrest import assert_that, equal_to, instance_of

from model.gateway import CREATE_PAYMENT_LINK_RESPONSE
from wnclient import WNClient

wn = WNClient().vagrant.go
fake = Factory.create()

TERM_ID = '21001'


def test_payment_link_create_ok():
    response = wn.xml(TERM_ID).payment_link_create()
    assert_that(response, instance_of(CREATE_PAYMENT_LINK_RESPONSE))
