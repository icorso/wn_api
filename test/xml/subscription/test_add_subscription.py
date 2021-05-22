from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.xml_requests import subscription, payment_subscription, securecard_registration, stored_subscription
from model.gateway import ADDSTOREDSUBSCRIPTIONRESPONSE, DELETESTOREDSUBSCRIPTIONRESPONSE, ADDSUBSCRIPTIONRESPONSE, \
    SUBSCRIPTIONPAYMENTRESPONSE
from utils import random_text
from wnclient import WNClient

wn = WNClient().vagrant.go
TERM_ID = '21001'

ss = stored_subscription()


def test_add_stored_subscription_limited():
    ss.MERCHANTREF = 'ss_limited_%s_%s' % (TERM_ID, random_text())
    ss.NAME = 'Limited stored subscription'
    ss.LENGTH = 3
    response = wn.xml(TERM_ID).add_stored_subscription(request=ss)
    assert_that(response, instance_of(ADDSTOREDSUBSCRIPTIONRESPONSE))


def test_add_stored_subscription_unlimited():
    ss.NAME = 'Unlimited stored subscription'
    ss.MERCHANTREF = 'ss_unlimited_%s_%s' % (TERM_ID, random_text())
    ss.LENGTH = 0

    response = wn.xml(TERM_ID).add_stored_subscription(request=ss)
    assert_that(response, instance_of(ADDSTOREDSUBSCRIPTIONRESPONSE))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


def test_add_subscription_existing_securecard():
    stored_subscription_response = wn.xml(TERM_ID).add_stored_subscription()
    sc_response = wn.xml(TERM_ID).secure_card_registration()

    s = subscription(stored_subscriptionref=stored_subscription_response.MERCHANTREF)
    s.SECURECARDMERCHANTREF = sc_response.MERCHANTREF
    subscription_response = wn.xml(TERM_ID).add_subscription(request=s)
    assert_that(subscription_response, instance_of(ADDSUBSCRIPTIONRESPONSE))

    sp = payment_subscription(subscription_response.MERCHANTREF)
    subscription_payment_response = wn.xml(TERM_ID).subscription_payment(request=sp, currency=Currency.CAD)
    assert_that(subscription_payment_response, instance_of(SUBSCRIPTIONPAYMENTRESPONSE))


def test_subscription_payment_of_non_validated_shared_securecard():
    # pilot feature "#23345 - Subscription Payments with non validated Secure Cards when CVV Mandatory is enabled"
    # is turned ON
    # merchant_go has shared securecards (General Setup > Share all Secure Cards)
    # terminal 21003 Features > Validate Secure Cards is off
    # terminal 21004 Features > Validate Secure Cards and CVV mandatory is on

    A = '21003'
    B = '21004'
    stored_subscription_response = wn.xml(B).add_stored_subscription()
    sc = securecard_registration()
    sc.without_field('CVV')
    sc_response = wn.xml(A).secure_card_registration(sc)

    s = subscription(stored_subscriptionref=stored_subscription_response.MERCHANTREF)
    s.CARDREFERENCE = sc_response.CARDREFERENCE
    subscription_response = wn.xml(B).add_subscription(request=s)
    assert_that(subscription_response, instance_of(ADDSUBSCRIPTIONRESPONSE))

    sp = payment_subscription(subscription_response.MERCHANTREF)
    subscription_payment_response = wn.xml(B).subscription_payment(request=sp, currency=Currency.USD)
    assert_that(subscription_payment_response, instance_of(SUBSCRIPTIONPAYMENTRESPONSE))


def test_remove_stored_subscription():
    response = wn.xml(TERM_ID).add_stored_subscription(stored_subscription())
    assert_that(response, instance_of(ADDSTOREDSUBSCRIPTIONRESPONSE))

    delete_stored_subscription_response = wn.xml(TERM_ID).delete_stored_subscription(response.MERCHANTREF)
    assert_that(delete_stored_subscription_response, instance_of(DELETESTOREDSUBSCRIPTIONRESPONSE))
    assert_that(delete_stored_subscription_response.generate_hash(),
                equal_to(delete_stored_subscription_response.HASH))
