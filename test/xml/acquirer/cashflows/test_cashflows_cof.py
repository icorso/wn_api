import pytest
from hamcrest import assert_that, instance_of, is_not, has_property, equal_to, is_

from constants import StoredCredentialTxType, CashFlowsSecureCard, Currency, TerminalType, TransactionType, \
    StoredCredentialUse
from data.xml_requests import securecard_registration, credential_on_file, \
    subscription, payment_subscription, stored_subscription, payment_securecard, payment
from model.gateway import SECURECARDREGISTRATIONRESPONSE, ADDSUBSCRIPTIONRESPONSE, SUBSCRIPTIONPAYMENTRESPONSE, \
    ADDSTOREDSUBSCRIPTIONRESPONSE, PAYMENTRESPONSE, CREDENTIALONFILE
from utils import random_text
from wnclient import WNClient

wn = WNClient().vagrant.wn
TERM_ID = '22004'


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
    response = wn.xml(TERM_ID).add_stored_subscription(request=ss, currency=Currency.EUR)
    assert_that(response, instance_of(ADDSTOREDSUBSCRIPTIONRESPONSE))


@pytest.mark.parametrize('card', CashFlowsSecureCard)
def test_cashflows_securecard_registration(card):
    sc = securecard_registration(cvv=card.cvv)
    sc.CREDENTIALONFILE = credential_on_file()
    sc.CREDENTIALONFILE.STOREDCREDENTIALTXTYPE = StoredCredentialTxType.FIRST_TXN.name
    sc.CREDENTIALONFILE.STOREDCREDENTIALUSE = card.cof_use.name
    sc.CARDNUMBER = card.cardnumber
    sc.MERCHANTREF = card.merchant_ref
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))
    assert_that(response.CREDENTIALONFILE, has_property('BRANDTXIDENTIFIER', is_not(None)))
    # verify DB secure_card_additional_setting.stored_credential_use field value
    sc_additional_settings = wn.db(terminal_number=TERM_ID).get_secure_card_additional_settings(response.MERCHANTREF)
    assert_that(sc_additional_settings.stored_credential_use, card.cof_use)


def test_cashflows_unsupported_securecard_registration():
    sc = securecard_registration()
    sc.CREDENTIALONFILE = credential_on_file()
    sc.CREDENTIALONFILE.STOREDCREDENTIALTXTYPE = StoredCredentialTxType.FIRST_TXN.name
    sc.CREDENTIALONFILE.STOREDCREDENTIALUSE = StoredCredentialUse.UNSCHEDULED.name
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))
    assert_that(response.CREDENTIALONFILE, has_property('BRANDTXIDENTIFIER', is_not(None)))


@pytest.mark.parametrize('card', [CashFlowsSecureCard.VISA_UNSC, CashFlowsSecureCard.VISA_INST, CashFlowsSecureCard.VISA_SUBS])
def test_cashflows_securecard_payment_ecommerce_CIT(card):
    search_response = wn.xml(TERM_ID).secure_card_search(card.merchant_ref)

    p = payment_securecard(cardreference=search_response.CARDREFERENCE)
    p.CURRENCY = Currency.EUR.name
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_CARDHOLDER_INITIATED_TXN.name,
    )

    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


@pytest.mark.parametrize('card', [CashFlowsSecureCard.VISA_UNSC, CashFlowsSecureCard.VISA_INST, CashFlowsSecureCard.VISA_SUBS])
def test_cashflows_securecard_payment_recurring_mit(card):
    search_response = wn.xml(TERM_ID).secure_card_search(card.merchant_ref)

    p = payment_securecard(cardreference=search_response.CARDREFERENCE)
    p.TRANSACTIONTYPE = TransactionType.RECURRING
    p.CURRENCY = Currency.EUR.name
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name,
        STOREDCREDENTIALUSE=StoredCredentialUse.RECURRING.name
    )
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))


@pytest.mark.parametrize('card', [CashFlowsSecureCard.VISA_UNSC, CashFlowsSecureCard.VISA_INST, CashFlowsSecureCard.VISA_SUBS])
def test_cashflows_securecard_payment_installment_mit(card):
    search_response = wn.xml(TERM_ID).secure_card_search(card.merchant_ref)

    p = payment_securecard(cardreference=search_response.CARDREFERENCE)
    p.TRANSACTIONTYPE = TransactionType.INSTALLMENT
    p.CURRENCY = Currency.EUR.name
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name,
        STOREDCREDENTIALUSE=StoredCredentialUse.INSTALLMENT.name
    )
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))


