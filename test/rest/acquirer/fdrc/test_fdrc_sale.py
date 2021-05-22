import pytest
from hamcrest import assert_that, equal_to, instance_of

from constants import EmvTlv, PosDevice
from data.rest_requests import rest_sale, rest_emv_tlv_sale, rest_track2_sale, rest_track2contactless, \
    rest_securecard_sale, rest_keyed_securecard
from model.rest import paymentMethod, transactionResponse
from wnclient import WNClient

wn = WNClient().vagrant.wn
TERM_ID = '22005'


@pytest.mark.parametrize('cardtype', ['visa', 'mastercard', 'amex', 'discover'])
def test_rest_keyed_card_sale(cardtype):
    wn.rest(TERM_ID).sale(rest_sale(cardtype=cardtype))


def test_rest_securecard_sale():
    sc = rest_keyed_securecard()
    securecard_response = wn.rest(TERM_ID).create_securecard(sc)
    response = wn.rest(TERM_ID).sale(rest_securecard_sale(cardreference=securecard_response.cardReference))
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))
    assert_that(response.receiptFields.cardHolderName, equal_to(sc.tokenMethod.keyedSecureCard.cardHolderName))


def test_rest_unknown_card_track2_sale():
    r = rest_track2_sale()
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


def test_rest_emv_visa_sale():
    r = rest_emv_tlv_sale()
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


def test_rest_emv_contactless_icc_sale():
    r = rest_emv_tlv_sale()
    r.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_ICC.value
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


@pytest.mark.parametrize('device', [
    PosDevice.WISEPAD,
    PosDevice.WALKER_C2X,
    PosDevice.PAX_A80_ATTENDED,
    PosDevice.PAX_A920_ATTENDED
])
def test_rest_emv_contactless_icc_devices_sale(device):
    r = rest_emv_tlv_sale()
    r.account.deviceId = device.device_name
    r.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_ICC.value
    r.device.type_ = device.device_name
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


def test_rest_emv_contactless_9F99_sale():
    # ticket #26517
    r = rest_emv_tlv_sale()
    r.paymentMethod.emvTlv.tlvString = EmvTlv.TAG_9F66.value
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


def test_rest_track2contactless_sale():
    r = rest_emv_tlv_sale()
    r.paymentMethod = paymentMethod(track2Contactless=rest_track2contactless())
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))
    assert_that(response.receiptFields.cardType, equal_to('MasterCard'))


def test_rest_offline_decline_emv_sale():
    r = rest_emv_tlv_sale()
    r.transactionType = 'OFFLINE_DECLINE'
    response = wn.rest(TERM_ID).sale(r)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('D'))
    assert_that(response.description, equal_to('Offline decline'))


def test_settlement():
    respone = wn.http.test_settle(params={'terminal_id': TERM_ID})
    assert_that(respone.status_code, equal_to(200))
