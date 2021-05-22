from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import LocalMerchant
from data.boarding.user import user
from model.boarding import user as user_
from wnclient import WNClient

wn = WNClient().local.go
TERM_ID = '21001'
fake = Factory.create()


def test_boarding_user_create():
    u = user(user_name=fake.user_name(), merchant_id=LocalMerchant.GO.itemid, terminals=[TERM_ID])
    # u.templateName = 'USER2_10-06-2020:16:54:32:135'
    u.allowChpOnVt = True
    u.allowAchjhtransactions = True
    response = wn.boarding().create_user(u, silence=False)
    assert_that(response, instance_of(user_))
    assert_that(response.allowAchjhtransactions, equal_to(True))


def test_boarding_user_update():
    response = wn.boarding().create_user(user(user_name=fake.user_name(),
                                              merchant_id=LocalMerchant.GO.itemid, terminals=[TERM_ID]))
    assert_that(response, instance_of(user_))

    update_request = response
    update_request.allowRefund = False
    update_response = wn.boarding().update_user(update_request)
    assert_that(update_response, instance_of(user_))
    assert_that(update_response.allowAchiptransactions, equal_to(False))


def test_boarding_list_user():
    request = wn.boarding(content_type='json').list_user('J68JGA4F5J')


def test_boarding_get_user():
    request = wn.boarding(content_type='xml').get_user('DS4ZFY0Z30')
    # request.allowChpOnVt = False
    # request.allowVirtualTerminal = False

    # update_response = wn.boarding().update_user(request)
    # print(getattr(update_response, 'allowChpOnVt'))
    # print(getattr(update_response, 'allowVirtualTerminal'))