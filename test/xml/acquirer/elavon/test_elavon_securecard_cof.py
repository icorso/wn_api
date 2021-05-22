import random

import pytest
from hamcrest import assert_that, instance_of, is_not, has_property, equal_to, is_

from constants import StoredCredentialTxType, CashFlowsSecureCard, Currency, TransactionType, \
    StoredCredentialUse, CashFlowsNoCofSecureCard, MpiData
from data.xml_requests import securecard_registration, credential_on_file, \
    subscription, payment_subscription, stored_subscription, payment_securecard, payment
from model.gateway import SECURECARDREGISTRATIONRESPONSE, ADDSUBSCRIPTIONRESPONSE, SUBSCRIPTIONPAYMENTRESPONSE, \
    ADDSTOREDSUBSCRIPTIONRESPONSE, PAYMENTRESPONSE, CREDENTIALONFILE, ERROR
from wnclient import WNClient

wn = WNClient().local.wn
TERM_ID = '20001'
VISA_CARDS = ['4658074914430378', '4491954376604191', '4305505400565786', '4783947410989336']


@pytest.mark.parametrize('merchant_ref, name, length', {
    ('ss_limited', 'Limited stored subscription', 3),
    ('ss_unlimited', 'Unlimited stored subscription', 0),
    ('ss_limited_before_cof', 'Limited stored subscription before CoF', 3),
    ('ss_unlimited_before_cof', 'Unlimited stored subscription before CoF', 0),
})
def test_add_stored_subscriptions(merchant_ref, name, length):
    ss = stored_subscription()
    ss.MERCHANTREF = merchant_ref
    ss.NAME = name
    ss.LENGTH = length
    response = wn.xml(TERM_ID).add_stored_subscription(request=ss, currency=Currency.USD)
    assert_that(response, instance_of(ADDSTOREDSUBSCRIPTIONRESPONSE))


@pytest.mark.parametrize('card', CashFlowsSecureCard)
def test_elavon_securecard_registration(card):
    sc = securecard_registration(cvv=card.cvv)
    sc.CREDENTIALONFILE = credential_on_file()
    sc.CREDENTIALONFILE.STOREDCREDENTIALTXTYPE = StoredCredentialTxType.FIRST_TXN.name
    sc.CREDENTIALONFILE.STOREDCREDENTIALUSE = card.cof_use.name
    sc.CARDNUMBER = card.cardnumber
    sc.MERCHANTREF = card.merchant_ref
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))
    assert_that(response.CREDENTIALONFILE, has_property('BRANDTXIDENTIFIER', is_not(None)))

    sc_additional_settings = wn.db(terminal_number=TERM_ID).get_secure_card_additional_settings(response.MERCHANTREF)
    assert_that(sc_additional_settings.stored_credential_use, card.cof_use)


def test_elavon_declined_securecard_registration():
    sc = securecard_registration()
    sc.CARDNUMBER = '4403938589512199'
    sc.CVV = '486'
    sc.CARDEXPIRY = '0421'
    sc.CREDENTIALONFILE = credential_on_file()
    sc.CREDENTIALONFILE.STOREDCREDENTIALTXTYPE = StoredCredentialTxType.FIRST_TXN.name
    sc.CREDENTIALONFILE.STOREDCREDENTIALUSE = StoredCredentialUse.UNSCHEDULED.name
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('INVALID SECURITY FIELD'))


def test_elavon_xid_3ds_securecard_registration():
    sc = securecard_registration()
    sc.TRANSACTIONTYPE = TransactionType.THREE_DS
    sc.CARDNUMBER = random.choice(VISA_CARDS)
    sc.CAVV = MpiData.FIRST.cavv
    sc.XID = MpiData.FIRST.xid
    sc.CREDENTIALONFILE = credential_on_file()
    sc.CREDENTIALONFILE.STOREDCREDENTIALTXTYPE = StoredCredentialTxType.FIRST_TXN.name
    sc.CREDENTIALONFILE.STOREDCREDENTIALUSE = StoredCredentialUse.UNSCHEDULED.name
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


