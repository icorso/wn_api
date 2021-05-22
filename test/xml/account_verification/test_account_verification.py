import hashlib

import pytest
from faker import Factory
from hamcrest import assert_that, equal_to, instance_of, contains_string

from data.xml_requests import account_verification_request
from model.boarding import terminal
from model.gateway import ACCOUNT_VERIFICATION_RESPONSE, ERROR
from utils import random_card, random_text
from wnclient import WNClient

wn = WNClient().vagrant

fake = Factory.create()

TERM_ID = '21001'
ELAVON_TERM_ID = '22001'
VISA_DECLINED = '4716568913084649'


def test_account_verification_verified():
    response = wn.go.xml(TERM_ID).account_verification()
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('VERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to(None))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


def test_account_cardtype_not_supported():
    """
        terminal should not support MASTERCARD
    """
    terminal_update_response = wn.go.boarding().update_terminal_cards(TERM_ID, ['visa'])
    assert_that(terminal_update_response, instance_of(terminal))

    av = account_verification_request()
    av.CARDNUMBER = random_card('mastercard').cardnumber
    response = wn.go.xml(TERM_ID).account_verification(av)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, contains_string('Unsupported CARDTYPE'))

    terminal_update_all_cards = wn.go.boarding().update_terminal_cards(TERM_ID)
    assert_that(terminal_update_all_cards, instance_of(terminal))


@pytest.mark.parametrize('field, max_length', [
    ('CARDHOLDERNAME', 50),
    ('POSTCODE', 50),
    ('ADDRESS1', 50),
    ('ADDRESS2', 50),
    ('CARDNUMBER', 40),
    ('CARDEXPIRY', 4),
])
def test_account_verification_max_length(field, max_length):

    av = account_verification_request()
    field_value = random_text(max_length + 1)
    setattr(av, field, field_value)
    response = wn.go.xml(TERM_ID).account_verification(av)
    expected_text = "cvc-maxLength-valid: Value '%s' with length = '%s' is not facet-valid with respect to maxLength " \
                    "'%s' for type '#AnonType_%s'."
    if field == 'CARDEXPIRY':
        expected_text = expected_text.replace('maxLength', 'length')
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to(expected_text % (field_value,
                                                                str(max_length + 1), str(max_length), field)))


@pytest.mark.parametrize('invalid_cardtype', ['492964151140848'])
def test_account_verification_invalid_card_type(invalid_cardtype):
    """ Incorrect cardnumber length """
    request = account_verification_request()
    request.CARDNUMBER = invalid_cardtype
    response = wn.go.xml(TERM_ID).account_verification(request)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid card type'))


@pytest.mark.parametrize('invalid_cardtype', ['1234567890', '12345678901', '4929641511408481'])
def test_account_verification_invalid_card_number(invalid_cardtype):
    request = account_verification_request()
    request.CARDNUMBER = invalid_cardtype
    response = wn.go.xml(TERM_ID).account_verification(request)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid card number'))


@pytest.mark.parametrize('expiry_date', ['aaaa', '0000', '9999', '0022', '1321', '0419'])  # 'MMYY'
def test_account_verification_invalid_card_expiry(expiry_date):
    request = account_verification_request()
    request.CARDEXPIRY = expiry_date
    response = wn.go.xml(TERM_ID).account_verification(request)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid card expiry'))


def test_account_verification_not_supported():
    """
        Should be 1$ auth/reversal in the log
    """
    response = wn.wn.xml(ELAVON_TERM_ID).account_verification()
    expected_hash_string = ELAVON_TERM_ID + ':' + response.DATETIME + ':' + wn.wn.get_terminal_secret()
    m = hashlib.sha512()
    m.update(str.encode(expected_hash_string))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")

    # assert_that(response.HASH, equal_to(m.hexdigest()), "Response HASH doesn't correspond to expected value")
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('VERIFIED'))


def test_account_verification_declined_response():
    request = account_verification_request()
    request.CARDNUMBER = VISA_DECLINED
    response = wn.go.xml(terminal_id=TERM_ID).account_verification(request)
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('UNVERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to('Error'))


def test_account_verification_credorax():
    """  simulator code should be updated to decline every txn by cvv:
         private void processAuthTxn(CredoraxResponse credoraxResponse) {
            String cvvResponse = CredoraxResponse.CVV_RESPONSE_NO_MATCH;
    """
    request = account_verification_request(cvv='111')
    response = wn.wn.xml(terminal_id='22006').account_verification(request)
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('UNVERIFIED'))


def test_account_verification_nmi_verified():
    request = account_verification_request()
    response = wn.wn.xml(terminal_id='22012').account_verification(request)
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('UNVERIFIED'))


def test_account_verification_nmi_unverified():
    """
        CVV validation failed when cvv differs from 999
    """
    TERM_ID = '22012'
    request = account_verification_request()
    request.CVV = '123'
    response = wn.wn.xml(terminal_id=TERM_ID).account_verification(request)
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('UNVERIFIED'))
    assert_that(response.RESPONSE_DETAIL, equal_to('CVV validation failed'))
    assert_that(response.generate_hash(), equal_to(response.HASH), "Response HASH doesn't correspond to expected value")


def test_account_verification_fdrc_verified():
    request = account_verification_request()
    response = wn.wn.xml(terminal_id='22005').account_verification(request)
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('VERIFIED'))
