from hamcrest import assert_that, equal_to

from wnclient import WNClient

wn = WNClient()


def test_boarding_terminal_get():
    t = wn.local.go.boarding(content_type='json').get_terminal(21017)
    # assert_that(t, instance_of(terminal))


def test_boarding_get_terminal_ip_ach():
    t = wn.local.go.boarding().get_terminal(21009)
    assert_that(t.achSettings.allowAchIpTransactions, equal_to(True))
    assert_that(t.achSettings.allowAchJhTransactions, equal_to(False))


def test_boarding_get_terminal_template_ip_ach():
    # tpl = 'fiserv_term_tpl'
    tpl = 'tsys_sierra_term_tpl'
    t = wn.local.with_scheme().go.boarding().get_terminal_template(tpl)
