from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Country, TransactionType, Currency
from data.xml_requests import securecard_registration, payment_securecard, payment_avs
from model.gateway import PAYMENTRESPONSE, SECURECARDREGISTRATIONRESPONSE, REFUNDRESPONSE, CUSTOMFIELD
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().vagrant.go
# TERM_ID = '352011'
TERM_ID = '21008'
# TERM_ID = '352013'

"""
Specification:  http://developers.payulatam.com/en/sdk/payments.html
Auth server:    https://sandbox.api.payulatam.com/payments-api/4.0/service.cgi
        | Bank Account ID
--------------------------
Mexico  | 512324
Panama  | 512326
Peru    | 512323
"""


def payulatam_payment():
    payment_request = payment_avs()
    payment_request.CARDHOLDERNAME = 'APPROVED'
    payment_request.CARDEXPIRY = '0122'
    payment_request.AUTOREADY = 'C'
    payment_request.EMAIL = fake.free_email()
    payment_request.REGION = 'AB'
    payment_request.COUNTRY = Country.Panama.short_code
    return payment_request


def test_payulatam_securecard_payment_declined():
    securecard = securecard_registration()

    sc_response = wn.xml(TERM_ID).secure_card_registration(securecard)
    assert_that(sc_response, instance_of(SECURECARDREGISTRATIONRESPONSE))

    p = payment_securecard(cardreference=sc_response.CARDREFERENCE)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_payulatam_keyed_payment_ok():
    response = wn.xml(TERM_ID).payment(payulatam_payment())
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


def test_payulatam_recurring_payment_rejected():
    p = payulatam_payment()
    p.AUTOREADY = 'C'
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    p.CARDHOLDERNAME = 'REJECTED'
    p.CUSTOMFIELD = [CUSTOMFIELD(NAME='USERAGENT', valueOf_=fake.user_agent()[:100])]
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))


def test_payulatam_partial_refund():
    p = payulatam_payment()
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    amount = round(p.AMOUNT / 2)
    refund_response = wn.xml(TERM_ID).refund(uniqueref, amount, Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_payulatam_full_refund():
    p = payulatam_payment()
    payment_response = wn.xml(TERM_ID).payment(p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))

    uniqueref = payment_response.UNIQUEREF
    refund_response = wn.xml(TERM_ID).refund(uniqueref, p.AMOUNT, Currency.USD)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))
