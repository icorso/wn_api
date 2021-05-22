from faker import Factory
from hamcrest import assert_that, instance_of

from data.xml_requests import securecard_registration, payment_securecard, payment, payment_avs, payment_chp
from model.gateway import PAYMENTRESPONSE, SECURECARDREGISTRATIONRESPONSE
from wnclient import WNClient

fake = Factory.create()

'''
Supports VISA and MasterCard only
No AVS and CVV
'''

wn = WNClient().local.go
TERM_ID = '21009'
CARD_NUM = '4761739001010440'


def test_flapws_securecard_payment_ok():
    securecard = securecard_registration(cardtype='mastercard')
    # securecard.CARDNUMBER = CARD_NUM

    sc_response = wn.xml(TERM_ID).secure_card_registration(securecard)
    assert_that(sc_response, instance_of(SECURECARDREGISTRATIONRESPONSE))

    response = wn.xml(TERM_ID).payment(payment_securecard(cardreference=sc_response.CARDREFERENCE))
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_flapws_keyed_payment_ok():
    request = payment(cardtype='visa', cvv=None)
    request.CARDNUMBER = CARD_NUM
    request.ORDERID = str(fake.random_number(7, True))
    request.AUTOREADY = 'C'
    request.ISSUENO = str(fake.random_number(2, True))  # issue #19267

    response = wn.xml(TERM_ID).payment(request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
