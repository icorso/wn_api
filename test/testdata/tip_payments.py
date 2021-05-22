import random
from decimal import Decimal

from faker import Factory

from data.rest_requests import rest_sale, rest_tip
from model.rest import tipType
from utils import random_amount, random_text
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.go


def test_saratoga_tip_rest_payment():
    for i in range(2000):
        amount = round(random_amount(digits=1), 0)
        tip_percentage = Decimal(0.01)

        p = rest_sale(amount=amount,
                      cardtype=random.choice(['VISA', 'mastercard', 'jcb', 'discover', 'maestro']),
                      cvv='999')
        tip = rest_tip(amount=(amount * float(tip_percentage)), tip_type=tipType.PERCENTAGE)
        tip.percentage = 1
        p.tip = tip
        p.orderId = random_text(15)

        wn.rest(terminal_id=str(21024 + random.randrange(50))).sale(request=p)
        print(i)