def test_elavon_mpiref_3ds_securecard_registration():
    sc = securecard_registration()
    sc.TRANSACTIONTYPE = TransactionType.THREE_DS
    sc.CARDNUMBER = random.choice(VISA_CARDS)
    sc.MPIREF = MpiData.FIRST.mpiref
    sc.CREDENTIALONFILE = credential_on_file()
    sc.CREDENTIALONFILE.STOREDCREDENTIALTXTYPE = StoredCredentialTxType.FIRST_TXN.name
    sc.CREDENTIALONFILE.STOREDCREDENTIALUSE = StoredCredentialUse.UNSCHEDULED.name
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


def test_elavon_no_cof_securecard_registration():
    sc = securecard_registration()
    sc.CARDEXPIRY = '1023'
    sc.CVV = '999'
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))
    assert_that(response, has_property('CREDENTIALONFILE', is_(None)))


@pytest.mark.parametrize('sc', [
        CashFlowsSecureCard.VISA_UNSC,
        CashFlowsSecureCard.VISA_INST,
        CashFlowsSecureCard.VISA_SUBS
])
def test_elavon_securecard_payment_ecommerce_CIT(sc):
    search_response = wn.xml(TERM_ID).secure_card_search(sc.merchant_ref)

    p = payment_securecard(cardreference=search_response.CARDREFERENCE)
    p.CREDENTIALONFILE = CREDENTIALONFILE(STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_CARDHOLDER_INITIATED_TXN.name)
    response = wn.xml(TERM_ID).payment(p)

    # DEFAULT values have been set for CoF VO - transactionType=2
    # CoF=<CREDENTIALONFILE>
    # <ORIGINALBRANDTXIDENTIFIER>sc_verif_tx_id</ORIGINALBRANDTXIDENTIFIER>
    # <STOREDCREDENTIALTXTYPE>SUBSEQUENT_MERCHANT_INITIATED_TXN</STOREDCREDENTIALTXTYPE>
    # <STOREDCREDENTIALUSE>RECURRING</STOREDCREDENTIALUSE></CREDENTIALONFILE>

    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    sc_verif_tx_id = wn.db(terminal_number=TERM_ID).get_secure_card_additional_settings(sc.merchant_ref).verification_txn_id
    assert_that(db_cof.stored_credential_tx_type, equal_to(int(StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(sc_verif_tx_id))
    assert_that(db_cof.brand_tx_identifier, equal_to(response.CREDENTIALONFILE.BRANDTXIDENTIFIER))
    assert_that(db_cof.stored_credential_use, equal_to(int(StoredCredentialUse.RECURRING.sid)))


@pytest.mark.parametrize('stored_credential_use', StoredCredentialUse)
def test_elavon_ecomm_cof_unscheduled_visa_payment(stored_credential_use):
    sct = StoredCredentialTxType.FIRST_TXN
    p = payment()
    p.CARDNUMBER = CashFlowsSecureCard.VISA_UNSC.cardnumber
    p.CVV = CashFlowsSecureCard.VISA_UNSC.cvv
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALUSE=stored_credential_use.name,
        STOREDCREDENTIALTXTYPE=sct.name
    )
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)
    assert_that(db_cof.stored_credential_tx_type, equal_to(int(sct.sid)))
    assert_that(db_cof.brand_tx_identifier, equal_to(response.CREDENTIALONFILE.BRANDTXIDENTIFIER))
    assert_that(db_cof.stored_credential_use, equal_to(int(stored_credential_use.sid)))


