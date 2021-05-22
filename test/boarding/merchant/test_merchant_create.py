from constants import MerchantPortfolio
from data.boarding.merchant import merchant
from wnclient import WNClient

wnclient = WNClient()


def test_boarding_merchant_create():
    wnclient.vagrant.wn.boarding().create_merchant(request=merchant(MerchantPortfolio.WN.mpid, host='WN', dba_name='merchant_wn'))
    # wnclient.vagrant.go.boarding().create_merchant(request=merchant(MerchantPortfolio.GO.mpid, host='Global One', dba_name='merchant_go'))
    # wnclient.local.pago.boarding().create_merchant(request=merchant('Pago Technology', 'pago'))
    # wnclient.local.ac.boarding().create_merchant(request=merchant('AnywhereCommerce', 'ac'))
    # wnclient.local.goepay.boarding().create_merchant(request=merchant('go ePay', 'goepay'))


def test_boarding_hound_merchant_create():
    # wnclient.hound.wn.boarding().create_merchant(request=merchant('WorldNet TPS', 'archiving_wn'))
    # wnclient.hound.go.boarding().create_merchant(request=merchant('GlobalOnePay', 'archiving_go'))
    # wnclient.hound.pago.boarding().create_merchant(request=merchant('Pago Technology', 'archiving_pago'))
    # wnclient.hound.ac.boarding().create_merchant(request=merchant('AnywhereCommerce', 'archiving_ac'))
    wnclient.hound.goepay.boarding().create_merchant(request=merchant('go ePay', 'archiving_goepay'))
