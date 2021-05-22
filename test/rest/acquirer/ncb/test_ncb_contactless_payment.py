from hamcrest import assert_that, instance_of, equal_to

from constants import Currency, EmvTlv
from data.rest_requests import rest_emv_tlv_sale, rest_reversal
from model.rest import transactionResponse, terminalType
from wnclient import WNClient

wn = WNClient().vagrant.ncb
TERM_ID = '23001'

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


def test_ncb_contactless_icc_sale():
    """
    ICC sale POSEntryMode : 07
    Refund POS Entry Mode  : 011
    """
    p = rest_emv_tlv_sale()
    p.account.terminalType = terminalType.CHP
    p.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_ICC.value
    p.paymentMethod.emvTlv.contactless = None
    response = wn.rest(TERM_ID).sale(request=p, currency=Currency.JMD)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


def test_ncb_contactless_icc_visa_sale():
    """
    ICC sale POSEntryMode : 05
    Refund POS Entry Mode  : 011
    """
    p = rest_emv_tlv_sale()
    p.account.terminalType = terminalType.CHP
    p.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_ICC_VISA_DEBIT.value
    p.paymentMethod.emvTlv.contactless = None
    response = wn.rest(TERM_ID).sale(request=p, currency=Currency.JMD)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))


def test_ncb_contactless_msr_void():
    p = rest_emv_tlv_sale()
    p.account.terminalType = terminalType.CHP
    p.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_MSR.value
    p.paymentMethod.emvTlv.contactless = 'true'
    response = wn.rest(TERM_ID).sale(request=p, currency=Currency.JMD)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))

    r = rest_reversal(response.uniqueRef)
    r.account.terminalType = terminalType.CHP
    reversal_response = wn.rest(TERM_ID).reversal(request=r)
    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))


def test_ncb_contactless_msr_refund():
    p = rest_emv_tlv_sale()
    p.account.terminalType = terminalType.CHP
    p.paymentMethod.emvTlv.tlvString = EmvTlv.CONTACTLESS_MSR.value
    p.paymentMethod.emvTlv.contactless = 'true'
    response = wn.rest(TERM_ID).sale(request=p, currency=Currency.JMD)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))

    reversal_response = wn.rest(TERM_ID).refund_referenced(uniqueref=response.uniqueRef,
                                                           amount='{:2f}'.format(response.authorizedAmount / 2),
                                                           currency=Currency.JMD)
    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))


def test_ncb_set_contactless_manually():
    # 9F39 emv tag absent
    p = rest_emv_tlv_sale()
    p.account.terminalType = terminalType.CHP
    p.paymentMethod.emvTlv.tlvString = EmvTlv.TAG_9F39_ABSENT.value
    p.paymentMethod.emvTlv.contactless = 'true'

    response = wn.rest(TERM_ID).sale(request=p, currency=Currency.JMD)
    assert_that(response, instance_of(transactionResponse))
    # [com.merchant.rest.Payment] - Manually setting POS Entry Mode to contactless ICC
    # [com.merchant.bank.ncb.NCBMessage] - POS Entry Mode  : 071


def test_ncb_contactless_unspecifiad():
    # 9F39 emv tag absent
    p = rest_emv_tlv_sale()
    p.account.terminalType = terminalType.CHP
    p.paymentMethod.emvTlv.tlvString = EmvTlv.UNSPECIFIED.value
    p.paymentMethod.emvTlv.contactless = None

    response = wn.rest(TERM_ID).sale(request=p, currency=Currency.JMD)
    assert_that(response, instance_of(transactionResponse))
    # [com.merchant.rest.Payment] - Manually setting POS Entry Mode to contactless ICC
    # [com.merchant.bank.ncb.NCBMessage] - POS Entry Mode  : 051
