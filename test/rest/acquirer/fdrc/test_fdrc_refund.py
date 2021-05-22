import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, is_not

from constants import Currency, PosDevice, EmvTlv, ApiKey, LocalMerchant
from data.rest_requests import rest_unreferenced_card_refund, rest_emv_tlv_sale, rest_referenced_refund, rest_reversal, \
    rest_sale
from model.boarding2 import FdrcTerminal
from model.rest import transactionResponse
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()

BOARDING_KEY = ApiKey.BOARDING_WN_FULL
MERCHANT_ID = LocalMerchant.GOEPAY.itemid
TERM_ID = '22005'
CURRENCY = Currency.USD

wn = WNClient().vagrant.wn.rest(TERM_ID)
wn_boarding = WNClient().vagrant.wn.boarding()
wn_boarding2 = WNClient().vagrant.wn.boarding2()
db = WNClient().db(terminal_number=TERM_ID)


def test_disable_fdrc_alternative_routing():
    key = db.get_api_key(BOARDING_KEY)
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=TERM_ID, response_type=FdrcTerminal,
                                         to_terminal=TERM_ID, enable=False, boarding2_key=key)


def test_referenced_partial_refund():
    refund_amount = 0.12
    sale_response = wn.sale(request=rest_sale())

    assert_that(sale_response.uniqueRef, is_not(None))
    refund_response = wn.refund_referenced(uniqueref=sale_response.uniqueRef, amount=refund_amount)

    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(round(sale_response.authorizedAmount - refund_amount, 2)))


def test_unreferenced_refund():
    amount = random_amount()
    refund_response = wn.refund_unreferenced(amount=amount)

    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(amount * -1))


@pytest.mark.parametrize('device,term_cat_code', [
    (PosDevice.PAX_A80_ATTENDED.device_name, '01'),  # pos_device.is_mpos = 0
    (PosDevice.WISEPAD.device_name, '09')            # pos_device.is_mpos = 1
])
def test_rest_fdrc_partial_refund(device, term_cat_code):
    s = rest_emv_tlv_sale(device_type=device)
    sale_response = wn.sale(request=s)
    refund_amount = 0.12
    unique_ref = wn.reporting_list(TERM_ID, order_id=s.orderId).transactionSummary[0].uniqueRef
    assert_that(unique_ref, is_not(None))

    refund_response = wn.refund_referenced(uniqueref=unique_ref, amount=refund_amount, currency=CURRENCY)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))
    assert_that(refund_response.authorizedAmount, equal_to(float(s.amount.amount) - refund_amount))

    db_response = db.get_fdrc_transaction(uniqueref=refund_response.uniqueRef)
    assert_that(db_response.orig_term_cat_code, equal_to(term_cat_code))


@pytest.mark.parametrize('device,term_cat_code', [
    (PosDevice.PAX_A80_ATTENDED.device_name, '01'),  # pos_device.is_mpos = 0
    (PosDevice.WISEPAD.device_name, '09')            # pos_device.is_mpos = 1
])
def test_rest_fdrc_unreferenced_refund(device, term_cat_code):
    refund_request = rest_unreferenced_card_refund(device_type=device)
    refund_response = wn.refund(request=refund_request)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.code, equal_to('A'))

    db_response = db.get_fdrc_transaction(uniqueref=refund_response.uniqueRef)
    assert_that(db_response.orig_term_cat_code, equal_to(term_cat_code))


@pytest.mark.parametrize('device,term_cat_code', [
    (PosDevice.PAX_A80_ATTENDED.device_name, '01'),  # pos_device.is_mpos = 0
    (PosDevice.WISEPAD.device_name, '09')            # pos_device.is_mpos = 1
])
def test_fdrc_pos_term_cat_code_reversal(device, term_cat_code):
    s = rest_emv_tlv_sale(device_type=device)
    s.paymentMethod.emvTlv.cardType = 'amex'
    s.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_ICC_DISCOVER.value

    sale_response = wn.sale(request=s)
    unique_ref = wn.reporting_list(TERM_ID, closed='false', order_id=s.orderId).transactionSummary[0].uniqueRef
    assert_that(unique_ref, is_not(None))

    r = rest_reversal(uniqueref=unique_ref, device_type=device)
    reversal_response = wn.reversal(r)
    # check logs for the TermCatCode value
    # manually check:
    # - completion (settlement) request
    # - refund (after settlement) //TODO need to clarify why it's set to 00
    # <TermCatCode>09</TermCatCode> for pos_device.is_mpos = 1 devices
    # <TermCatCode>01</TermCatCode> for pos_device.is_mpos = 0 devices
    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))

    db_response = db.get_fdrc_transaction(uniqueref=unique_ref)
    assert_that(db_response.orig_term_cat_code, equal_to(term_cat_code))
