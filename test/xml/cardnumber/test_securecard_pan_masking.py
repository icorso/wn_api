import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import securecard_registration, securecard_update, payment
from model.gateway import ERROR, SECURECARDREGISTRATIONRESPONSE, CUSTOMFIELD, PAYMENTRESPONSE
from utils import random_card, split_string
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22001'
CUSTOMEFIELD_NAME = 'SecureCardField'
# #31871 - Disallow card number setting in other fields at creating, modifying SC


@pytest.mark.parametrize('field', [
    'CARDHOLDERNAME',
    'PHONE',
    'EMAIL',
    'POSTCODE'
])
def test_securecard_registration_exact_pan_not_allowed(field):
    request = securecard_registration()
    setattr(request, field, request.CARDNUMBER)
    response = wn.xml(TERM_ID).secure_card_registration(request=request)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to(f'Invalid {field} field'))


@pytest.mark.parametrize('field, divider', [
    ('CARDHOLDERNAME', ' '),
    ('PHONE', ' '),
    ('EMAIL', ' '),
    ('POSTCODE', ' '),
    ('CARDHOLDERNAME', '-'),
    ('PHONE', '-'),
    ('EMAIL', '-'),
    ('POSTCODE', '-')
])
def test_securecard_registration_divided_pan_not_allowed(field, divider):
    request = securecard_registration()
    setattr(request, field, split_string(request.CARDNUMBER, divider, 4))
    response = wn.xml(TERM_ID).secure_card_registration(request=request)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to(f'Invalid {field} field'))


def test_securecard_registration_pan_mpiref():
    request = securecard_registration()
    request.MPIREF = 'ab' + request.CARDNUMBER + 'xz'
    response = wn.xml(TERM_ID).secure_card_registration(request=request)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to(f'Invalid MPIREF field'))


@pytest.mark.parametrize('field', [
    'CARDHOLDERNAME',
    'PHONE',
    'EMAIL',
    'POSTCODE'
])
def test_securecard_registration_another_pan_allowed(field):
    request = securecard_registration()
    setattr(request, field, random_card('visa').cardnumber)
    response = wn.xml(TERM_ID).secure_card_registration(request=request)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


@pytest.mark.parametrize('field', [
    'CARDHOLDERNAME',
    'PHONE',
    'EMAIL',
])
def test_securecard_update_pan_not_allowed(field):
    response = wn.xml(TERM_ID).secure_card_registration()

    update_request = securecard_update(response.MERCHANTREF)
    setattr(update_request, field, update_request.CARDNUMBER)

    update_response = wn.xml(TERM_ID).secure_card_update(update_request)
    assert_that(update_response, instance_of(ERROR))
    assert_that(update_response.ERRORSTRING, equal_to(f'Invalid {field} field'))


def test_securecard_registration_custom_field_pan_not_allowed():
    request = securecard_registration()
    request.CUSTOMFIELD = [
        CUSTOMFIELD(NAME=CUSTOMEFIELD_NAME, valueOf_=request.CARDNUMBER)
    ]
    response = wn.xml(TERM_ID).secure_card_registration(request=request)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to(f'Invalid CUSTOMFIELD - {CUSTOMEFIELD_NAME} field'))


def test_securecard_update_custom_field_pan_not_allowed():
    response = wn.xml(TERM_ID).secure_card_registration()
    update_request = securecard_update(response.MERCHANTREF, cardtype='mastercard')
    update_request.CUSTOMFIELD = [
        CUSTOMFIELD(NAME=CUSTOMEFIELD_NAME, valueOf_=update_request.CARDNUMBER)
    ]

    update_response = wn.xml(TERM_ID).secure_card_update(update_request)
    assert_that(update_response, instance_of(ERROR))
    assert_that(update_response.ERRORSTRING, equal_to(f'Invalid CUSTOMFIELD - {CUSTOMEFIELD_NAME} field'))


@pytest.mark.parametrize('divider', [' ', '-'])
def test_securecard_registration_custom_field_divided_pan_not_allowed(divider):
    request = securecard_registration()
    request.CUSTOMFIELD = [
        CUSTOMFIELD(NAME=CUSTOMEFIELD_NAME, valueOf_=split_string(request.CARDNUMBER, divider, 4))
    ]
    response = wn.xml(TERM_ID).secure_card_registration(request=request)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to(f'Invalid CUSTOMFIELD - {CUSTOMEFIELD_NAME} field'))


@pytest.mark.parametrize('field', [
    'CARDHOLDERNAME',
    'EMAIL',
    'POSTCODE'
])
def test_securecard_auto_registration_not_allowed(field):
    """
    WorldnetMerchantPortfolio > Enable SC Auto Registration is turned on
    """
    p = payment()
    setattr(p, field, p.CARDNUMBER) if field is not  'EMAIL' else setattr(p, field, p.CARDNUMBER + "@local.host")
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
