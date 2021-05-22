import pytest
from hamcrest import assert_that, instance_of, equal_to, has_length

from constants import LocalMerchant, SecureCard, MerchantPortfolio
from model.gateway import ERROR, CUSTOMFIELD, \
    SECURE_CARD_ADVANCED_SEARCH_RESPONSE
from wnclient import WNClient

wn = WNClient().local.go
TERM_ID = '21001'
TERM_ID_SHARED = '21002'
MP = MerchantPortfolio.GO_MERCHANT_PORTFOLIO


@pytest.mark.parametrize('custom_field', [
    [CUSTOMFIELD(NAME='UID', valueOf_='uid_mastercard'), CUSTOMFIELD(NAME='ismastercard', valueOf_='True')],
    [CUSTOMFIELD(NAME='UID', valueOf_='uid_mastercard')]
])
def test_securecard_advanced_search_custom_field_card_found(custom_field):
    sc = SecureCard.MASTERCARD
    wn.boarding().update_merchant_general_setup(LocalMerchant.GO.itemid)
    wn.boarding().update_merchant(LocalMerchant.GO.itemid, merchantPortfolioUniqueId=None)

    response = wn.xml(TERM_ID).secure_card_advanced_search(CUSTOMFIELD=custom_field)
    assert_that(response, instance_of(SECURE_CARD_ADVANCED_SEARCH_RESPONSE))
    assert_that(response.SECURECARD, has_length(1))
    assert_that(response.SECURECARD[0].MERCHANTREF, equal_to(sc.merchant_ref))


def test_securecard_advanced_search_custom_fields_of_different_cards():
    wn.boarding().update_merchant_general_setup(LocalMerchant.GO.itemid)
    wn.boarding().update_merchant(LocalMerchant.GO.itemid, merchantPortfolioUniqueId=None)

    response = wn.xml(TERM_ID).secure_card_advanced_search(
        CUSTOMFIELD=[CUSTOMFIELD(NAME='isvisa', valueOf_='True'), CUSTOMFIELD(NAME='ismastercard', valueOf_='True')])
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('SECURE CARD NOT FOUND'))


def test_securecard_advanced_search_by_custom_field_value_not_exists():
    wn.boarding().update_merchant_general_setup(LocalMerchant.GO.itemid)
    wn.boarding().update_merchant(LocalMerchant.GO.itemid, merchantPortfolioUniqueId=None)
    response = wn.xml(TERM_ID).secure_card_advanced_search(
        CUSTOMFIELD=[CUSTOMFIELD(NAME='uid', valueOf_='value doesnt exist')])
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('SECURE CARD NOT FOUND'))


def test_securecard_advanced_search_by_custom_field_sc_sharing_disabled():
    wn.boarding().update_merchant_general_setup(LocalMerchant.GO.itemid)
    wn.boarding().update_merchant(LocalMerchant.GO.itemid, merchantPortfolioUniqueId=None)

    response = wn.xml(TERM_ID).secure_card_advanced_search(
        CUSTOMFIELD=[CUSTOMFIELD(NAME='not_exists', valueOf_='any value')])
    assert_that(response, instance_of(SECURE_CARD_ADVANCED_SEARCH_RESPONSE))
    assert_that(response.SECURECARD, has_length(8))     # see issue #23910


def test_securecard_advanced_search_by_custom_field_sc_sharing_enabled():
    wn.boarding().update_merchant_general_setup(LocalMerchant.GO.itemid, True, True)
    wn.boarding().update_merchant(LocalMerchant.GO.itemid, merchantPortfolioUniqueId=None)
    response = wn.xml(TERM_ID_SHARED).secure_card_advanced_search(
        CUSTOMFIELD=[CUSTOMFIELD(NAME='uid', valueOf_='uid_mastercard')])
    assert_that(response, instance_of(SECURE_CARD_ADVANCED_SEARCH_RESPONSE))
    assert_that(response.SECURECARD, has_length(8))     # see issue #23910


