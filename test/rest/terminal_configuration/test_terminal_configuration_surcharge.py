from hamcrest import assert_that, instance_of, equal_to

from model.rest import configurationRequest, account, terminalConfiguration
from utils import today, random_surcharge_percent
from wnclient import WNClient

wn = WNClient().local.go
wn_boarding = WNClient().local.go.boarding()
TERM_ID = '21001'


def test_rest_surcharge_enable_success():
    surcharge_percent = random_surcharge_percent()
    wn_boarding.update_terminal_surcharge(TERM_ID, allow_surcharge=True,
                                          surcharge_percent=surcharge_percent, silence=True)
    tk = wn.rest(TERM_ID).temporary_key().key
    ac = account(terminalId=TERM_ID, terminalType='INTERNET')
    c = configurationRequest(
        account=ac,
        apiKey=tk,
        dateTime=today(format='%Y-%m-%dT%H:%M:%S')
    )
    response = wn.rest(TERM_ID).get_terminal_configuration(c)
    assert_that(response, instance_of(terminalConfiguration))
    assert_that(response.surchargePercentage, equal_to(surcharge_percent))
