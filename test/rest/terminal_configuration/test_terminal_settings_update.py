from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.rest_requests import rest_account
from model.rest import terminalUpdateResponse, terminalUpdate, \
    settingCreateType, terminalTax
from utils import today, random_surcharge_percent
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.go
wn_boarding = WNClient().local.go.boarding()
TERM_ID = '21001'


def terminal_tax():
    tax_name = fake.text(5)
    tax_percent = random_surcharge_percent(minorunits=5)
    return terminalTax(name=tax_name,percentage=tax_percent)


def test_rest_tax_terminal_setting_update_success():
    tax = terminal_tax()
    request = terminalUpdate(
        dateTime=today(format='%Y-%m-%dT%H:%M:%S'),
        account=rest_account(TERM_ID),
        settingCreate=settingCreateType(tax=[tax])
    )
    response = wn.rest(TERM_ID, content_type='json').update_terminal_settings(request)
    assert_that(response, instance_of(terminalUpdateResponse))
    assert_that(response.settingCreate.tax[0].name, equal_to(tax.name))
    assert_that(response.settingCreate.tax[0].percentage, equal_to(tax.percentage))
