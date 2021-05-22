from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import FiServCard, Currency
from data.rest_requests import rest_account
from model.rest import dukptPinDetails, pinDetails, balanceInquiry, paymentMethod, keyedCard, \
    trackData, balanceInquiryResponse
from utils import today
from wnclient import WNClient

wn = WNClient().vagrant.wn
TERM_ID = '22006'
fake = Factory.create()


def balance_inquiry_request():
    card = FiServCard.rand()

    return balanceInquiry(
        currency=Currency.USD.name,
        account=rest_account(TERM_ID),
        dateTime=today(format='%Y-%m-%dT%H:%M:%S'),
        deviceType='INGENICO_ICT220',
        cardReadMethod=paymentMethod(keyedCard=keyedCard(
            cardHolderName='Some name',
            cardType='CBIC',
            cardNumber=card.cardnum,
            cardAccount=card.cardaccount,
            expiryDate='0124',
            cvv=None,
            pinDetails=pinDetails(dukptPinDetails(pin=card.pin, pinKsn=card.ksn))
        ))
    )


def balance_inquiry_track2_request():
    # ;6007602801003837964=181010114991888?
    # KSN=FFFF5678901234E00001
    # BDK Index=1
    # POS Device=WISEPAD
    return balanceInquiry(
        currency=Currency.USD.name,
        account=rest_account(TERM_ID),
        dateTime=today(format='%Y-%m-%dT%H:%M:%S'),
        deviceType='WISEPAD',
        cardReadMethod=paymentMethod(
            track2=trackData(
                cardAccount='FOOD_STAMP',
                cardType='CBIC',
                encryptedData='159CE98AF9C6B9C2101EECA4CF28CF63FAD5CA2D759461FB',
                ksn='FFFF5678901234E00001',
                pinDetails=pinDetails(
                    dukptPinDetails(
                        pin='51C096C5F32D0E63',
                        pinKsn='FFFF5678901234E00001'
                    )
                )
            )
        )
    )


def test_balance_inquiry_keyedcard():
    response = wn.rest(TERM_ID).balance_inquiry(balance_inquiry_request())
    assert_that(response, instance_of(balanceInquiryResponse))
    assert_that(response.code, equal_to('A'))


def test_balance_inquiry_track2():
    response = wn.rest(TERM_ID).balance_inquiry(balance_inquiry_track2_request())
    assert_that(response, instance_of(balanceInquiryResponse))
    assert_that(response.code, equal_to('A'))

