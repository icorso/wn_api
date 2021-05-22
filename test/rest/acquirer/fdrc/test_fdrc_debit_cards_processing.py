import pytest
from hamcrest import assert_that, is_not, instance_of, equal_to

from constants import EmvTlv, PosDevice
from data.rest_requests import rest_reversal, rest_emv_tlv_sale
from model.rest import transactionResponse
from wnclient import WNClient

TERM_ID = '22004'
wn = WNClient().local.goepay.rest(TERM_ID)
db = WNClient().db(terminal_number=TERM_ID)

# Pilot feature #24496 - [FDRC] Debit Processing should be turned on


@pytest.mark.parametrize('cardtype, emv', [
    ('VISA DEBIT', EmvTlv.CONTACTLESS_ICC_VISA_DEBIT),
    ('DEBIT MASTERCARD', EmvTlv.CONTACTLESS_ICC_MC_DEBIT),
    ('VISA', EmvTlv.CONTACTLESS_ICC),
    ('MASTERCARD', EmvTlv.CONTACTLESS_ICC_MC_CREDIT)
])
def test_fdrc_contacless_icc_sale(cardtype, emv):
    s = rest_emv_tlv_sale()
    s.paymentMethod.emvTlv.cardType = cardtype
    s.paymentMethod.emvTlv.tlvString = emv.value
    sale_response = wn.sale(request=s)
    assert_that(sale_response, instance_of(transactionResponse))
    assert_that(sale_response.code, equal_to('A'))


@pytest.mark.parametrize('cardtype, emv', [
    ('VISA DEBIT', EmvTlv.CONTACTLESS_ICC_VISA_DEBIT),
    ('DEBIT MASTERCARD', EmvTlv.CONTACTLESS_ICC_MC_DEBIT),
    ('VISA', EmvTlv.CONTACTLESS_ICC),
    ('MASTERCARD', EmvTlv.CONTACTLESS_ICC_MC_CREDIT)

])
def test_fdrc_emv_contactless_icc_reversal(cardtype, emv):
    s = rest_emv_tlv_sale()
    s.paymentMethod.emvTlv.cardType = cardtype
    s.paymentMethod.emvTlv.tlvString = emv.value
    sale_response = wn.sale(request=s)
    unique_ref = wn.reporting_list(TERM_ID, closed='false', order_id=s.orderId).transactionSummary[0].uniqueRef
    assert_that(unique_ref, is_not(None))

    # check logs for - a <DebitRequest> tag should be sent to FDRC.
    r = rest_reversal(uniqueref=unique_ref)
    reversal_response = wn.reversal(r)
    # None of the card-specific groups: AmexGrp, MCGrp, VisaGrp, DSGrp should be sent in the Void or
    # Completion (Settlement) request.
    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))
