from faker import Factory
from hamcrest import assert_that, instance_of

from model.gateway import TERMINAL_CONFIGURATION_RESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.go
TERM_ID = '21001'
MULTICURRENCY_TERM_ID = '21002'


def test_single_currency_terminal_configuration():
    response = wn.xml(terminal_id=TERM_ID).terminal_configuration()
    assert_that(response, instance_of(TERMINAL_CONFIGURATION_RESPONSE))


def test_multi_currency_terminal_configuration():
    response = wn.xml(terminal_id=MULTICURRENCY_TERM_ID).terminal_configuration()
    assert_that(response, instance_of(TERMINAL_CONFIGURATION_RESPONSE))