@pytest.mark.parametrize('card', CashFlowsSecureCard)
def test_elavon_securecard_payment_recurring_MIT(card):
    search_response = wn.xml(TERM_ID).secure_card_search(card.merchant_ref)

    p = payment_securecard(cardreference=search_response.CARDREFERENCE)
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name,
        STOREDCREDENTIALUSE=StoredCredentialUse.RECURRING.name
    )
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))

    sc_verif_tx_id = wn.db(terminal_number=TERM_ID).get_secure_card_additional_settings(card.merchant_ref).verification_txn_id
    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)

    assert_that(db_cof.stored_credential_tx_type, equal_to(int(StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(sc_verif_tx_id))
    assert_that(db_cof.brand_tx_identifier, equal_to(response.CREDENTIALONFILE.BRANDTXIDENTIFIER))
    assert_that(db_cof.stored_credential_use, equal_to(int(StoredCredentialUse.RECURRING.sid)))


@pytest.mark.parametrize('card', CashFlowsNoCofSecureCard)
def test_elavon_no_cof_securecard_payment_recurring_MIT(card):
    search_response = wn.xml(TERM_ID).secure_card_search(card.merchant_ref)

    p = payment_securecard(cardreference=search_response.CARDREFERENCE)
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        ORIGINALBRANDTXIDENTIFIER='4958209358290384',
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name,
        STOREDCREDENTIALUSE=StoredCredentialUse.RECURRING.name
    )
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))


@pytest.mark.parametrize('card', CashFlowsSecureCard)
def test_elavon_securecard_payment_installment_MIT(card):
    search_response = wn.xml(TERM_ID).secure_card_search(card.merchant_ref)

    p = payment_securecard(cardreference=search_response.CARDREFERENCE)
    p.TRANSACTIONTYPE = TransactionType.INSTALLMENT
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name,
        STOREDCREDENTIALUSE=StoredCredentialUse.INSTALLMENT.name
    )
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))

    sc_verif_tx_id = wn.db(terminal_number=TERM_ID).get_secure_card_additional_settings(card.merchant_ref).verification_txn_id
    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=response.UNIQUEREF)

    assert_that(db_cof.stored_credential_tx_type, equal_to(int(StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(sc_verif_tx_id))
    assert_that(db_cof.brand_tx_identifier, equal_to(response.CREDENTIALONFILE.BRANDTXIDENTIFIER))
    assert_that(db_cof.stored_credential_use, equal_to(int(StoredCredentialUse.RECURRING.sid)))


@pytest.mark.parametrize('card', CashFlowsNoCofSecureCard)
def test_elavon_no_cof_securecard_payment_installment_MIT(card):
    search_response = wn.xml(TERM_ID).secure_card_search(card.merchant_ref)

    p = payment_securecard(cardreference=search_response.CARDREFERENCE)
    p.TRANSACTIONTYPE = TransactionType.INSTALLMENT
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name,
        STOREDCREDENTIALUSE=StoredCredentialUse.INSTALLMENT.name
    )
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))


@pytest.mark.parametrize('ss_merchant_ref, sc, cof_use_id', {
    ('ss_limited', CashFlowsSecureCard.VISA_UNSC, StoredCredentialUse.INSTALLMENT.sid),
    ('ss_limited', CashFlowsSecureCard.VISA_INST, StoredCredentialUse.INSTALLMENT.sid),
    ('ss_limited', CashFlowsSecureCard.VISA_SUBS, StoredCredentialUse.INSTALLMENT.sid),
    ('ss_unlimited', CashFlowsSecureCard.VISA_UNSC, StoredCredentialUse.RECURRING.sid),
    ('ss_unlimited', CashFlowsSecureCard.VISA_INST, StoredCredentialUse.RECURRING.sid),
    ('ss_unlimited', CashFlowsSecureCard.VISA_SUBS, StoredCredentialUse.RECURRING.sid),
})
def test_elavon_subscription_payment(ss_merchant_ref, sc, cof_use_id):
    s = subscription(stored_subscriptionref=ss_merchant_ref)
    s.MERCHANTREF = '%s_%s' % (ss_merchant_ref, sc.merchant_ref)
    s.SECURECARDMERCHANTREF = sc.merchant_ref
    subscription_response = wn.xml(TERM_ID).add_subscription(request=s)
    assert_that(subscription_response, instance_of(ADDSUBSCRIPTIONRESPONSE))

    sc_verif_tx_id = wn.db().get_secure_card_additional_settings(sc.merchant_ref).verification_txn_id
    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(
        description='Automatic set-up payment for subscription: %s' % s.MERCHANTREF)

    assert_that(db_cof.stored_credential_tx_type, equal_to(int(StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.sid)))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(sc_verif_tx_id))
    assert_that(db_cof.stored_credential_use, equal_to(int(cof_use_id)))

    sp = payment_subscription(s.MERCHANTREF)
    subscription_payment_response = wn.xml(TERM_ID).subscription_payment(request=sp, currency=Currency.USD)
    assert_that(subscription_payment_response, instance_of(SUBSCRIPTIONPAYMENTRESPONSE))

    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=subscription_payment_response.UNIQUEREF)

    assert_that(db_cof.stored_credential_tx_type, equal_to(int(StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.sid)))
    assert_that(db_cof.brand_tx_identifier, is_not(None))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(sc_verif_tx_id))
    assert_that(db_cof.stored_credential_use, equal_to(int(cof_use_id)))


