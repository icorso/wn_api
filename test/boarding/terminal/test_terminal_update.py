import pytest
from hamcrest import assert_that, instance_of, equal_to, has_length

from constants import LocalMerchant
from data.boarding.terminal import integrapay_terminal
from model.boarding import terminal, threeDsCardsType
from wnclient import WNClient

wn = WNClient()


def test_boarding_terminal_3ds_update():
    wn = WNClient().local.wn
    t = wn.boarding().get_terminal(20007)
    t.securityFraud.threedSecure = True
    t.securityFraud.threedsMerchantId = '1'
    t.securityFraud.threedsPassword = 'password123'
    t.threeDsCards = threeDsCardsType(['MASTERCARD'])
    r = wn.boarding().update_terminal(request=t)
    assert_that(r, instance_of(terminal))
    assert_that(r.securityFraud.threedSecure, equal_to(True))
    assert_that(r.threeDsCards.threeDsCard, has_length(1))


def test_boarding_terminal_threatmetrix_update():
    t = wn.local.go.boarding().get_terminal(21001)
    t.securityFraud.threatMetrixEnabled = True
    t.securityFraud.threatMetrixOrgId = '1008xb81'
    t.securityFraud.threatMetrixApiKey = 'w2v4h5yb1c2hrbaj'
    t.securityFraud.threatMetrixPolicyName = 'review_all'
    t.securityFraud.threatMetrixRejectOnError = False
    t.securityFraud.threatMetrixRiskScoreThreshold = None
    r = wn.local.go.boarding().update_terminal(request=t)
    assert_that(r, instance_of(terminal))
    assert_that(r.securityFraud.threatMetrixEnabled, equal_to(True))


def test_boarding_terminal_ip_ach_create():
    t = integrapay_terminal(merchant_id=LocalMerchant.GO.itemid)
    r = wn.local.go.boarding().create_terminal(t)
    assert_that(r, instance_of(terminal))


@pytest.mark.parametrize('allow_intergapay', [True, False])
def test_boarding_terminal_ip_ach_update(allow_intergapay):
    t = wn.local.go.boarding().get_terminal(48006)
    t.achSettings.allowAchIpTransactions = allow_intergapay

    r = wn.local.go.boarding().update_terminal(request=t)
    assert_that(r, instance_of(terminal))
    assert_that(r.achSettings.allowAchIpTransactions, equal_to(allow_intergapay))


def test_boarding_get_terminal_ip_ach():
    t = wn.local.go.boarding().get_terminal(48006)
    assert_that(t.achSettings.allowAchIpTransactions, equal_to(True))
    assert_that(t.achSettings.allowAchJhTransactions, equal_to(False))


def test_boarding_get_terminal_template_ip_ach():
    tpl = 'integrap_term_tpl'
    t = wn.local.go.boarding().get_terminal_template(tpl)


def test_boarding_terminal_currency_update():
    wn = WNClient().local.go
    t = wn.boarding().get_terminal(21024, silence=True)
    t.bankSettings.currency = 'USD'
    r = wn.boarding().update_terminal(request=t)
