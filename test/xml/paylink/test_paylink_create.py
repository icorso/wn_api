import random

from faker import Factory
from hamcrest import assert_that, equal_to, instance_of

from constants import PaylinkAuthType
from model.paylink import CREATE_RESPONSE, SEND_RESPONSE
from wnclient import WNClient

wn = WNClient().vagrant.wn
fake = Factory.create()

TERM_ID = '22001'


def test_paylink_send_ok():
    response = wn.paylink(TERM_ID).send('5160874932')
    assert_that(response, instance_of(SEND_RESPONSE))
    assert_that(response.STATUS, equal_to('OPEN'))


def test_paylink_create_preauth():
    # r =  paylink_create_request(auth_type=PaylinkAuthType.PRE_AUTH)
    # r.TERMINALID = '21001'
    # print(r.xml(is_hashable=True))
    response = wn.paylink(TERM_ID).create_paylink(paylink_create_request(auth_type=PaylinkAuthType.PRE_AUTH))
    assert_that(response, instance_of(CREATE_RESPONSE))
    assert_that(response.STATUS, equal_to('OPEN'))
