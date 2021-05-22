import pytest
from hamcrest import assert_that, instance_of, equal_to, is_not

from constants import StoredCredentialTxType, StoredCredentialUse, MpiData, TransactionType
from data.xml_requests import payment_securecard, securecard_registration, securecard_update, credential_on_file, \
    payment, payment_applepay_visa, payment_applepay_mastercard_3ds
from model.gateway import SECURECARDREGISTRATIONRESPONSE, PAYMENTRESPONSE, SECURECARDUPDATERESPONSE, ERROR, \
    CREDENTIALONFILE
from utils import random_text, random_card
from wnclient import WNClient

wn = WNClient().vagrant.go
TERM_ID = '21001'

VISA_DECLINED = '4716568913084649'


@pytest.mark.parametrize("stored_credential_use", StoredCredentialUse)
def test_clear_data_visa_ecommerce_FIRST_TX_payment(stored_credential_use):
    cof_tx_type = StoredCredentialTxType.FIRST_TXN
    p = payment()
    p.CREDENTIALONFILE = credential_on_file()
    p.CREDENTIALONFILE.STOREDCREDENTIALTXTYPE = cof_tx_type.name
    p.CREDENTIALONFILE.STOREDCREDENTIALUSE = stored_credential_use.name
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof.stored_credential_tx_type, equal_to(int(cof_tx_type.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(None))
    assert_that(db_cof.brand_tx_identifier, equal_to(response.CREDENTIALONFILE.BRANDTXIDENTIFIER))
    assert_that(db_cof.stored_credential_use, equal_to(int(stored_credential_use.sid)))


@pytest.mark.parametrize("stored_credential_use", [StoredCredentialUse.UNSCHEDULED])
def test_clear_data_mastercard_ecommerce_FIRST_TX_payment(stored_credential_use):
    cof_tx_type = StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN
    org_brand_tx_id = random_text()
    p = payment(cardtype='mastercard')
    p.CREDENTIALONFILE = credential_on_file()
    p.CREDENTIALONFILE.STOREDCREDENTIALTXTYPE = cof_tx_type.name
    p.CREDENTIALONFILE.STOREDCREDENTIALUSE = stored_credential_use.name
    p.CREDENTIALONFILE.ORIGINALBRANDTXIDENTIFIER = org_brand_tx_id
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof.stored_credential_tx_type, equal_to(int(cof_tx_type.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(org_brand_tx_id))
    assert_that(db_cof.brand_tx_identifier, equal_to(response.CREDENTIALONFILE.BRANDTXIDENTIFIER))
    assert_that(db_cof.stored_credential_use, equal_to(int(stored_credential_use.sid)))


@pytest.mark.parametrize("stored_credential_use", StoredCredentialUse)
def test_clear_data_amex_ecommerce_FIRST_TX_payment(stored_credential_use):
    cof_tx_type = StoredCredentialTxType.FIRST_TXN
    p = payment(cardtype='amex')
    p.CREDENTIALONFILE = credential_on_file()
    p.CREDENTIALONFILE.STOREDCREDENTIALTXTYPE = cof_tx_type.name
    p.CREDENTIALONFILE.STOREDCREDENTIALUSE = stored_credential_use.name
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof.stored_credential_tx_type, equal_to(int(cof_tx_type.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(None))
    assert_that(db_cof.brand_tx_identifier, equal_to(response.CREDENTIALONFILE.BRANDTXIDENTIFIER))
    assert_that(db_cof.stored_credential_use, equal_to(int(stored_credential_use.sid)))


def test_clear_data_ecommerce_CIT_payment():
    cof_tx_type = StoredCredentialTxType.SUBSEQUENT_CARDHOLDER_INITIATED_TXN
    p = payment()
    p.CREDENTIALONFILE = CREDENTIALONFILE(STOREDCREDENTIALTXTYPE=cof_tx_type.name)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.CREDENTIALONFILE, equal_to(None))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof.stored_credential_tx_type, equal_to(int(cof_tx_type.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(None))
    assert_that(db_cof.brand_tx_identifier, is_not(None))
    assert_that(db_cof.stored_credential_use, equal_to(0))


def test_clear_data_ecommerce_MIT_ORIGID_payment():
    org_brand_tx_id = random_text()
    cof_tx_type = StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN
    cof_tx_use = StoredCredentialUse.UNSCHEDULED
    p = payment()
    p.CREDENTIALONFILE = credential_on_file(cof_tx_type.name, cof_tx_use.name)
    p.CREDENTIALONFILE.ORIGINALBRANDTXIDENTIFIER=org_brand_tx_id
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof.stored_credential_tx_type, equal_to(int(cof_tx_type.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(org_brand_tx_id))
    assert_that(db_cof.brand_tx_identifier, equal_to(response.CREDENTIALONFILE.BRANDTXIDENTIFIER))
    assert_that(db_cof.stored_credential_use, equal_to(int(cof_tx_use.sid)))


def test_clear_data_ecommerce_empty_cof_payment():
    p = payment()
    p.CREDENTIALONFILE = CREDENTIALONFILE()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.CREDENTIALONFILE, equal_to(None))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof.stored_credential_tx_type,
                equal_to(int(StoredCredentialTxType.SUBSEQUENT_CARDHOLDER_INITIATED_TXN.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(None))
    assert_that(db_cof.brand_tx_identifier, is_not(None))
    assert_that(db_cof.stored_credential_use, equal_to(0))


def test_clear_data_without_credential_tx_type():
    p = payment()
    p.CREDENTIALONFILE = CREDENTIALONFILE(STOREDCREDENTIALUSE=StoredCredentialUse.UNSCHEDULED.name)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid STOREDCREDENTIALTXTYPE'))


def test_clear_data_without_payment_usage():
    p = payment()
    p.CREDENTIALONFILE = CREDENTIALONFILE(STOREDCREDENTIALTXTYPE=
                                          StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid STOREDCREDENTIALUSE'))


def test_clear_data_ecommerce_MIT_ORIGID_declined_payment():
    p = payment()
    p.CARDNUMBER = VISA_DECLINED
    p.CREDENTIALONFILE = credential_on_file()
    p.CREDENTIALONFILE.ORIGINALBRANDTXIDENTIFIER=random_text()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSETEXT, equal_to('Error'))


@pytest.mark.parametrize('payload', [payment_applepay_visa(), payment_applepay_mastercard_3ds()])
def test_applepay_MIT_ORIGID_payment(payload):
    """Field 62.2 should be equal to ORIGINALBRANDTXIDENTIFIER for VISA and 62.17 for other card types"""
    p = payload
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name,
        STOREDCREDENTIALUSE=StoredCredentialUse.UNSCHEDULED.name,
        ORIGINALBRANDTXIDENTIFIER=random_text()
    )
    response = wn.xml(terminal_id=TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_visa_3ds_payment_mpiref():
    # TODO use xml request to get mpiref
    p = payment(cardtype='visa')
    p.TRANSACTIONTYPE = TransactionType.THREE_DS
    p.MPIREF = MpiData.FIRST.mpiref
    p.CREDENTIALONFILE = credential_on_file(
        stored_credential_tx_type=StoredCredentialTxType.FIRST_TXN.name,
        stored_credential_use=StoredCredentialUse.INSTALLMENT.name
    )
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    db_txn = wn.db(terminal_number=TERM_ID).get_transaction(uniqueref=response.UNIQUEREF)
    assert_that(db_txn.commercetype, equal_to(str(TransactionType.THREE_DS)))


def test_visa_3ds_payment_xid_cavv():
    p = payment(cardtype='visa')
    p.TRANSACTIONTYPE = 6
    p.CAVV = MpiData.FIRST.cavv
    p.XID = MpiData.FIRST.xid
    p.CREDENTIALONFILE = credential_on_file(
        stored_credential_tx_type=StoredCredentialTxType.FIRST_TXN.name,
        stored_credential_use=StoredCredentialUse.INSTALLMENT.name
    )
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
