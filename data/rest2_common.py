from faker import Factory

from model.rest2 import CardDetails, Customer, Address, KeyedPayload
from utils import today, random_card

fake = Factory.create()
today = today(format='%Y-%m-%dT%H:%M:%S')


def rest2_address():
    return Address(
        line1=fake.street_address(),
        line2=fake.secondary_address(),
        postal_code=fake.postcode(),
        city=fake.city(),
        state=fake.state(),
        country=fake.country_code()
    )


def rest2_customer():
    return Customer(
        name=fake.name(),
        notification_language='en',
        phone=fake.msisdn(),
        email=fake.free_email(),
        billing_address=rest2_address(),
        shipping_address=rest2_address()
    )


def rest2_card_details(cardtype='visa', cvv=None, source=None):
    creditcard = random_card(cardtype=cardtype) if cardtype else random_card()
    if cvv == 'random':
        cvv = creditcard.cvv
    return CardDetails(
        issue_number=fake.random_number(digits=2, fix_len=True),
        source=source,
        card_number=creditcard.cardnumber,
        expiry_date=creditcard.cardexpiry,
        cvv=cvv
    )


def rest2_keyed_payload(cardtype=None, cvv=None, source=None):
    return KeyedPayload(
            cardholder_name=fake.name(),
            payload_type='KEYED',
            account_type='CHECKING',
            card_details=rest2_card_details(cardtype, cvv, source=source)
        )
