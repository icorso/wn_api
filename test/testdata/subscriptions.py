import pytest
from faker import Factory
from hamcrest import assert_that, instance_of

from constants import Currency, SecureCard
from data.xml_requests import stored_subscription, subscription
from model.gateway import ADDSTOREDSUBSCRIPTIONRESPONSE, ADDSUBSCRIPTIONRESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21001'


@pytest.mark.parametrize('merchant_ref, name, length', {
    ('ss_limited', 'Limited stored subscription', 3),
    ('ss_unlimited', 'Unlimited stored subscription', 0),
})
def test_add_stored_subscriptions(merchant_ref, name, length):
    ss = stored_subscription()
    ss.MERCHANTREF = merchant_ref
    ss.NAME = name
    ss.LENGTH = length
    response = wn.xml(TERM_ID).add_stored_subscription(request=ss, currency=Currency.USD)
    assert_that(response, instance_of(ADDSTOREDSUBSCRIPTIONRESPONSE))


@pytest.mark.parametrize('stored_sub_merchant_ref, sc_merchant_ref', {
    ('ss_limited', SecureCard.VISA.merchant_ref),
    ('ss_unlimited',  SecureCard.VISA.merchant_ref),
})
def test_add_subscription(stored_sub_merchant_ref, sc_merchant_ref):
    s = subscription(stored_subscriptionref=stored_sub_merchant_ref)
    s.SECURECARDMERCHANTREF = sc_merchant_ref
    s.TERMINALID = TERM_ID
    s.MERCHANTREF = stored_sub_merchant_ref.replace('ss', 's')
    subscription_response = wn.xml(TERM_ID).add_subscription(request=s)
    assert_that(subscription_response, instance_of(ADDSUBSCRIPTIONRESPONSE))
