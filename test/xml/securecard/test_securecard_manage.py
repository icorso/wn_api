import random

import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import securecard_registration, securecard_update
from model.gateway import SECURECARDREGISTRATIONRESPONSE, SECURECARDUPDATERESPONSE, ERROR, CUSTOMFIELD
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21001'


def test_securecard_registration_ok():
    sc = securecard_registration(cardtype='visa', cvv='999')
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))
    assert_that(response.generate_hash(), equal_to(response.HASH))


def test_securecard_registration_custom_field():
    sc = securecard_registration(cardtype=random.choice(['visa', 'mastercard', 'amex']), cvv='999')
    sc.CUSTOMFIELD = [CUSTOMFIELD(NAME='CustomString101', valueOf_=fake.text(20))]
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))
    assert_that(response.generate_hash(), equal_to(response.HASH))


@pytest.mark.parametrize('expiry_date', ['aaaa', '0000', '9999', '0022', '1321'])  # 'MMYY' 0419
def test_securecard_registration_invalid_expiry_date(expiry_date):
    sc = securecard_registration(cvv='999')
    sc.CARDEXPIRY = expiry_date
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('INVALID CARDEXPIRY'))


def test_securecard_registration_past_expiry_date():
    sc = securecard_registration(cvv='999')
    sc.CARDEXPIRY = '1219'
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


def test_securecard_cardnumber_update_ok():
    cvv = '999'
    sc = securecard_registration(cvv=cvv)
    securecard_create_response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    securecard_update_request = securecard_update(securecard_create_response.MERCHANTREF, cardtype='mastercard', cvv=cvv)

    response = wn.xml(TERM_ID).secure_card_update(request=securecard_update_request)
    assert_that(response, instance_of(SECURECARDUPDATERESPONSE))


def test_securecard_partial_update_ok():
    sc_create_request = securecard_registration()
    sc_create_response = wn.xml(TERM_ID).secure_card_registration(request=sc_create_request)

    sc_update_request = securecard_update(sc_create_response.MERCHANTREF)
    sc_update_request.CARDNUMBER = sc_create_request.CARDNUMBER
    sc_update_request.CARDTYPE = sc_create_request.CARDTYPE

    response = wn.xml(TERM_ID).secure_card_update(request=sc_update_request)
    assert_that(response, instance_of(SECURECARDUPDATERESPONSE))


def test_securecard_removal():
    secure_card = wn.xml(TERM_ID).secure_card_registration(request=securecard_registration())
    assert_that(secure_card, instance_of(SECURECARDREGISTRATIONRESPONSE))
    assert_that(secure_card.generate_hash(), equal_to(secure_card.HASH))

    secure_card_removal_response = wn.xml(TERM_ID).secure_card_removal(secure_card.MERCHANTREF, secure_card.CARDREFERENCE)
    assert_that(secure_card_removal_response.generate_hash(), equal_to(secure_card_removal_response.HASH))
