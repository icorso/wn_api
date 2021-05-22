import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, is_not, has_length

from constants import LocalMerchant
from data.boarding.terminal import fiserv_terminal
from model.boarding import terminal, cardsType
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.goepay
tpl = 'fiserv_term_tpl'


def test_boarding_terminal_fiserv_create_and_get():
    t = fiserv_terminal(merchant_id=LocalMerchant.GOEPAY.itemid)
    t.cards = cardsType(['CBIC'])
    response = wn.boarding().create_terminal(request=t)
    assert_that(response, instance_of(terminal))

    new_terminal = WNClient().local.goepay.boarding().get_terminal(response.terminalNumber)
    assert_that(new_terminal, instance_of(terminal))
    assert_that(new_terminal.cards.card, has_length(1))


def test_boarding_terminal_fiserv_create_empty():
    t = fiserv_terminal(merchant_id=LocalMerchant.GOEPAY.itemid)
    t.cards = cardsType([])
    response = wn.boarding().create_terminal(request=t)
    assert_that(response, instance_of(terminal))

    new_terminal = WNClient().local.goepay.boarding().get_terminal(response.terminalNumber)
    assert_that(new_terminal, instance_of(terminal))
    assert_that(new_terminal.cards.card, has_length(0))


def test_boarding_terminal_fiserv_create_and_validate_cards():
    t = fiserv_terminal(merchant_id=LocalMerchant.GOEPAY.itemid)
    t.cards.add_card('VISA')
    response = wn.boarding().create_terminal(request=t)
    assert_that(response, instance_of(terminal))

    new_terminal = WNClient().local.goepay.boarding().get_terminal(response.terminalNumber)
    assert_that(new_terminal, instance_of(terminal))
    assert_that(new_terminal.cards.card, has_length(1))
    assert_that(new_terminal.cards.card[0], equal_to('CBIC'))


def test_boarding_terminal_fiserv_update_and_validate_cards():
    t = fiserv_terminal(merchant_id=LocalMerchant.GOEPAY.itemid)
    t.cards = cardsType([])
    response = wn.boarding().create_terminal(request=t)
    assert_that(response, instance_of(terminal))

    update_terminal = wn.boarding().get_terminal(response.terminalNumber)
    update_terminal.cards = cardsType(['VISA', 'CBIC'])

    update_terminal_response = wn.boarding().update_terminal(update_terminal)
    assert_that(update_terminal_response, instance_of(terminal))
    assert_that(update_terminal_response.cards.card, has_length(1))
    assert_that(update_terminal_response.cards.card[0], equal_to('CBIC'))


def test_boarding_terminal_fiserv_template_get():
    response = wn.boarding().get_terminal_template(tpl)
    assert_that(response, instance_of(terminal))


def test_boarding_terminal_fiserv_deactivate():
    response = wn.boarding().create_terminal(request=fiserv_terminal(merchant_id=LocalMerchant.GOEPAY.itemid))
    delete_terminal = wn.boarding().delete_terminal(response.terminalNumber)
    assert_that(delete_terminal.deactivationDate, is_not(None))

    activate_terminal = wn.boarding().activate_terminal(response.terminalNumber)
    assert_that(activate_terminal.deactivationDate, equal_to(None))


def test_boarding_terminal_fiserv_list_terminal():
    response = wn.boarding().list_terminal(LocalMerchant.GOEPAY.itemid)
    assert_that(response, instance_of(terminal))


def test_boarding_terminal_fiserv_create_state_validation():
    t = fiserv_terminal(merchant_id=LocalMerchant.GOEPAY.itemid)
    t.country = 'USA'
    t.additionalSettings.usState = None
    response = wn.boarding().create_terminal(request=t)
    error = response.validationErrors.validationError[0]
    assert_that(error.target, equal_to('usState'))
    assert_that(error.message, equal_to('Mandatory Field'))


@pytest.mark.parametrize('value, message', [
    (None, 'Mandatory Field'),
    ('', 'Mandatory Field'),
    ('abc123456', 'Value should not be longer than 7 characters')
])
def test_boarding_terminal_fiserv_fcsId_validation(value, message):
    t = fiserv_terminal(merchant_id=LocalMerchant.GOEPAY.itemid)
    t.bankSettings.set_fcsId(value)
    response = wn.boarding().create_terminal(request=t)
    error = response.validationErrors.validationError[0]
    assert_that(error.target, equal_to('fcsId'))
    assert_that(error.message, equal_to(message))


@pytest.mark.parametrize('field, value, message', [
    ('allowPreAuth', True, 'Value not allowed when acquirer is FiServ'),
    ('allowRecurring', True, 'Value not allowed when acquirer is FiServ'),
    ('allowEmcp', True, 'Value not allowed when acquirer is FiServ')
])
def test_boarding_terminal_fiserv_bank_settings_validation(field, value, message):
    t = fiserv_terminal(merchant_id=LocalMerchant.GOEPAY.itemid)
    setattr(t.bankSettings, field, value)
    response = WNClient().local.goepay.boarding().create_terminal(request=t)
    error = response.validationErrors.validationError[0]
    assert_that(error.target, equal_to(field))
    assert_that(error.message, equal_to(message))


def test_boarding_create_fiserv_terminal_from_template():
    t = fiserv_terminal(merchant_id=LocalMerchant.GOEPAY.itemid)
    t.templateName = tpl
    t.without_field('cards', 'integration', 'features')
    create_response = wn.boarding().create_terminal(request=t)
    assert_that(create_response, instance_of(terminal))


def test_boarding_update_fiserv_fcsId():
    fcsId = str(fake.random_number(7))
    t = fiserv_terminal(merchant_id=LocalMerchant.GOEPAY.itemid)
    t.bankSettings.set_fcsId = '1234567'
    create_response = wn.boarding().create_terminal(request=t)

    update_request = create_response
    update_request.bankSettings.set_fcsId(fcsId)
    update_response = wn.boarding().update_terminal(request=update_request)
    assert_that(update_response.bankSettings.fcsId, equal_to(fcsId))


def test_boarding_get_fiserv_terminal_template():
    t = wn.boarding().get_terminal_template(tpl)
    assert_that(t, instance_of(terminal))
