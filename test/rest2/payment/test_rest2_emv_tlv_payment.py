import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey, EmvTlv, PosDevice, CardReadMethod
from data.rest2_payment_requests import rest2_payment_emv
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '21001'
db = WNClient().db(terminal_number=TERM_ID)
KEY = db.get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)
wn_boarding = WNClient().vagrant.go.boarding()


def test_payment_emv_tlv_contacless_icc_valid():
    p = rest2_payment_emv(tlv_string=EmvTlv.CONTACTLESS_ICC.value, device_type=PosDevice.WISEPAD, ksn='88888835400002200001')
    response = wn.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
    db_transaction = db.get_transaction(uniqueref=response.unique_reference)
    assert_that(db_transaction.cardreadmethod, equal_to(CardReadMethod.CONTACTLESS_ICC))
    #  [com.merchant.bank.tsyssaratoga.helpers.PosEntryMode] - [POS Entry Mode] 0710


@pytest.mark.parametrize('tlv_string', [EmvTlv.UNSPECIFIED, EmvTlv.TAG_9F39_ABSENT])
def test_payment_emv_tlv_contacless_icc_unspecified(tlv_string):
    p = rest2_payment_emv(tlv_string=tlv_string.value, device_type=PosDevice.WISEPAD, ksn='88888835400002200001')
    response = wn.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
    db_transaction = db.get_transaction(uniqueref=response.unique_reference)
    assert_that(db_transaction.cardreadmethod, equal_to(CardReadMethod.ICC))
    # [com.merchant.bank.tsyssaratoga.helpers.PosEntryMode] - [POS Entry Mode] 0510
