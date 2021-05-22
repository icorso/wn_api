from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import TransactionType, Currency
from data.xml_requests import payment_chp, payment, payment_avs
from model.gateway import PAYMENTRESPONSE, PREAUTHRESPONSE, CUSTOMFIELD, REFUNDRESPONSE
from utils import random_card
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22012'
VISA_DECLINED = '4716568913084649'

'''
Visa        4111111111111111
MasterCard  5431111111111111
AMEX        341111111111111
Discover    6011601160116611

CVV: 999
exp: 1025 (MMyy)

To cause a declined message, pass an amount less than 1.00.
To trigger a fatal error message, pass an invalid card number.
To simulate an AVS match, pass 888 in the address1 field, 77777 for zip.
To simulate a CVV not match, pass CVV that differs from 999.
'''


def test_nmi_keyed_card_payment_ok():
    response = wn.xml(terminal_id=TERM_ID).payment()
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_nmi_keyed_card_payment_declined_cvv():
    p = payment()
    p.CARDNUMBER = '4111111111111111'
    p.CVV = '123'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSETEXT, equal_to('CVV FAILURE'))


def test_nmi_keyed_card_avs_payment_ok():
    response = wn.xml(terminal_id=TERM_ID).payment(payment_avs())
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_nmi_recurring_payment_declined_cvv():
    p = payment_avs()
    p.CARDNUMBER = '4111111111111111'
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    p.CVV = '123'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSETEXT, equal_to('CVV FAILURE'))


def test_nmi_recurring_payment_declined_fatal():
    p = payment_avs()
    p.AUTOREADY = 'C'
    p.AMOUNT = 0.25
    p.CARDNUMBER = random_card().cardnumber
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    p.CVV = '999'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSETEXT, equal_to('Transaction was declined by processor'))


def test_nmi_recurring_payment_declined_custom_field_fatal():
    p = payment_avs()
    p.AUTOREADY = 'C'
    p.AMOUNT = 0.25
    p.CARDNUMBER = random_card().cardnumber
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    p.CUSTOMFIELD = [CUSTOMFIELD(NAME='num', valueOf_='5')]
    p.CVV = '999'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSETEXT, equal_to('Transaction was declined by processor'))


def test_nmi_chp_payment():
    response = wn.xml(TERM_ID).payment(payment_chp())
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_nmi_keyed_card_payment_void():
    p = payment()
    response = wn.xml(TERM_ID).payment()
    assert_that(response, instance_of(PAYMENTRESPONSE))

    void_response = wn.xml(TERM_ID).refund(uniqueref=response.UNIQUEREF, amount=p.AMOUNT, currency=Currency.USD)
    assert_that(void_response, instance_of(REFUNDRESPONSE))
    assert_that(void_response.RESPONSETEXT, equal_to('SUCCESS'))
