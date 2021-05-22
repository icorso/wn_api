import pytest
from hamcrest import assert_that, instance_of, equal_to

from model.rest import configurationRequest, account, terminalConfiguration
from utils import today, random_surcharge_percent
from wnclient import WNClient

wn = WNClient().local.go
wn_boarding = WNClient().local.go.boarding()
TERM_ID = '21001'
SURCHARGE_PERCENT = random_surcharge_percent()


@pytest.mark.parametrize('allow_surcharge,result_set', [
    (True, [True, True, True, SURCHARGE_PERCENT]),
    # (False, [False, None, None, None])
])
def test_rest_get_terminal_config_surcharge(allow_surcharge, result_set):
    # result_set = [allowSurcharges, allowSurchargesForMobile, allowSurchargesForVT, surchargePercentage]
    wn_boarding.update_terminal_surcharge(TERM_ID, allow_surcharge=allow_surcharge, surcharge_percent=result_set[3])

    tk = wn.rest(TERM_ID).temporary_key().key
    ac = account(terminalId=TERM_ID, terminalType='CHP')
    c = configurationRequest(account=ac, apiKey=tk, dateTime=today(format='%Y-%m-%dT%H:%M:%S'))

    configuration_response = wn.rest(TERM_ID).get_terminal_configuration(c)
    assert_that(configuration_response, instance_of(terminalConfiguration))
    assert_that(configuration_response.allowSurcharges, equal_to(result_set[0]))
    assert_that(configuration_response.allowSurchargesForMobile, equal_to(result_set[1]))
    assert_that(configuration_response.allowSurchargesForVT, equal_to(result_set[2]))
    assert_that(configuration_response.surchargePercentage, equal_to(result_set[3]))
