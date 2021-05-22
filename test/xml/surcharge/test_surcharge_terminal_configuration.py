from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from model.gateway import TERMINAL_CONFIGURATION_RESPONSE
from utils import random_surcharge_percent
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.go
wn_boarding = WNClient().local.go.boarding()
TERM_ID = '21001'


def test_terminal_configuration_surcharge_valid():
    surcharge_percent = random_surcharge_percent()
    wn_boarding.update_terminal_surcharge(terminal_number=TERM_ID, allow_surcharge=True, surcharge_percent=surcharge_percent)
    response = wn.xml(terminal_id=TERM_ID).terminal_configuration()
    assert_that(response, instance_of(TERMINAL_CONFIGURATION_RESPONSE))
    assert_that(response.FEATURES.SURCHARGE.ENABLED, equal_to(True))
    assert_that(response.FEATURES.SURCHARGE.SURCHARGE_PERCENT, equal_to(surcharge_percent))


def test_terminal_configuration_surcharge_disabled():
    wn_boarding.update_terminal_surcharge(terminal_number=TERM_ID, allow_surcharge=False)
    response = wn.xml(terminal_id=TERM_ID).terminal_configuration()
    assert_that(response, instance_of(TERMINAL_CONFIGURATION_RESPONSE))
    assert_that(response.FEATURES.SURCHARGE.ENABLED, equal_to(False))
    assert_that(response.FEATURES.SURCHARGE.SURCHARGE_PERCENT, equal_to(None))
