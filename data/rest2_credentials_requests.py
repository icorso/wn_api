from faker import Factory

from data.rest2_common import rest2_card_details, rest2_customer, rest2_keyed_payload
from model.rest2 import KeyedPayload, StoreCredentialsRequest, UpdateCredentialsRequest, UpdatablePayload
from utils import today

fake = Factory.create()
today = today(format='%Y-%m-%dT%H:%M:%S')


def rest2_credentials_keyed(cardtype=None, cvv=None, custom_fields=None) -> StoreCredentialsRequest:
    request = StoreCredentialsRequest(
        operator=fake.name(),
        merchant_reference='MAPI_' + str(fake.random_number(7, False)),
        # ip_address=fake.ipv4(),  # Unable to deserialize value
        customer=rest2_customer(),
        customer_account=rest2_keyed_payload(cardtype, cvv),
        additional_data_fields=custom_fields
    )
    return request


def rest2_updatable_payload():
    return UpdatablePayload(
        source='CARD'
    )


def rest2_update_credentials(cardtype=None, cvv=None, custom_fields=None):
    request = UpdateCredentialsRequest(
        operator=fake.name(),
        customer=rest2_customer(),
        customer_account=rest2_card_details(cardtype=cardtype, cvv=cvv, source='CARD'),
        additional_data_fields=custom_fields
    )
    request.customer_account.cardholder_name = fake.name()

    return request