def test_securecard_advanced_search_by_disabled_terminal():
    sc = SecureCard.MASTERCARD
    wn.boarding().delete_terminal(TERM_ID)
    wn.boarding().update_merchant_general_setup(LocalMerchant.GO.itemid)
    wn.boarding().update_merchant(LocalMerchant.GO.itemid, merchantPortfolioUniqueId=None)
    wn.boarding().update_merchant_portfolio(MP.mpid, enableSecureCardAutoSharing=False,
                                            shareCardsFromDeactivatedTerminals=False)

    response = wn.xml(TERM_ID).secure_card_advanced_search(NAME=sc.cardholdername)
    wn.boarding().activate_terminal(TERM_ID)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('INVALID TERMINALID'))


@pytest.mark.parametrize('search_criteria', ['CARDHOLDERNAME', 'PHONE', 'EMAIL', 'CREATIONDATE'])
def test_securecard_advanced_search_merchant_portfolio_shared(search_criteria):
    sc = SecureCard.rand()
    search_value = getattr(sc, search_criteria.lower())
    if search_criteria is 'CREATIONDATE':
        search_value = sc.creationdate.strftime('%d-%m-%Y')
    search_criteria = search_criteria.replace('CARDHOLDERNAME', 'NAME')

    wn.boarding().update_merchant_general_setup(LocalMerchant.GO.itemid)
    wn.boarding().update_merchant(LocalMerchant.GO.itemid, merchantPortfolioUniqueId=MP.mpid)
    wn.boarding().update_merchant_portfolio(MP.mpid, enableSecureCardAutoSharing=True,
                                            shareCardsFromDeactivatedTerminals=True)

    response = wn.xml(TERM_ID_SHARED).secure_card_advanced_search(**{search_criteria: search_value})
    assert_that(response, instance_of(SECURE_CARD_ADVANCED_SEARCH_RESPONSE))
    assert_that(response.SECURECARD, has_length(1))
    assert_that(response.SECURECARD[0].MERCHANTREF, equal_to(sc.merchant_ref))


@pytest.mark.parametrize('search_criteria', ['CARDHOLDERNAME', 'PHONE', 'EMAIL', 'CREATIONDATE'])
def test_securecard_advanced_search_merchant_shared_only(search_criteria):
    sc = SecureCard.rand()
    search_value = getattr(sc, search_criteria.lower())
    if search_criteria is 'CREATIONDATE':
        search_value = sc.creationdate.strftime('%d-%m-%Y')
    search_criteria = search_criteria.replace('CARDHOLDERNAME', 'NAME')

    wn.boarding().activate_terminal(TERM_ID)
    wn.boarding().update_merchant(LocalMerchant.GO.itemid, merchantPortfolioUniqueId=None)
    wn.boarding().update_merchant_general_setup(LocalMerchant.GO.itemid, True, True)

    response = wn.xml(TERM_ID_SHARED).secure_card_advanced_search(**{search_criteria: search_value})
    assert_that(response, instance_of(SECURE_CARD_ADVANCED_SEARCH_RESPONSE))
    assert_that(response.SECURECARD, has_length(1))
    assert_that(response.SECURECARD[0].MERCHANTREF, equal_to(sc.merchant_ref))


@pytest.mark.parametrize('search_criteria', ['CARDHOLDERNAME', 'PHONE', 'EMAIL', 'CREATIONDATE'])
def test_securecard_advanced_search_deactivated_terminal_merchant_shared(search_criteria):
    sc = SecureCard.rand()
    search_value = getattr(sc, search_criteria.lower())
    if search_criteria is 'CREATIONDATE':
        search_value = sc.creationdate.strftime('%d-%m-%Y')
    search_criteria = search_criteria.replace('CARDHOLDERNAME', 'NAME')

    wn.boarding().delete_terminal(TERM_ID)
    wn.boarding().update_merchant_general_setup(LocalMerchant.GO.itemid, True, True)
    wn.boarding().update_merchant(LocalMerchant.GO.itemid, merchantPortfolioUniqueId=None)

    response = wn.xml(TERM_ID_SHARED).secure_card_advanced_search(**{search_criteria: search_value})
    wn.boarding().activate_terminal(TERM_ID)

    assert_that(response, instance_of(SECURE_CARD_ADVANCED_SEARCH_RESPONSE))
    assert_that(response.SECURECARD, has_length(1))
    assert_that(response.SECURECARD[0].MERCHANTREF, equal_to(sc.merchant_ref))


