from random import randrange

import pytest
from faker import Factory
from hamcrest import assert_that, instance_of

from constants import SecureCard, CashFlowsSecureCard, StoredCredentialTxType
from data.xml_requests import payment_securecard, securecard_registration, credential_on_file
from model.gateway import SECURECARDREGISTRATION, SECURECARDREGISTRATIONRESPONSE
from utils import random_card, today, random_text
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go


def sc_reg(mref, cvv=''):
        creditcard = random_card()
        cvv = creditcard.cvv if not cvv else cvv
        return SECURECARDREGISTRATION(
            MERCHANTREF=mref,
            DATETIME=str(today()),
            CARDNUMBER=creditcard.cardnumber,
            CARDEXPIRY=creditcard.cardexpiry,
            CARDTYPE=creditcard.cardtype,
            CARDHOLDERNAME=creditcard.cardholder,
            CVV=cvv,
            POSTCODE=fake.postcode(),
            PHONE=fake.msisdn(),
            EMAIL=fake.free_email(),
        )


def test_bulk_securecard_registration():
    for i in range(50):  # terminals
        term_num = 21024 + i
        for c in range(100):  # securecards
            sc = sc_reg(mref=str(term_num) + str(c))
            sc.without_field('CVV')
            wn.xml(str(term_num)).secure_card_registration(request=sc)


def test_bulk_random_securecard_payment():
    counter = 0
    settle_txn_counter = 700
    for i in range(2000):
        terminal = str(21024 + randrange(50))
        sc = terminal + str(randrange(0, 100))
        cardref = wn.xml(terminal).secure_card_search(sc).CARDREFERENCE
        payment_request = payment_securecard(cardref)
        payment_request.ORDERID = random_text(15)
        wn.xml(terminal).payment(request=payment_request)
        if counter == settle_txn_counter:
            for j in range(50):
                WNClient().local.go.http.test_settle(params={'terminal_id': str(21024 + j)})
                print('Settlement started after ' + str(i) + ' transactions.')
            counter = 0
        counter += 1


def test_settle_txns():
    for j in range(50):
        WNClient().local.go.http.test_settle(params={'terminal_id': str(21024 + j)})


@pytest.mark.parametrize('sc', SecureCard)
def test_predefined_securecards_registration(sc):
    terminal_number = '22001'
    wn = WNClient().vagrant.wn

    request = securecard_registration(cvv='999')
    request.TERMINALID = terminal_number
    request.CARDNUMBER = sc.cardnumber
    request.MERCHANTREF = sc.merchant_ref
    request.CARDHOLDERNAME = sc.cardholdername
    request.PHONE = sc.phone
    request.EMAIL = sc.email

    response = wn.xml(terminal_number).secure_card_registration(request=request)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


@pytest.mark.parametrize('sc', CashFlowsSecureCard)
def test_cof_securecards_registration(sc):
    terminal_number = '22001'
    wn = WNClient().vagrant.wn

    request = securecard_registration(cvv='999')
    request.TERMINALID = terminal_number
    request.CARDNUMBER = sc.cardnumber
    request.MERCHANTREF = sc.merchant_ref
    request.CREDENTIALONFILE = credential_on_file()
    request.CREDENTIALONFILE.STOREDCREDENTIALTXTYPE = StoredCredentialTxType.FIRST_TXN.name
    request.CREDENTIALONFILE.STOREDCREDENTIALUSE = sc.cof_use.name

    response = wn.xml(terminal_number).secure_card_registration(request=request)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))
