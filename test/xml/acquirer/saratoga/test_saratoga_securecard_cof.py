from hamcrest import assert_that, instance_of, is_not, has_property

from constants import StoredCredentialTxType, StoredCredentialUse, TransactionType
from data.xml_requests import securecard_registration, credential_on_file, securecard_update, payment_securecard
from model.gateway import SECURECARDREGISTRATIONRESPONSE, CREDENTIALONFILE, SECURECARDUPDATERESPONSE, PAYMENTRESPONSE
from wnclient import WNClient

wn = WNClient().vagrant.go
TERM_ID = '21001'


def test_saratoga_securecard_registration_cof():
    sc = securecard_registration()
    sc.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.FIRST_TXN.name,
        STOREDCREDENTIALUSE=StoredCredentialUse.UNSCHEDULED.name
    )

    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))
    assert_that(response.CREDENTIALONFILE, has_property('BRANDTXIDENTIFIER', is_not(None)))


def test_securecard_cardnumber_update_stored_credential_use():
    cvv = '999'
    cardnumber = '4372281658205446'
    sc = securecard_registration(cvv=cvv)
    sc.CARDNUMBER = cardnumber
    sc.CREDENTIALONFILE = credential_on_file(stored_credential_use=StoredCredentialUse.INSTALLMENT.name,
                                             stored_credential_tx_type=StoredCredentialTxType.FIRST_TXN.name)
    securecard_create_response = wn.xml(TERM_ID).secure_card_registration(request=sc)

    securecard_update_request = securecard_update(securecard_create_response.MERCHANTREF, cvv=cvv)
    securecard_update_request.CARDNUMBER = cardnumber
    securecard_update_request.CREDENTIALONFILE = credential_on_file(
        stored_credential_use=StoredCredentialUse.RECURRING.name,
        stored_credential_tx_type=StoredCredentialTxType.FIRST_TXN.name)
    response = wn.xml(TERM_ID).secure_card_update(request=securecard_update_request)
    assert_that(response, instance_of(SECURECARDUPDATERESPONSE))


def test_securecard_cardholder_payment_cof():
    secure_card = wn.xml(TERM_ID).secure_card_registration()
    assert_that(secure_card, instance_of(SECURECARDREGISTRATIONRESPONSE))

    payment_request = payment_securecard(cardreference=secure_card.CARDREFERENCE)
    payment_request.CREDENTIALONFILE = credential_on_file(
        stored_credential_use=None,
        stored_credential_tx_type=StoredCredentialTxType.SUBSEQUENT_CARDHOLDER_INITIATED_TXN.name)
    payment_request.without_field('STOREDCREDENTIALUSE')
    response = wn.xml(TERM_ID).payment(request=payment_request)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_securecard_recurring_payment_cof():
    secure_card = wn.xml(TERM_ID).secure_card_registration()
    assert_that(secure_card, instance_of(SECURECARDREGISTRATIONRESPONSE))

    payment_request = payment_securecard(cardreference=secure_card.CARDREFERENCE)
    payment_request.CREDENTIALONFILE = credential_on_file(
        stored_credential_use=StoredCredentialUse.RECURRING.name,
        stored_credential_tx_type=StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name)
    payment_request.TRANSACTIONTYPE = TransactionType.RECURRING

    payment_request.without_field('STOREDCREDENTIALUSE')
    response = wn.xml(TERM_ID).payment(request=payment_request)
    assert_that(response, instance_of(PAYMENTRESPONSE))