@pytest.mark.parametrize('search_criteria', ['CARDHOLDERNAME', 'PHONE', 'EMAIL', 'CREATIONDATE'])
def test_securecard_advanced_search_merchant_shared_not_allowed_from_deactivated_terminal(search_criteria):
    sc = SecureCard.rand()
    search_value = getattr(sc, search_criteria.lower())
    if search_criteria is 'CREATIONDATE':
        search_value = sc.creationdate.strftime('%d-%m-%Y')
    search_criteria = search_criteria.replace('CARDHOLDERNAME', 'NAME')

    wn.boarding().delete_terminal(TERM_ID)
    wn.boarding().update_merchant_general_setup(LocalMerchant.GO.itemid, True, False)
    wn.boarding().update_merchant(LocalMerchant.GO.itemid, merchantPortfolioUniqueId=None)

    response = wn.xml(TERM_ID_SHARED).secure_card_advanced_search(**{search_criteria: search_value})
    wn.boarding().activate_terminal(TERM_ID)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, 'SECURE CARD NOT FOUND')


@pytest.mark.parametrize('search_criteria', ['CARDHOLDERNAME', 'PHONE', 'EMAIL', 'CREATIONDATE'])
def test_securecard_advanced_search_deactivated_terminal_sharing_disabled(search_criteria):
    sc = SecureCard.rand()
    search_value = getattr(sc, search_criteria.lower())
    if search_criteria is 'CREATIONDATE':
        search_value = sc.creationdate.strftime('%d-%m-%Y')
    search_criteria = search_criteria.replace('CARDHOLDERNAME', 'NAME')

    wn.boarding().delete_terminal(TERM_ID)
    wn.boarding().update_merchant_general_setup(LocalMerchant.GO.itemid)
    wn.boarding().update_merchant(LocalMerchant.GO.itemid, merchantPortfolioUniqueId=None)

    response = wn.xml(TERM_ID_SHARED).secure_card_advanced_search(**{search_criteria: search_value})
    wn.boarding().activate_terminal(TERM_ID)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('SECURE CARD NOT FOUND'))


@pytest.mark.parametrize('search_criteria', ['CARDHOLDERNAME', 'PHONE', 'EMAIL', 'CREATIONDATE'])
def test_securecard_advanced_search_deactivated_terminal_merchant_portfolio_shared(search_criteria):
    mp = MerchantPortfolio.GO_MERCHANT_PORTFOLIO
    sc = SecureCard.rand()
    search_value = getattr(sc, search_criteria.lower())
    if search_criteria is 'CREATIONDATE':
        search_value = sc.creationdate.strftime('%d-%m-%Y')
    search_criteria = search_criteria.replace('CARDHOLDERNAME', 'NAME')

    wn.boarding().delete_terminal(TERM_ID)                                                     # deactivate terminal
    wn.boarding().update_merchant(LocalMerchant.GO.itemid, merchantPortfolioUniqueId=mp.mpid)  # set merchant portfolio
    wn.boarding().update_merchant_general_setup(LocalMerchant.GO.itemid)                       # disable sc sharing
    wn.boarding().update_merchant_portfolio(MP.mpid, enableSecureCardAutoSharing=True,
                                            shareCardsFromDeactivatedTerminals=True,
                                            enableSecureCardUniqueness=False)

    response = wn.xml(TERM_ID_SHARED).secure_card_advanced_search(**{search_criteria: search_value})
    wn.boarding().activate_terminal(TERM_ID)                                                # activate terminal

    assert_that(response, instance_of(SECURE_CARD_ADVANCED_SEARCH_RESPONSE))
    assert_that(response.SECURECARD, has_length(1))
    assert_that(response.SECURECARD[0].MERCHANTREF, equal_to(sc.merchant_ref))
