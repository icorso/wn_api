from hamcrest import assert_that, is_not, instance_of, equal_to

from constants import EmvTlv
from data.rest_requests import rest_reversal, rest_emv_tlv_sale
from model.rest import transactionResponse
from wnclient import WNClient

TERM_ID = '20004'
wn = WNClient().local.goepay.rest(TERM_ID)


def test_elavon_pos_reversal_valid_emv_data():
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
    # check logs for emv
    assert_that(reversal_response, instance_of(transactionResponse))
    assert_that(reversal_response.code, equal_to('A'))
