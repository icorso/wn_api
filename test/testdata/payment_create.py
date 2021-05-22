import random
from time import sleep

from faker import Factory

from constants import Currency
from data.xml_requests import payment_avs
from utils import today, random_amount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_LIST = [['21001', False], ['21009', False], ['21002', True]]


def test_create_random_payments():
    b = 0
    for i in range(1000):
        t = random.choice(TERM_LIST)
        amount = random_amount()
        response = wn.xml(t[0]).payment(
            payment_avs(amount=amount, cardtype=random.choice(['jcb', 'visa', 'mastercard', 'amex', 'discover'])),
            is_multicurrency=t[1]
        )

        if b == 2:
            wn.xml(t[0]).refund(amount=amount-0.33, uniqueref=response.UNIQUEREF, currency=Currency.USD)

        if b == 3:
            wn.xml(t[0]).refund(amount=amount, uniqueref=response.UNIQUEREF, currency=Currency.USD)

        if b == 4:
            for t in TERM_LIST:
                wn.boarding().update_terminal_batch_time(terminal_number=t[0], batch_time=today(format='%H:%M', hours=-3))
            b = 0
        b += 1
        sleep(2)
