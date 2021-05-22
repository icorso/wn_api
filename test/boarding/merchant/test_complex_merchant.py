import random

from faker import Factory

from data.boarding.merchant import merchant
from data.boarding.terminal import tsys_saratoga_terminal
from data.xml_requests import securecard_registration
from wnclient import WNClient

wnclient = WNClient()
wn = WNClient().local.go
fake = Factory.create()


def test_boarding_merchant_create():
    total_merchant = 1
    terminals_per_merchant = 1
    securecards_per_terminal = 1
    for mm in range(0, total_merchant):
        m = wnclient.local.go.boarding().create_merchant(request=merchant('GlobalOnePay', fake.name()), silence=True)
        for tt in range(0, terminals_per_merchant):
            t = tsys_saratoga_terminal(merchant_id=m.merchantId)
            t.features.validateScSecurity = False
            t_response = wnclient.local.go.boarding().create_terminal(request=t, silence=True)
            for scsc in range(0, securecards_per_terminal):
                sc = securecard_registration(cardtype=random.choice(['visa', 'mastercard', 'discover', 'amex']), cvv='999')
                response = wn.xml(t_response .terminalNumber).secure_card_registration(request=sc, silence=True)
