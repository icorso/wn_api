import random

import pytest
from faker import Factory
from hamcrest import equal_to, assert_that, instance_of

from constants import Currency, TransactionType, TerminalType
from data.xml_requests import payment, payment_avs, unreferenced_refund
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE, PAYMENT, \
    ERROR
from utils import today, random_amount
from wnclient import WNClient
fake = Factory.create()

wn = WNClient().local.go
wn_boarding = WNClient().local.go.boarding()
TERM_ID = '21026'
TERM_ID_MC = '21016'
TERM_ID_EUR = '21017'

'''
Valid cards:
Visa* - 4000000000000002
Visa Corporate** - 4159288888888882
MasterCard - 5121212121212124
Discover - 6011000000000004
Diners Club - 36111111111111 (14 digit), 3811112222222222 (16 digit)
American Express - 370000000000002
JCB - 3566664444444445
Electronic Gift Card (EGC) - 6032610007325520
Foreign Currency Cards	4032769999999992 (CAD), 5432675555555552 (EUR)

USD 1.43 - pick up card
USD 1.54 - expired card
---
* Also works for 3D Secure
** Allows for the capture of additional Level 2 Data
'''

base_payment = payment()
base_payment.AUTOREADY = 'C'
base_payment.AMOUNT = random_amount(digits=2, minorunits=0)
base_payment.CARDNUMBER = random.choice(['4000000000000002', '4159288888888882'])
base_payment.without_field('CVV')
# base_payment.CVV = '999'

avs_payment = payment_avs()
avs_payment.AUTOREADY = 'C'
avs_payment.AMOUNT = random_amount(digits=2, minorunits=0)
avs_payment.CARDNUMBER = random.choice(['4000000000000002', '4159288888888882'])
avs_payment.CVV = '999'


def test_elavon_converge_keyed_payment():
    response = wn.xml(TERM_ID).payment(base_payment)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


@pytest.mark.parametrize('amount, response_text', [
    (random_amount(1, 55), 'Invalid PIN'),
    (random_amount(1, 72), 'Declined'),  # Response code: 'DECLINED CVV2'  mapped to: 'D'
])
def test_elavon_converge_visa_declined_response(amount, response_text):
    p = base_payment
    p.AMOUNT = amount
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))
    assert_that(response.RESPONSETEXT, equal_to(response_text))


def test_elavon_converge_eur_payment():
    p = base_payment
    p.CURRENCY = 'EUR'
    p.CARDNUMBER = '5432675555555552'
    response = wn.xml(TERM_ID_EUR).payment(base_payment)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_elavon_converge_large_description_payment():
    p = base_payment
    p.DESCRIPTION = fake.text()[:300] + fake.text()[:300]
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_elavon_converge_chp_payment():
    p = PAYMENT(
        ORDERID='XML_' + str(fake.random_number(7, False)),
        AMOUNT=random_amount(digits=2, minorunits=0),
        DATETIME=str(today()),
        TRACKDATA=';4000000000000002=%s10114991888?' % (fake.credit_card_expire(date_format='%y%m')),
        CARDTYPE='VISA',
        CARDHOLDERNAME=fake.name(),
        CURRENCY='USD',
        TERMINALTYPE=TerminalType.CHP,
        TRANSACTIONTYPE=TransactionType.CHP,
        AUTOREADY='C',
        DESCRIPTION=fake.text(30)
    )
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    # <ssl_cvv2cvc2_indicator>9</ssl_cvv2cvc2_indicator>


def test_elavon_converge_recurring_payment():
    # we don't support recurring
    p = base_payment
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_elavon_converge_payment_without_cvv():
    p = base_payment
    p.CVV = None

    get_terminal_response = wn_boarding.get_terminal(TERM_ID)
    get_terminal_response.features.validateScSecurity = False
    wn_boarding.update_terminal(get_terminal_response)

    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    # <ssl_cvv2cvc2_indicator>1</ssl_cvv2cvc2_indicator>


def test_elavon_converge_avs_payment():
    response = wn.xml(TERM_ID).payment(avs_payment)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    # Used only ADDRESS1 and POSTCODE fields
    #  <ssl_avs_address>66947 Scott Vista Apt. 215</ssl_avs_address><ssl_avs_zip>83543</ssl_avs_zip>


def test_elavon_converge_partial_refund():
    response = wn.xml(TERM_ID).payment(base_payment)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    refund_amount = base_payment.AMOUNT / 2
    refund_response = wn.xml(TERM_ID).refund(response.UNIQUEREF, refund_amount, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_elavon_converge_full_refund():
    response = wn.xml(TERM_ID).payment(base_payment)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    refund_response = wn.xml(TERM_ID).refund(response.UNIQUEREF, base_payment.AMOUNT, currency=Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_elavon_converge_unreferenced_refund():
    p = unreferenced_refund(amount=1.00)

    refund_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(refund_response, instance_of(ERROR))
    assert_that(refund_response.ERRORSTRING, equal_to('UNREFERENCED REFUNDS NOT ALLOWED'))


def test_elavon_converge_mc_terminal_keyed_payment():
    response = wn.xml(TERM_ID_MC).payment(base_payment, is_multicurrency=True)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    # only MC terminal request contain <ssl_transaction_currency>USD</ssl_transaction_currency> tag
    # but there is no MC terminal available on acquirer's side
