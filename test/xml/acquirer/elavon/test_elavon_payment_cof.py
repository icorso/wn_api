import random

import pytest
from hamcrest import assert_that, instance_of, is_not, has_property, equal_to, is_

from constants import StoredCredentialTxType, StoredCredentialUse, MpiData, TransactionType
from data.xml_requests import payment, credential_on_file, preauth
from model.gateway import PAYMENTRESPONSE, CREDENTIALONFILE, PREAUTHRESPONSE
from utils import random_text
from wnclient import WNClient

wn = WNClient().local.wn
TERM_ID = '20001'
VISA_CARDS = ['4658074914430378', '4491954376604191', '4305505400565786', '4783947410989336']
VISA_EDCC = ['4508017074013288']
VISA_CARDS_DECLINE = ['4183117674880086', '4183117674880086', '4674455190097140']
MC_CARDS_DECLINE = ['5203138256373970']  # Expiry date 03 2020 leads to failed CVV validation


@pytest.mark.parametrize('stored_credential_use', StoredCredentialUse)
def test_elavon_ecomm_cof_first_txn_visa_payment(stored_credential_use):
    stored_tx_type = StoredCredentialTxType.FIRST_TXN
    p = payment()
    p.CARDNUMBER = random.choice(VISA_CARDS)
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALUSE=stored_credential_use.name,
        STOREDCREDENTIALTXTYPE=stored_tx_type.name
    )
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof.stored_credential_tx_type, equal_to(int(stored_tx_type.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(None))
    assert_that(db_cof.brand_tx_identifier, equal_to(response.CREDENTIALONFILE.BRANDTXIDENTIFIER))
    assert_that(db_cof.stored_credential_use, equal_to(int(stored_credential_use.sid)))


def test_elavon_ecomm_cof_CIT_visa_payment():
    cit = StoredCredentialTxType.SUBSEQUENT_CARDHOLDER_INITIATED_TXN
    p = payment()
    p.CARDNUMBER = random.choice(VISA_CARDS)
    p.CREDENTIALONFILE = CREDENTIALONFILE(STOREDCREDENTIALTXTYPE=cit.name)

    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response, has_property('CREDENTIALONFILE', is_(None)))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof.stored_credential_tx_type, equal_to(int(cit.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(None))
    assert_that(db_cof.brand_tx_identifier, is_not(None))
    assert_that(db_cof.stored_credential_use, equal_to(0))


def test_elavon_cof_CIT_visa_preauth():
    cof_tx_use = StoredCredentialUse.UNSCHEDULED
    cof_tx_type = StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN
    cof_org_tx_id = random_text(11)
    p = preauth()
    p.CARDNUMBER = random.choice(VISA_CARDS)
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        ORIGINALBRANDTXIDENTIFIER=cof_org_tx_id,  # length should be exactly 11 symbols
        STOREDCREDENTIALUSE=cof_tx_use.name,
        STOREDCREDENTIALTXTYPE=cof_tx_type.name
    )

    response = wn.xml(TERM_ID).preauth(p)
    assert_that(response, instance_of(PREAUTHRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof.stored_credential_tx_type, equal_to(int(cof_tx_type.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(cof_org_tx_id))
    assert_that(db_cof.brand_tx_identifier, equal_to(response.CREDENTIALONFILE.BRANDTXIDENTIFIER))
    assert_that(db_cof.stored_credential_use, equal_to(int(cof_tx_use.sid)))


def test_elavon_ecomm_cof_MIT_UNSC_visa_payment():
    cof_tx_use = StoredCredentialUse.UNSCHEDULED
    cof_tx_type = StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN
    cof_org_tx_id = random_text(11)
    p = payment()
    p.CARDNUMBER = random.choice(VISA_CARDS)
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        ORIGINALBRANDTXIDENTIFIER=cof_org_tx_id,  # length should be exactly 11 symbols
        STOREDCREDENTIALUSE=cof_tx_use.name,
        STOREDCREDENTIALTXTYPE=cof_tx_type.name
    )

    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof.stored_credential_tx_type, equal_to(int(cof_tx_type.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(cof_org_tx_id))
    assert_that(db_cof.brand_tx_identifier, equal_to(response.CREDENTIALONFILE.BRANDTXIDENTIFIER))
    assert_that(db_cof.stored_credential_use, equal_to(int(cof_tx_use.sid)))


def test_elavon_ecomm_no_cof_visa_payment():
    p = payment()
    p.CARDNUMBER = random.choice(VISA_CARDS)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response, has_property('CREDENTIALONFILE', is_(None)))
    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof, equal_to(None))


def test_elavon_cof_visa_declined_payment():
    cof_use = StoredCredentialUse.UNSCHEDULED
    cof_tx_type = StoredCredentialTxType.FIRST_TXN
    p = payment()
    p.CARDNUMBER = random.choice(VISA_CARDS)
    p.CARDEXPIRY = '0223'
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALUSE=cof_use.name,
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.FIRST_TXN.name
    )
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof.stored_credential_tx_type, equal_to(int(cof_tx_type.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(None))
    assert_that(db_cof.brand_tx_identifier, equal_to(response.CREDENTIALONFILE.BRANDTXIDENTIFIER))
    assert_that(db_cof.stored_credential_use, equal_to(int(cof_use.sid)))


def test_elavon_3ds_payment_xid_cavv():
    p = payment()
    p.TRANSACTIONTYPE = TransactionType.THREE_DS
    p.CAVV = MpiData.FIRST.cavv
    p.XID = MpiData.FIRST.xid
    p.CREDENTIALONFILE = credential_on_file(
        stored_credential_tx_type=StoredCredentialTxType.FIRST_TXN.name,
        stored_credential_use=StoredCredentialUse.INSTALLMENT.name
    )
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    # Sending request to Gate : ...<XID>MpiData.FIRST.xid</XID> should be in the logs


# MPI order ID: HPP69371 Unexpected error: TPSEJBException: mpi.wrongorderid
# def test_elavon_3ds_payment_mpiref():
#     p = payment()
#     p.TRANSACTIONTYPE = TransactionType.THREE_DS
#     p.MPIREF = MpiData.FIRST.mpiref
#     p.CREDENTIALONFILE = credential_on_file(
#         stored_credential_tx_type=StoredCredentialTxType.FIRST_TXN.name,
#         stored_credential_use=StoredCredentialUse.INSTALLMENT.name
#     )
#     response = wn.xml(terminal_id=TERM_ID).payment(request=p)
#     assert_that(response, instance_of(PAYMENTRESPONSE))
