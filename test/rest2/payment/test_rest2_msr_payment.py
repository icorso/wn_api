from faker import Factory
from faker import Factory
from hamcrest import assert_that, instance_of

from constants import ApiKey, PosDevice, MsrPayload
from data.rest2_payment_requests import rest2_payment_msr_encrypted
from model.rest2.payment import Payment
from wnclient import WNClient

fake = Factory.create()

db = WNClient().db()
TERM_ID = '21001'
KEY = db.get_api_key(ApiKey.API_GO_FULL)
wn = WNClient().vagrant.go.rest2(terminal_id=TERM_ID)
wn_boarding = WNClient().vagrant.go.boarding()


def test_payment_contactless_msr():
    p = rest2_payment_msr_encrypted(encrypted_data=MsrPayload.VISA.encrypted,
                                    ksn='88888835400002200001',
                                    device_type=PosDevice.WISEPAD,
                                    additional_tlv_data='9F390191')
    response = wn.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
    # [com.merchant.bank.tsyssaratoga.helpers.PosEntryMode] - [POS Entry Mode] 9110


def test_payment_encrypted_keyed_msr():
    p = rest2_payment_msr_encrypted(MsrPayload.VISA.encrypted,
                                    device_type=PosDevice.WISEPAD,
                                    ksn='88888835400002200001')
    response = wn.payment(request=p, api2_key=KEY, silence=False)
    assert_that(response, instance_of(Payment))
    # [com.merchant.bank.tsyssaratoga.helpers.PosEntryMode] - [POS Entry Mode] 0110
