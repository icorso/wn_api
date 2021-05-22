import random

import pytest
from faker import Factory
from hamcrest import equal_to, assert_that, instance_of, is_, not_none, has_length

from constants import Currency
from data.xml_requests import payment, payment_avs, unreferenced_refund, payment_securecard, securecard_registration, \
    subscription, payment_subscription
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE, REFUND, SECURECARDREGISTRATIONRESPONSE, \
    ADDSUBSCRIPTIONRESPONSE, SUBSCRIPTIONPAYMENTRESPONSE
from utils import today, random_amount
from wnclient import WNClient
fake = Factory.create()

wn = WNClient().local.go
wn_boarding = WNClient().local.go.boarding()
TERM_ID = '21024'
TERM_ID_MC = '21016'
TERM_ID_CAD = '21017'

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

USD 71.43 - pick up card
---
* Also works for 3D Secure
** Allows for the capture of additional Level 2 Data
'''

base_payment = payment_avs()
base_payment.AUTOREADY = 'C'
base_payment.AMOUNT = random_amount(digits=2, minorunits=0)
base_payment.CARDNUMBER = random.choice(['4000000000000002', '4159288888888882'])
base_payment.CVV = '999'

converge_secure_cards = {
    'visa': '4000000000000002',
    'mastercard': '5121212121212124',
    'discover': '6011000000000004',
    'diners': '3811112222222222',
    'jcb': '3566664444444445'
}


@pytest.mark.parametrize('validate_sc', [True, False])
def test_elavon_converge_secure_card_registration(validate_sc):
    get_terminal_response = wn_boarding.get_terminal(TERM_ID)
    get_terminal_response.features.validateScSecurity = validate_sc
    boarding_response = wn_boarding.update_terminal(get_terminal_response)
    assert_that(boarding_response.features.validateScSecurity, equal_to(validate_sc))

    securecard_response = wn.xml(TERM_ID).secure_card_registration()
    assert_that(securecard_response, instance_of(SECURECARDREGISTRATIONRESPONSE))
    assert_that(securecard_response.CARDREFERENCE, has_length(16))


def test_elavon_converge_secure_card_payment():
    get_terminal_response = wn_boarding.get_terminal(TERM_ID)
    get_terminal_response.features.validateScSecurity = False
    wn_boarding.update_terminal(get_terminal_response)

    card_type, card_number = random.choice(list(converge_secure_cards.items()))
    sc_request = securecard_registration(card_type)
    sc_request.CARDNUMBER = card_number
    sc_response = wn.xml(TERM_ID).secure_card_registration(sc_request)

    payment_response = wn.xml(TERM_ID).payment(payment_securecard(amount=random_amount(2, 0),
                                                                  cardreference=sc_response.CARDREFERENCE))
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))
    assert_that(payment_response.RESPONSECODE, equal_to('A'))


def test_elavon_converge_subscription_payment():
    get_terminal_response = wn_boarding.get_terminal(TERM_ID)
    get_terminal_response.features.validateScSecurity = False
    wn_boarding.update_terminal(get_terminal_response)

    card_type, card_number = random.choice(list(converge_secure_cards.items()))
    sc_request = securecard_registration(card_type)
    sc_request.CARDNUMBER = card_number
    sc_response = wn.xml(TERM_ID).secure_card_registration(sc_request)
    stored_subscription_response = wn.xml(TERM_ID).add_stored_subscription()

    s = subscription(stored_subscriptionref=stored_subscription_response.MERCHANTREF)
    s.SECURECARDMERCHANTREF = sc_response.MERCHANTREF
    subscription_response = wn.xml(TERM_ID).add_subscription(request=s)
    assert_that(subscription_response, instance_of(ADDSUBSCRIPTIONRESPONSE))

    sp = payment_subscription(subscription_response.MERCHANTREF)
    subscription_payment_response = wn.xml(TERM_ID).subscription_payment(request=sp, currency=Currency.USD)
    assert_that(subscription_payment_response, instance_of(SUBSCRIPTIONPAYMENTRESPONSE))