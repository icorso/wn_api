from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import subscription, stored_subscription, \
    update_subscription
from model.gateway import ADDSUBSCRIPTIONRESPONSE, \
    UPDATESUBSCRIPTIONRESPONSE
from wnclient import WNClient

wn = WNClient().vagrant.go
TERM_ID = '21001'

ss = stored_subscription()


def test_update_subscription_securecard():
    stored_subscription_response = wn.xml(TERM_ID).add_stored_subscription()
    sc_response = wn.xml(TERM_ID).secure_card_registration()
    sc_response2 = wn.xml(TERM_ID).secure_card_registration()
    # add subscription
    s = subscription(stored_subscriptionref=stored_subscription_response.MERCHANTREF)
    s.SECURECARDMERCHANTREF = sc_response.MERCHANTREF
    subscription_response = wn.xml(TERM_ID).add_subscription(request=s)
    assert_that(subscription_response, instance_of(ADDSUBSCRIPTIONRESPONSE))
    # update subscription
    update_request = update_subscription(merchant_ref=subscription_response.MERCHANTREF,
                                         securecard_ref=sc_response2.MERCHANTREF)
    update_response = wn.xml(TERM_ID).update_subscription(request=update_request)
    assert_that(update_response, instance_of(UPDATESUBSCRIPTIONRESPONSE))
    assert_that(update_response.MERCHANTREF, equal_to(subscription_response.MERCHANTREF))
