from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import payment_securecard
from model.gateway import SECURECARDREGISTRATIONRESPONSE, PAYMENTRESPONSE, ERROR
from wnclient import WNClient

wn = WNClient().vagrant.go
TERM_ID = '21001'


def test_securecard_payment():
    secure_card = wn.xml(TERM_ID).secure_card_registration()
    assert_that(secure_card, instance_of(SECURECARDREGISTRATIONRESPONSE))

    response = wn.xml(TERM_ID).payment(payment_securecard(cardreference=secure_card.CARDREFERENCE))
    assert_that(response, instance_of(PAYMENTRESPONSE))

    wn.xml(TERM_ID).secure_card_removal(secure_card.MERCHANTREF, secure_card.CARDREFERENCE)


def test_securecard_reference_number_space_payment():
    secure_card = wn.xml(TERM_ID).secure_card_registration()
    assert_that(secure_card, instance_of(SECURECARDREGISTRATIONRESPONSE))

    response = wn.xml(TERM_ID).payment(payment_securecard(cardreference='    ' + secure_card.CARDREFERENCE + '    '))
    assert_that(response, instance_of(PAYMENTRESPONSE))

    wn.xml(TERM_ID).secure_card_removal(secure_card.MERCHANTREF, secure_card.CARDREFERENCE)


def test_securecard_incorrect_ref_payment():
    secure_card = wn.xml(TERM_ID).secure_card_registration()
    assert_that(secure_card, instance_of(SECURECARDREGISTRATIONRESPONSE))
    response = wn.xml(TERM_ID).payment(payment_securecard(cardreference=secure_card.CARDREFERENCE + '000000000000000000000000'))
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid CARDNUMBER field'))


def test_securecard_empty_ref_payment():
    secure_card = wn.xml(TERM_ID).secure_card_registration()
    assert_that(secure_card, instance_of(SECURECARDREGISTRATIONRESPONSE))
    response = wn.xml(TERM_ID).payment(payment_securecard(cardreference='          '))
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid CARDNUMBER field'))
