from faker import Factory

from constants import Currency
from model.paylink import SEND, CUSTOMER, CREATE
from utils import today, random_amount

fake = Factory.create()


def send_paylink_request(merchantref):
    return SEND(
        MERCHANTREF=merchantref,
        ADDITIONAL_MESSAGE=fake.text(30),
        CUSTOMER=CUSTOMER(
            CUSTOMER_MERCHANTREF=str(fake.random_number(digits=8, fix_len=True)),
            NAME=fake.name(),
            EMAIL=fake.free_email(),
            PHONE=str(fake.random_number(digits=8, fix_len=True))
        ),
        DATETIME=str(today())
    )


def create_payment_link_request(merchantref, auth_type='PAYMENT', amount=None, currency=Currency.USD):
    return CREATE(
        MERCHANTREF=merchantref,
        ORDERID='XPL' + fake.random_number(digits=6, fix_len=True),
        EXPIRATION_DATE=today(days=1),
        AUTH_TYPE=auth_type,  # PAYMENT or PRE-AUTH
        DESCRIPTION=fake.text(20),
        CURRENCY=currency.code,
        TOTAL_AMOUNT=amount if amount else random_amount(currency=currency),
        DATETIME=today()
    )


