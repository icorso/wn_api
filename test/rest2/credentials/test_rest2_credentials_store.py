import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey
from data.rest2_credentials_requests import rest2_credentials_keyed
from model.rest2 import CustomField
from model.rest2.secure_credentials import SecureCredentials
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '22001'
KEY = db.get_api_key(ApiKey.API_WN_FULL)
wn = WNClient().vagrant.wn.rest2(terminal_id=TERM_ID)


@pytest.mark.parametrize('cardtype', ['VISA', 'MASTERCARD', 'AMEX', 'DINERS', 'MAESTRO', 'JCB'])
def test_credentials_store_different_card_types(cardtype):
    response = wn.credentials_store(request=rest2_credentials_keyed(cardtype=cardtype), api2_key=KEY, silence=False)
    assert_that(response, instance_of(SecureCredentials))


def test_credentials_store_custom_field():
    scf = CustomField(name='SecureCardField', value=str(fake.random_number()))
    response = wn.credentials_store(request=rest2_credentials_keyed(cardtype='visa', custom_fields=[scf]),
                                    api2_key=KEY, silence=False)
    assert_that(response, instance_of(SecureCredentials))
    assert_that(list(filter(lambda cf: (cf.name == 'SecureCardField'), response.additional_data_fields))[0],
                equal_to(scf))
