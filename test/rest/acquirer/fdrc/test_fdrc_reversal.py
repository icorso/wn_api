from faker import Factory
from hamcrest import assert_that, is_not, instance_of, equal_to

from constants import EmvTlv, ApiKey, Currency, LocalMerchant
from data.rest_requests import rest_reversal, rest_emv_tlv_sale, rest_sale
from model.boarding2 import FdrcTerminal
from model.rest import transactionResponse
from wnclient import WNClient

fake = Factory.create()

GOEPAY_KEY = ApiKey.BOARDING_GOEPAY_FULL
TERM_ID = '22004'
CURRENCY = Currency.USD
MERCHANT_ID = LocalMerchant.GOEPAY.itemid

wn = WNClient().local.goepay.rest(TERM_ID)
wn_boarding = WNClient().local.goepay.boarding()
wn_boarding2 = WNClient().local.goepay.boarding2()
db = WNClient().db(terminal_number=TERM_ID)


def test_disable_alternative_routing():
    key = db.get_api_key(GOEPAY_KEY)
    wn_boarding2.update_processing_rules(merchant_id=MERCHANT_ID, terminal_number=TERM_ID, response_type=FdrcTerminal,
                                         to_terminal=TERM_ID, enable=False, boarding2_key=key)


def test_fdrc_keyed_reversal():
    sale_response = wn.sale(request=rest_sale())

    assert_that(sale_response.uniqueRef, is_not(None))
    reversal_response = wn.reversal(rest_reversal(sale_response.uniqueRef))

    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))
    assert_that(reversal_response.authorizedAmount, equal_to(sale_response.authorizedAmount))


def test_fdrc_emv_reversal_overwrite():
    s = rest_emv_tlv_sale()
    s.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_ICC.value
    s.paymentMethod.emvTlv.contactless = 'true'
    sale_response = wn.sale(request=s)
    unique_ref = wn.reporting_list(TERM_ID, closed='false', order_id=s.orderId).transactionSummary[0].uniqueRef
    assert_that(unique_ref, is_not(None))

    r = rest_reversal(uniqueref=unique_ref)
    r.receiptDetailsRequired = True
    r.tlvString = EmvTlv.CONTACTLESS_ICC_9F10_CHANGED.value
    reversal_response = wn.reversal(r)
    # check logs for emv parsed data
    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))


def test_fdrc_emv_reversal_without_tlv_string():
    s = rest_emv_tlv_sale()
    s.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_ICC.value
    s.paymentMethod.emvTlv.contactless = 'true'
    sale_response = wn.sale(request=s)
    unique_ref = wn.reporting_list(TERM_ID, closed='false', order_id=s.orderId).transactionSummary[0].uniqueRef
    assert_that(unique_ref, is_not(None))

    r = rest_reversal(uniqueref=unique_ref)
    r.receiptDetailsRequired = True
    reversal_response = wn.reversal(r)
    # check logs for emv parsed data - reversal emv data should be taken from transaction_icc table
    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))


def test_fdrc_emv_reversal_incorrect_tlv_string():
    s = rest_emv_tlv_sale()
    s.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_ICC.value
    s.paymentMethod.emvTlv.contactless = 'true'
    sale_response = wn.sale(request=s)
    unique_ref = wn.reporting_list(TERM_ID, closed='false', order_id=s.orderId).transactionSummary[0].uniqueRef
    assert_that(unique_ref, is_not(None))

    r = rest_reversal(uniqueref=unique_ref)
    r.receiptDetailsRequired = True
    r.tlvString = '0123575843'
    reversal_response = wn.reversal(r)
    # check logs for emv parsed data - reversal emv data should be taken from transaction_icc table
    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))

