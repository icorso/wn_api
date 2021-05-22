from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey, PaynomixCard
from data.rest2_payment_requests import rest2_payment_moto
from model.rest2.payment import Payment
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '22015'
KEY = db.get_api_key(ApiKey.API_WN_FULL)
wn = WNClient().vagrant.wn.rest2(terminal_id=TERM_ID)
wn_boarding = WNClient().vagrant.wn.boarding()


def test_payment_moto_valid():
    r = rest2_payment_moto()
    r.order.total_amount = random_amount(digits=2)
    r.customer_account.card_details.card_number = PaynomixCard.rand().cardnumber
    wn_boarding.update_terminal_integration(TERM_ID, 'autoReady', True, silence=True)
    wn_boarding.update_terminal_bank_settings(TERM_ID, 'allowPreAuth', True, silence=True)
    response = wn.payment(request=r, api2_key=KEY)
    assert_that(response, instance_of(Payment))
    assert_that(response.transaction_result.status, equal_to('READY'))
