from faker import Factory
from hamcrest import assert_that, instance_of

from constants import ApiKey
from data.rest2_payment_requests import rest2_payment_moto
from model.rest2 import Surcharge, OrderBreakdown, Tip
from model.rest2.payment import Payment
from utils import SurchargeAmount
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '21001'
KEY = db.get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)
wn_boarding = WNClient().vagrant.go.boarding()


def test_payment_surcharge_tip():
    amount = 8.81
    tip = 1.32
    amounts = SurchargeAmount(amount=amount + tip, percentage=4)
    p = rest2_payment_moto()
    p.order.total_amount = round(amount + tip + amounts.surcharge, 2)
    p.order.order_breakdown = OrderBreakdown(
        subtotal_amount=amount,
        tip=Tip(
            type='FIXED_AMOUNT',
            amount=tip
        ),
        surcharge=Surcharge(
            applied=True,
            amount=amounts.surcharge,
            percentage=amounts.percentage
        )
    )

    response = wn.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
