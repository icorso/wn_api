from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import TransactionType, TerminalType
from data.xml_requests import payment_avs, payment
from model.gateway import PAYMENTRESPONSE, CUSTOMFIELD, ERROR
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21001'
ROUTING_TERM_ID = '21999'


def test_saratoga_terminal_custom_field_payment():
    p = payment()
    p.CUSTOMFIELD = [CUSTOMFIELD(NAME='uid', valueOf_=fake.text(40))]
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_payment_routing_by_generic_custom_field():
    p = payment_avs()
    p.TERMINALTYPE = TerminalType.INTERNET
    p.TRANSACTIONTYPE = TransactionType.INTERNET
    p.CUSTOMFIELD = [CUSTOMFIELD(NAME='PRODUCT_SKU', valueOf_='PSKU1234')]
    response = wn.xml(terminal_id=ROUTING_TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_payment_no_routing_custom_field_value_do_not_match():
    p = payment_avs()
    p.TERMINALTYPE = TerminalType.INTERNET
    p.TRANSACTIONTYPE = TransactionType.INTERNET
    p.CUSTOMFIELD = [CUSTOMFIELD(NAME='PRODUCT_SKU', valueOf_=fake.text(10))]
    response = wn.xml(terminal_id=ROUTING_TERM_ID).payment(request=p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Transaction can\'t be balanced'))
