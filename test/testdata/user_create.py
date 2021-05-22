from constants import LocalMerchant
from data.boarding.user import user
from wnclient import WNClient

wn_client = WNClient().vagrant


def test_boarding_wn_user_create():
    u = user(user_name='user', merchant_id=LocalMerchant.WN.itemid, terminals=['22001'])
    wn_client.wn.boarding().create_user(u, silence=True)


def test_boarding_go_user_create():
    u = user(user_name='user', merchant_id=LocalMerchant.WN.itemid, terminals=['21001'])
    wn_client.go.boarding().create_user(u, silence=False)
