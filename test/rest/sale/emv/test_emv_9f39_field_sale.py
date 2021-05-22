from hamcrest import assert_that, instance_of

from constants import EmvTlv, Currency, PosDevice
from data.rest_requests import rest_emv_tlv_sale
from model.rest import transactionResponse
from wnclient import WNClient

wn = WNClient().vagrant.go
TERM_ID = '21001'
DEVICE = PosDevice.WISEPAD.device_name
CURRENCY = Currency.USD


def test_saratoga_emv_contactless_icc_contactless_true():
    # 9F39: 07 - Contactless ICC
    p = rest_emv_tlv_sale()
    p.deviceType = DEVICE
    p.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_ICC_MC_CREDIT.value
    p.paymentMethod.emvTlv.contactless = 'true'
    p.device.type_ = DEVICE

    response = wn.rest(terminal_id=TERM_ID).sale(request=p, currency=CURRENCY)
    assert_that(response, instance_of(transactionResponse))
    # Result: Set the transaction as 07 Contactless Integrated Circuit Read
    # 2020-07-15 17:47:27,132 DEBUG [default task-4] [com.merchant.bank.tsyssaratoga.helpers.PosEntryMode] - [POS Entry Mode] 0710


def test_saratoga_emv_contactless_msr_contactless_true():
    # 9F39: 91 - Contactless MSR
    p = rest_emv_tlv_sale()
    p.deviceType = DEVICE
    p.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_MSR.value
    p.paymentMethod.emvTlv.contactless = 'true'
    p.device.type_ = DEVICE

    response = wn.rest(terminal_id=TERM_ID).sale(request=p, currency=CURRENCY)
    assert_that(response, instance_of(transactionResponse))
    # Result: Set the transaction as 91 Contactless Magnetic Stripe Read
    # 2020-07-15 17:48:39,403 DEBUG [default task-4] [com.merchant.bank.tsyssaratoga.helpers.PosEntryMode] - [POS Entry Mode] 9120


def test_saratoga_emv_unspecified_contactless_true():
    # 9F39: 00 - Unspecified
    p = rest_emv_tlv_sale()
    p.deviceType = DEVICE
    p.paymentMethod.emvTlv.tlvString = EmvTlv.UNSPECIFIED.value
    p.paymentMethod.emvTlv.contactless = 'true'
    p.device.type_ = DEVICE

    response = wn.rest(terminal_id=TERM_ID).sale(request=p, currency=CURRENCY)
    assert_that(response, instance_of(transactionResponse))
    # Result: Set the transaction as 05 Integrated Circuit Read (CVV data Reliable)
    # 2020-07-15 17:55:20,474 INFO  [default task-4] [com.merchant.rest.Payment] - POS Entry Mode: 00
    # 2020-07-15 17:55:20,502 DEBUG [default task-4] [com.merchant.bank.tsyssaratoga.helpers.PosEntryMode] - [POS Entry Mode] 0520


def test_saratoga_emv_absent_contactless_true():
    # 9F39 absent
    p = rest_emv_tlv_sale()
    p.deviceType = DEVICE
    p.paymentMethod.emvTlv.tlvString = EmvTlv.TAG_9F39_ABSENT.value
    p.paymentMethod.emvTlv.contactless = 'true'
    p.device.type_ = DEVICE

    response = wn.rest(terminal_id=TERM_ID).sale(request=p, currency=CURRENCY)
    assert_that(response, instance_of(transactionResponse))
    # 2020-07-15 17:52:19,154 INFO  [default task-4] [com.merchant.rest.Payment] - Manually setting POS Entry Mode to contactless
    # 2020-07-15 17:52:19,189 DEBUG [default task-4] [com.merchant.bank.tsyssaratoga.helpers.PosEntryMode] - [POS Entry Mode] 9120


# contactless false or none


def test_saratoga_emv_contactless_msr_contactless_none():
    # 9F39: 91 - Contactless MSR
    p = rest_emv_tlv_sale()
    p.deviceType = DEVICE
    p.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_MSR.value
    p.paymentMethod.emvTlv.contactless = None
    p.device.type_ = DEVICE
    response = wn.rest(terminal_id=TERM_ID).sale(request=p, currency=CURRENCY)
    assert_that(response, instance_of(transactionResponse))
    # Result: Set the transaction as 91 Contactless Magnetic Stripe Read
    # 2020-07-15 18:18:53,841 DEBUG [default task-4] [com.merchant.bank.tsyssaratoga.helpers.PosEntryMode] - [POS Entry Mode] 9120


def test_saratoga_emv_contactless_icc_contactless_none():
    # 9F39: 07 - Contactless ICC
    p = rest_emv_tlv_sale()
    p.deviceType = DEVICE
    p.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_ICC.value
    p.paymentMethod.emvTlv.contactless = None
    p.device.type_ = DEVICE

    response = wn.rest(terminal_id=TERM_ID).sale(request=p)
    assert_that(response, instance_of(transactionResponse))
    # Result: Set the transaction as 07 Contactless Integrated Circuit Read
    # 2020-07-15 18:26:12,475 DEBUG [default task-4] [com.merchant.bank.tsyssaratoga.helpers.PosEntryMode] - [POS Entry Mode] 0720


def test_saratoga_emv_unspecified_contactless_none():
    # 9F39: 00 - Unspecified
    p = rest_emv_tlv_sale()
    p.deviceType = DEVICE
    p.paymentMethod.emvTlv.tlvString = EmvTlv.UNSPECIFIED.value
    p.paymentMethod.emvTlv.contactless = None
    p.device.type_ = DEVICE

    response = wn.rest(terminal_id=TERM_ID).sale(request=p, currency=CURRENCY)
    assert_that(response, instance_of(transactionResponse))
    # Expected result: pos entry mode = 05 (ICC)
    # 2020-07-15 12:37:50,450 DEBUG [default task-2] [com.merchant.bank.tsyssaratoga.helpers.PosEntryMode] - [POS Entry Mode] 0520


def test_saratoga_emv_absent_contactless_none():
    # 9F39 absent
    p = rest_emv_tlv_sale()
    p.deviceType = DEVICE
    p.paymentMethod.emvTlv.tlvString = EmvTlv.TAG_9F39_ABSENT
    p.paymentMethod.emvTlv.contactless = None
    p.device.type_ = DEVICE

    response = wn.rest(terminal_id=TERM_ID).sale(request=p, currency=CURRENCY)
    assert_that(response, instance_of(transactionResponse))
    # Result: Set the transaction as 05 Integrated Circuit Read (CVV data Reliable)
    # 2020-07-15 18:30:02,727 DEBUG [default task-4] [com.merchant.bank.tsyssaratoga.helpers.PosEntryMode] - [POS Entry Mode] 0520