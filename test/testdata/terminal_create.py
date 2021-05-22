from constants import Country, LocalMerchant
from data.boarding.terminal import braintree_terminal, tsys_saratoga_terminal, elavon_pos_terminal, nmi_terminal, \
    cybersourcesoap_terminal, flapws_terminal, maxconnect_terminal, netaxcept_terminal, paysafe_terminal, \
    payulatam_terminal, moneris_terminal, payvision_terminal, elavon_terminal, \
    securepay_terminal, fiserv_terminal, integrapay_terminal, tango_terminal, elavon_converge_terminal, \
    cashflows_terminal, aib_terminal, worldpay_terminal, allpago_terminal, tsys_sierra_terminal, fdrc_terminal, \
    propay_terminal, ctpayments_terminal, ncb_terminal, credorax_terminal, barclaycard_terminal, \
    authnet_terminal
from wnclient import WNClient

wn = WNClient().vagrant.wn
go = WNClient().vagrant.go
ncb = WNClient().vagrant.ncb


def test_globalone_terminal_create():
    # merchant_go terminals:
    go.boarding().create_terminal(request=tsys_saratoga_terminal(merchant_id=LocalMerchant.GO.itemid))
    mc_saratoga_term = tsys_saratoga_terminal(merchant_id=LocalMerchant.GO.itemid)
    mc_saratoga_term.bankSettings.allowMulticurrency = True
    go.boarding().create_terminal(request=mc_saratoga_term)
    go.boarding().create_terminal(request=nmi_terminal(merchant_id=LocalMerchant.GO.itemid))
    go.boarding().create_terminal(request=tango_terminal(merchant_id=LocalMerchant.GO.itemid))
    go.boarding().create_terminal(request=payulatam_terminal(merchant_id=LocalMerchant.GO.itemid, country=Country.Panama))
    go.boarding().create_terminal(request=tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid))
    go.boarding().create_terminal(request=ctpayments_terminal(merchant_id=LocalMerchant.GO.itemid))


def test_worldnet_terminal_create():
    wn.boarding().create_terminal(request=elavon_terminal(merchant_id=LocalMerchant.WN.itemid))
    wn.boarding().create_terminal(request=elavon_pos_terminal(merchant_id=LocalMerchant.WN.itemid))
    wn.boarding().create_terminal(request=aib_terminal(merchant_id=LocalMerchant.WN.itemid))
    wn.boarding().create_terminal(request=cashflows_terminal(merchant_id=LocalMerchant.WN.itemid))
    wn.boarding().create_terminal(request=fdrc_terminal(merchant_id=LocalMerchant.WN.itemid))
    wn.boarding().create_terminal(request=fiserv_terminal(merchant_id=LocalMerchant.WN.itemid))
    wn.boarding().create_terminal(request=credorax_terminal(merchant_id=LocalMerchant.WN.itemid))
    wn.boarding().create_terminal(request=worldpay_terminal(merchant_id=LocalMerchant.WN.itemid))
    wn.boarding().create_terminal(request=barclaycard_terminal(merchant_id=LocalMerchant.WN.itemid))
    wn.boarding().create_terminal(request=authnet_terminal(merchant_id=LocalMerchant.WN.itemid))
    wn.boarding().create_terminal(request=elavon_pos_terminal(merchant_id=LocalMerchant.WN.itemid))
    wn.boarding().create_terminal(request=nmi_terminal(merchant_id=LocalMerchant.WN.itemid))

    # ncb.boarding().create_terminal(request=ncb_terminal(merchant_id=LocalMerchant.NCB.itemid)) # not possible now

    # wn.vagrant.wn.boarding().create_terminal(request=paysafe_terminal(merchant_id=LocalMerchant.WN.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=braintree_terminal(merchant_id=LocalMerchant.GO.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=flapws_terminal(merchant_id=LocalMerchant.GO.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=maxconnect_terminal(merchant_id=LocalMerchant.GO.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=cybersourcesoap_terminal(merchant_id=LocalMerchant.GO.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=integrapay_terminal(merchant_id=LocalMerchant.GO.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=moneris_terminal(merchant_id=LocalMerchant.GO.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=payvision_terminal(merchant_id=LocalMerchant.GO.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=securepay_terminal(merchant_id=LocalMerchant.GO.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=netaxcept_terminal(merchant_id=LocalMerchant.GO.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=propay_terminal(merchant_id=LocalMerchant.GO.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=elavon_converge_terminal(merchant_id=LocalMerchant.GO.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=allpago_terminal(merchant_id=LocalMerchant.GO.itemid))
    # wn.vagrant.go.boarding().create_terminal(request=tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid))