@pytest.mark.parametrize('ss_merchant_ref, sc', {
    ('ss_limited', CashFlowsSecureCard.VISA_UNSC),
    ('ss_limited', CashFlowsSecureCard.VISA_INST),
    ('ss_limited', CashFlowsSecureCard.VISA_SUBS),
    ('ss_unlimited', CashFlowsSecureCard.VISA_UNSC),
    ('ss_unlimited', CashFlowsSecureCard.VISA_INST),
    ('ss_unlimited', CashFlowsSecureCard.VISA_SUBS),
    # ('ss_limited_before_cof', CashFlowsSecureCard.VISA_NO_COF),
    # ('ss_unlimited_before_cof', CashFlowsSecureCard.VISA_NO_COF),
    # ('ss_limited_before_cof', CashFlowsSecureCard.MC_NO_COF),
    # ('ss_unlimited_before_cof', CashFlowsSecureCard.MC_NO_COF),
})
def test_cashflows_subscription_payment(ss_merchant_ref, sc):
    s = subscription(stored_subscriptionref=ss_merchant_ref)
    s.MERCHANTREF = '%s_%s' % (ss_merchant_ref, sc.merchant_ref)
    s.SECURECARDMERCHANTREF = sc.merchant_ref
    subscription_response = wn.xml(TERM_ID).add_subscription(request=s)
    assert_that(subscription_response, instance_of(ADDSUBSCRIPTIONRESPONSE))

    sp = payment_subscription(subscription_response.MERCHANTREF)
    subscription_payment_response = wn.xml(TERM_ID).subscription_payment(request=sp, currency=Currency.EUR)
    assert_that(subscription_payment_response, instance_of(SUBSCRIPTIONPAYMENTRESPONSE))


@pytest.mark.parametrize('stored_credential_use', StoredCredentialUse)
def test_cashflows_ecomm_cof_unscheduled_visa_payment(stored_credential_use):
    p = payment()
    p.CURRENCY = Currency.EUR.name
    p.CARDNUMBER = CashFlowsSecureCard.VISA_UNSC.cardnumber
    p.CVV = CashFlowsSecureCard.VISA_UNSC.cvv
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALUSE=stored_credential_use.name,
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.FIRST_TXN.name
    )
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))


def test_cashflows_ecomm_cof_CIT_visa_payment():
    p = payment()
    p.CURRENCY = Currency.EUR.name
    p.CARDNUMBER = CashFlowsSecureCard.VISA_SUBS.cardnumber
    p.CVV = CashFlowsSecureCard.VISA_SUBS.cvv
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_CARDHOLDER_INITIATED_TXN.name
    )

    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response, has_property('CREDENTIALONFILE', is_(None)))


def test_cashflows_ecomm_cof_MIT_UNSC_visa_payment():
    p = payment()
    p.CURRENCY = Currency.EUR.name
    p.CARDNUMBER = CashFlowsSecureCard.VISA_SUBS.cardnumber
    p.CVV = CashFlowsSecureCard.VISA_SUBS.cvv
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        ORIGINALBRANDTXIDENTIFIER=random_text(11),  # length should be exactly 11 symbols
        STOREDCREDENTIALUSE=StoredCredentialUse.UNSCHEDULED.name,
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_MERCHANT_INITIATED_TXN.name
    )

    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.CREDENTIALONFILE.BRANDTXIDENTIFIER, is_not(None))


def test_cashflows_ecomm_no_cof_visa_payment():
    p = payment()
    p.CURRENCY = Currency.EUR.name
    p.CARDNUMBER = CashFlowsSecureCard.VISA_SUBS.cardnumber
    p.CVV = CashFlowsSecureCard.VISA_SUBS.cvv

    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response, has_property('CREDENTIALONFILE', is_(None)))


def test_cashflows_moto_cof_payment():
    p = payment()
    p.TERMINALTYPE=TerminalType.MOTO
    p.TRANSACTIONTYPE=TransactionType.MOTO
    p.CURRENCY = Currency.EUR.name
    p.CARDNUMBER = CashFlowsSecureCard.VISA_UNSC.cardnumber
    p.CVV = CashFlowsSecureCard.VISA_UNSC.cvv
    p.CREDENTIALONFILE = CREDENTIALONFILE(
        STOREDCREDENTIALTXTYPE=StoredCredentialTxType.SUBSEQUENT_CARDHOLDER_INITIATED_TXN.name
    )

    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
