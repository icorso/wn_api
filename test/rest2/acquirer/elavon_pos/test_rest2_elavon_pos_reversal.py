from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey, EmvTlv, PosDevice, Currency, CardReadMethod
from data.rest2_payment_requests import rest2_payment_moto, rest2_payment_emv
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '22002'
wn = WNClient().vagrant.wn.rest2(terminal_id=TERM_ID)
wn_boarding = WNClient().vagrant.wn.boarding()
db = WNClient().db(terminal_number=TERM_ID)
KEY = db.get_api_key(ApiKey.API_WN_FULL)


def test_payment_moto_valid():
    response = wn.payment(request=rest2_payment_moto(), api2_key=KEY)
    assert_that(response, instance_of(Payment))

    reversal_response = wn.payment_reverse(uniqueref=response.unique_reference,
                                           amount=response.order.total_amount,
                                           api2_key=KEY)
# operator not set


def test_elavon_pos_payment_contactless_icc():
    p = rest2_payment_emv(tlv_string=EmvTlv.CONTACTLESS_ICC.value,
                          device_type=PosDevice.WISEPAD,
                          ksn='88888835400002200001')
    response = wn.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
    db_transaction = db.get_transaction(uniqueref=response.unique_reference)
    assert_that(db_transaction.cardreadmethod, equal_to(CardReadMethod.CONTACTLESS_ICC))
