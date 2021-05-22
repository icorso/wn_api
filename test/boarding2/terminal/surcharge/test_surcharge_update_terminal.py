import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import LocalMerchant, ApiKey
from model.boarding2 import Error
from model.boarding2 import Surcharge
from model.boarding2 import TsysSaratogaTerminal
from utils import random_surcharge_percent
from wnclient import WNClient

wn = WNClient().local.go.boarding2()
db = WNClient().db()
GO_KEY = ApiKey.BOARDING_GO_FULL
fake = Factory().create()
TERM_ID = '21001'


@pytest.mark.parametrize('enable, percent', [(True, random_surcharge_percent(5)),
                                             (False, None),
                                             (True, 4.00000),
                                             (True, 0.1)])
def test_update_terminal_surcharge_valid(enable, percent):
    key = db.get_api_key(GO_KEY)
    original_terminal = wn.get_terminal(LocalMerchant.GO.itemid, TERM_ID, TsysSaratogaTerminal, key)
    original_terminal.secret = 'someSecretPhrase'
    original_terminal.terminal_features.surcharge = Surcharge(enable, percent)

    # check surcharge in create_terminal response
    update_terminal_response = wn.update_terminal(LocalMerchant.GO.itemid, TERM_ID, original_terminal, TsysSaratogaTerminal, key)
    assert_that(update_terminal_response, instance_of(TsysSaratogaTerminal))
    assert_that(update_terminal_response.terminal_features.surcharge, equal_to(original_terminal.terminal_features.surcharge))

    # check surcharge in get_terminal response
    new_terminal = wn.get_terminal(LocalMerchant.GO.itemid, update_terminal_response.terminal_number, TsysSaratogaTerminal, key)
    assert_that(new_terminal.terminal_features.surcharge, equal_to(original_terminal.terminal_features.surcharge))


def test_update_terminal_surcharge_empty():
    key = db.get_api_key(GO_KEY)
    original_terminal = wn.get_terminal(LocalMerchant.GO.itemid, TERM_ID, TsysSaratogaTerminal, key)
    original_terminal.secret = 'someSecretPhrase'
    original_terminal.terminal_features.surcharge = {}

    surcharge = Surcharge(enable=False, percent=None)
    # check surcharge in create_terminal response
    create_terminal_response = wn.update_terminal(LocalMerchant.GO.itemid, TERM_ID, original_terminal, TsysSaratogaTerminal, key)
    assert_that(create_terminal_response, instance_of(TsysSaratogaTerminal))
    assert_that(create_terminal_response.terminal_features.surcharge, equal_to(surcharge))

    # check surcharge in get_terminal response
    new_terminal = wn.get_terminal(LocalMerchant.GO.itemid, create_terminal_response.terminal_number, TsysSaratogaTerminal, key)
    assert_that(new_terminal.terminal_features.surcharge, equal_to(surcharge))


@pytest.mark.parametrize('percent, error_message', [(None, 'must not be null'),
                                                    ('4.00001', 'must be less than or equal to 4.0'),
                                                    ('0.09', 'must be greater than or equal to 0.1'),
                                                    ('abc', 'Unable to deserialize value'),
                                                    ('', 'must not be null')])
def test_update_terminal_surcharge_percent_validation(percent, error_message):
    key = db.get_api_key(GO_KEY)
    original_terminal = wn.get_terminal(LocalMerchant.GO.itemid, TERM_ID, TsysSaratogaTerminal, key)
    original_terminal.secret = 'someSecretPhrase'
    original_terminal.terminal_features.surcharge = Surcharge(enable=True, percent=percent)

    update_terminal_response = wn.update_terminal(LocalMerchant.GO.itemid, TERM_ID, original_terminal, TsysSaratogaTerminal, key)
    assert_that(update_terminal_response, instance_of(Error))
    assert_that(update_terminal_response.details[0].error_message, equal_to(error_message))
    assert_that(update_terminal_response.details[0].source._property, equal_to('percent'))
