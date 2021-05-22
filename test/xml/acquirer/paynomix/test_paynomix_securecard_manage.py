from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import PaynomixCard
from data.xml_requests import securecard_registration, securecard_update
from model.gateway import SECURECARDREGISTRATIONRESPONSE, SECURECARDUPDATERESPONSE, CUSTOMFIELD
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22015'


def test_securecard_registration_ok():
    sc = securecard_registration()
    sc.CARDNUMBER = PaynomixCard.rand().cardnumber
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))
    assert_that(response.generate_hash(), equal_to(response.HASH))


def test_securecard_registration_custom_field():
    sc = securecard_registration()
    sc.CARDNUMBER = PaynomixCard.rand().cardnumber
    sc.CUSTOMFIELD = [CUSTOMFIELD(NAME='CustomStringSC', valueOf_=fake.text(20))]
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))
    assert_that(response.generate_hash(), equal_to(response.HASH))


def test_securecard_cardnumber_update_ok():
    sc = securecard_registration()
    sc.CARDNUMBER = PaynomixCard.VISA.cardnumber
    securecard_create_response = wn.xml(TERM_ID).secure_card_registration(request=sc)

    securecard_update_request = securecard_update(securecard_create_response.MERCHANTREF, cardtype='mastercard')
    securecard_update_request.CARDNUMBER = PaynomixCard.MASTERCARD.cardnumber

    response = wn.xml(TERM_ID).secure_card_update(request=securecard_update_request)
    assert_that(response, instance_of(SECURECARDUPDATERESPONSE))


def test_securecard_removal():
    sc = securecard_registration()
    sc.CARDNUMBER = PaynomixCard.rand().cardnumber

    secure_card = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(secure_card, instance_of(SECURECARDREGISTRATIONRESPONSE))
    assert_that(secure_card.generate_hash(), equal_to(secure_card.HASH))

    secure_card_removal_response = wn.xml(TERM_ID).secure_card_removal(secure_card.MERCHANTREF, secure_card.CARDREFERENCE)
    assert_that(secure_card_removal_response.generate_hash(), equal_to(secure_card_removal_response.HASH))
