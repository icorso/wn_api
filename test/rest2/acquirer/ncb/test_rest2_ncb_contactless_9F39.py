import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import ApiKey, EmvTlv, PosDevice, Currency, CardReadMethod
from data.rest2_payment_requests import rest2_payment_emv, rest2_payment_msr_encrypted
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '23001'
db = WNClient().db(terminal_number=TERM_ID)
KEY = db.get_api_key(ApiKey.API_NCB_FULL)
wn = WNClient().vagrant.ncb.rest2(terminal_id=TERM_ID)
"""
NCB POS entry mode values:
---------------------------
PEM_MANUAL_WITH_PIN = "011";
PEM_SWIPE_WITH_PIN = "021";
PEM_ICC_WITH_PIN = "051";
PEM_SWIPE_FALLBACK = "801";
PEM_CONTACTLESS_ICC= "007";
PEM_CONTACTLESS_MSR = "007";
"""


def test_ncb_payment_contactless_icc():
    p = rest2_payment_emv(tlv_string=EmvTlv.CONTACTLESS_ICC.value,
                          device_type=PosDevice.WISEPAD,
                          ksn='88888835400002200001',
                          currency=Currency.JMD)
    response = wn.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
    db_transaction = db.get_transaction(uniqueref=response.unique_reference)
    assert_that(db_transaction.cardreadmethod, equal_to(CardReadMethod.CONTACTLESS_ICC))
    # [com.merchant.bank.ncb.NCBMessage] - POS Entry Mode  : 071


@pytest.mark.parametrize('tlv_string', [
    EmvTlv.UNSPECIFIED,
    EmvTlv.TAG_9F39_ABSENT
])
def test_ncb_payment_icc_tag_9f39_not_specified(tlv_string):
    p = rest2_payment_emv(tlv_string=tlv_string.value,
                          device_type=PosDevice.WISEPAD,
                          ksn='88888835400002200001',
                          currency=Currency.JMD)
    response = wn.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
    db_transaction = db.get_transaction(uniqueref=response.unique_reference)
    assert_that(db_transaction.cardreadmethod, equal_to(CardReadMethod.ICC))
    # [com.merchant.bank.ncb.NCBMessage] - POS Entry Mode  : 051


def test_ncb_payment_contactless_msr():
    p = rest2_payment_msr_encrypted(encrypted_data='C3436C5CC89E6FD3A9822B6F1D13782E4FFDEBD444C6C515',
                                    ksn='88888835400002200001',
                                    device_type=PosDevice.WISEPAD,
                                    additional_tlv_data='9F390191',
                                    currency=Currency.JMD)
    response = wn.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
    db_transaction = db.get_transaction(uniqueref=response.unique_reference)
    assert_that(db_transaction.cardreadmethod, equal_to(CardReadMethod.CONTACTLESS_MSR))
    # [com.merchant.bank.ncb.NCBMessage] - POS Entry Mode  : 071


def test_payment_msr_encrypted_keyed():
    # decrypted data ;4024007118320745=221210114991888?
    # BDK index 2
    # KSN 88888835400002200001
    p = rest2_payment_msr_encrypted('C3436C5CC89E6FD3A9822B6F1D13782E4FFDEBD444C6C515',
                                    device_type=PosDevice.WISEPAD,
                                    ksn='88888835400002200001', currency=Currency.JMD)
    response = wn.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
    db_transaction = db.get_transaction(uniqueref=response.unique_reference)
    assert_that(db_transaction.cardreadmethod, equal_to(CardReadMethod.KEYED))
    # [com.merchant.bank.ncb.NCBMessage] -[POS Entry Mode] 0110
