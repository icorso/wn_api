import random

from faker import Factory

from constants import FiServCard
from data.rest_requests import rest_sale, rest_reversal, rest_unreferenced_card_refund
from model.rest import dukptPinDetails, pinDetails, refundMethod, refundUnreferenced, voucher
from wnclient import WNClient

wn = WNClient().vagrant.wn
TERM_ID = '22006'
fake = Factory.create()


def fiserv_keyed_payment():
    card = FiServCard.rand()

    p = rest_sale()
    p.without_field('customer', 'autoReady')
    p.account.terminalType = 'CHP'
    p.account.deviceId = 'ict_220_1'
    p.deviceType = 'INGENICO_ICT220'
    p.paymentMethod.keyedCard.cardHolderName = None
    p.paymentMethod.keyedCard.cardType = 'CBIC'
    p.paymentMethod.keyedCard.cardNumber = card.cardnum
    p.paymentMethod.keyedCard.cardAccount = card.cardaccount
    p.paymentMethod.keyedCard.cvv = None
    p.paymentMethod.keyedCard.pinDetails = pinDetails(dukptPinDetails(
        pin=card.pin,
        pinKsn=card.ksn
    ))
    p.requestType = 'PURCHASE'
    return p


def test_fiserv_sale_keyed_approved():
    a = 0
    for i in range(2900):
        term_id = str(random.randrange(22006, 23504))
        # print(term_id)
        response = wn.rest(term_id).sale(fiserv_keyed_payment())
        if a == 20:
            reversal_request = rest_reversal(uniqueref=response.uniqueRef)
            reversal_request.account.terminalType = 'CHP'
            reversal_response = wn.rest(term_id).reversal(reversal_request)

            request = rest_unreferenced_card_refund()
            request.deviceType = 'INGENICO_ICT220'
            request.account.deviceId = 'ict_220_1'
            request.refundMethod = refundMethod(
                unreferenced=refundUnreferenced(
                    voucher=voucher(
                        cardAccount=FiServCard.FS1.cardaccount,
                        cardNumber=FiServCard.FS1.cardnum,
                        cardType='CBIC',
                        voucherApprovalCode='123456',
                        voucherNumber='123456789012345'
                    ),
                    reason=fake.text(10),
                    orderId='RFND_' + str(fake.random_number(7, False))

                )
            )
            wn.rest(TERM_ID).refund(request)
            a = 0

        a += 1
        print(a)
