import pytest
from hamcrest import assert_that, instance_of, equal_to

from constants import LocalMerchant
from data.boarding.terminal import tsys_saratoga_terminal, elavon_terminal
from model.boarding import serviceError, terminal
from utils import random_surcharge_percent
from wnclient import WNClient

wn = WNClient()
TERM_ID = 21001


def test_boarding_create_terminal_surcharge_success():
    surcharge_percent = random_surcharge_percent(5)
    request = tsys_saratoga_terminal(merchant_id=LocalMerchant.GO.itemid)
    request.features.allowSurcharge = True,
    request.features.surchargePercent = surcharge_percent
    t = wn.local.go.boarding().create_terminal(request=request)
    assert_that(t, instance_of(terminal))

    get_terminal_updated = wn.boarding().get_terminal(t.terminalNumber)
    assert_that(get_terminal_updated.features.allowSurcharge, equal_to(True))
    assert_that(get_terminal_updated.features.surchargePercent, equal_to(surcharge_percent))


@pytest.mark.parametrize('percent', [0.09, -1, 4.00001])
def test_boarding_create_terminal_surcharge_wrong_percentage(percent):
    request = tsys_saratoga_terminal(merchant_id=LocalMerchant.GO.itemid)
    request.features.allowSurcharge = True
    request.features.surchargePercent = percent
    t = wn.local.go.boarding().create_terminal(request=request)

    assert_that(t, instance_of(serviceError))
    assert_that(t.validationErrors.validationError[0].message, equal_to('Value should be between 0.10000 and 4.00000'))


def test_boarding_update_terminal_surcharge_enable():
    surcharge_percent = random_surcharge_percent(5)
    t = wn.local.go.boarding().update_terminal_surcharge(terminal_number=TERM_ID, allow_surcharge=True,
                                                         surcharge_percent=surcharge_percent)
    assert_that(t, instance_of(terminal))

    get_terminal_updated = wn.boarding().get_terminal(TERM_ID)
    assert_that(get_terminal_updated.features.allowSurcharge, equal_to(True))
    assert_that(get_terminal_updated.features.surchargePercent, equal_to(surcharge_percent))


def test_boarding_update_terminal_surcharge_disable():
    t = wn.local.go.boarding().update_terminal_surcharge(terminal_number=TERM_ID)
    assert_that(t, instance_of(terminal))

    get_terminal_updated = wn.boarding().get_terminal(TERM_ID)
    assert_that(get_terminal_updated.features.allowSurcharge, equal_to(False))


@pytest.mark.parametrize('percent', [0.09, -1, 4.00001])
def test_boarding_update_terminal_surcharge_wrong_percentage(percent):
    t = wn.local.go.boarding().update_terminal_surcharge(TERM_ID, True, percent)
    assert_that(t, instance_of(serviceError))
    assert_that(t.validationErrors.validationError[0].message, equal_to('Value should be between 0.10000 and 4.00000'))


def test_boarding_terminal_create_acquirer_not_support_surcharge():
    e_terminal = elavon_terminal(merchant_id=LocalMerchant.WN.itemid)
    e_terminal.features.allowSurcharge = True
    e_terminal.features.surchargePercent = 4
    r = wn.local.wn.boarding().create_terminal(request=e_terminal)
    assert_that(r, instance_of(serviceError))
    assert_that(r.validationErrors.validationError[0].message, equal_to('Surcharge is not allowed for this acquirer'))


def test_boarding_terminal_update_surcharge_success():
    surcharge_percent = random_surcharge_percent(5)
    t = wn.local.go.boarding().get_terminal(TERM_ID, silence=False)
    t.features.allowSurcharge = True
    t.features.surchargePercent = surcharge_percent
    r = wn.local.go.boarding().update_terminal(request=t)
    assert_that(r, instance_of(terminal))
    assert_that(r.features.allowSurcharge, equal_to(True))
    assert_that(r.features.surchargePercent, equal_to(surcharge_percent))


def test_boarding_terminal_update_acquirer_not_support_surcharge():
    t = wn.local.rest.boarding().get_terminal(20001, silence=True)
    t.features.allowSurcharge = True
    r = wn.local.rest.boarding().update_terminal(request=t, silence=False)
    assert_that(r, instance_of(serviceError))
    assert_that(r.validationErrors.validationError[0].message, equal_to('Surcharge is not allowed for this acquirer'))

    another_get = wn.local.rest.boarding().get_terminal(20001, silence=False)
    assert_that(another_get.features.allowSurcharge, equal_to(False))