@pytest.mark.parametrize('ss_merchant_ref, sc', {
    ('ss_limited_before_cof', CashFlowsNoCofSecureCard.VISA_NO_COF),
    ('ss_unlimited_before_cof', CashFlowsNoCofSecureCard.VISA_NO_COF),
    ('ss_limited_before_cof', CashFlowsNoCofSecureCard.MC_NO_COF),
    ('ss_unlimited_before_cof', CashFlowsNoCofSecureCard.MC_NO_COF)
})
def test_elavon_before_cof_subscription_registration(ss_merchant_ref, sc):
    # UPDATE `acquirer` SET `supports_cof`='0' WHERE `id`='1';
    # Disable elavon cof pilot feature and clear app cache
    s = subscription(stored_subscriptionref=ss_merchant_ref)
    s.MERCHANTREF = '%s_%s' % (ss_merchant_ref, sc.merchant_ref)
    s.SECURECARDMERCHANTREF = sc.merchant_ref
    subscription_response = wn.xml(TERM_ID).add_subscription(request=s)
    assert_that(subscription_response, instance_of(ADDSUBSCRIPTIONRESPONSE))


@pytest.mark.parametrize('ss_merchant_ref, sc, cof_use_id', {
    ('ss_limited_before_cof', CashFlowsNoCofSecureCard.VISA_NO_COF, StoredCredentialUse.INSTALLMENT.sid),
    ('ss_unlimited_before_cof', CashFlowsNoCofSecureCard.VISA_NO_COF, StoredCredentialUse.RECURRING.sid),
    ('ss_limited_before_cof', CashFlowsNoCofSecureCard.MC_NO_COF, StoredCredentialUse.INSTALLMENT.sid),
    ('ss_unlimited_before_cof', CashFlowsNoCofSecureCard.MC_NO_COF, StoredCredentialUse.RECURRING.sid)
})
def test_elavon_before_cof_subscription_payment(ss_merchant_ref, sc, cof_use_id):
    # UPDATE `acquirer` SET `supports_cof`='1' WHERE `id`='1';
    # Enable elavon cof pilot feature and clear app cache
    subscription_merchantref = '%s_%s' % (ss_merchant_ref, sc.merchant_ref)

    sp = payment_subscription(subscription_merchantref)
    subscription_payment_response = wn.xml(TERM_ID).subscription_payment(request=sp, currency=Currency.USD)
    assert_that(subscription_payment_response, instance_of(SUBSCRIPTIONPAYMENTRESPONSE))

    sc_verif_tx_id = wn.db().get_secure_card_additional_settings(sc.merchant_ref).verification_txn_id
    db_cof = wn.db(terminal_number=TERM_ID).get_transaction_cof_details(uniqueref=subscription_payment_response.UNIQUEREF)

    assert_that(db_cof.stored_credential_tx_type, equal_to(int(StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.sid)))
    assert_that(db_cof.brand_tx_identifier, is_not(None))
    assert_that(db_cof.original_brand_tx_identifier, equal_to(sc_verif_tx_id))
    assert_that(db_cof.stored_credential_use, equal_to(int(cof_use_id)))
