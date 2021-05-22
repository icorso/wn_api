import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to, is_not, has_length

from constants import LocalMerchant
from data.boarding.terminal import tsys_sierra_terminal
from model.boarding import terminal, cardsType, reimbursementAttributeEnum, industryCodeEnum, serviceError, \
    languageIndicatorEnum
from utils import random_text
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.go
tpl = 'tsys_sierra_term_tpl'


def test_boarding_terminal_sierra_create_and_get():
    t = tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid)
    response = wn.boarding().create_terminal(request=t)
    assert_that(response, instance_of(terminal))

    get_terminal_response = WNClient().local.go.boarding().get_terminal(response.terminalNumber)
    ats = get_terminal_response.additionalSettings
    assert_that(get_terminal_response, instance_of(terminal))
    assert_that(ats.agentBankNumber, equal_to(t.additionalSettings.agentBankNumber))
    assert_that(ats.agentChainNumber, equal_to(t.additionalSettings.agentChainNumber))
    assert_that(ats.terminalIdNumber, equal_to(t.additionalSettings.terminalIdNumber))
    assert_that(ats.storeNumber, equal_to(t.additionalSettings.storeNumber))
    assert_that(ats.abaNumber, equal_to(t.additionalSettings.abaNumber))
    assert_that(ats.settlementAgentNo, equal_to(t.additionalSettings.settlementAgentNo))
    assert_that(ats.industryCode, equal_to(t.additionalSettings.industryCode))
    assert_that(ats.languageIndicator, equal_to(t.additionalSettings.languageIndicator))
    assert_that(ats.authenticationCode, equal_to(t.additionalSettings.authenticationCode))
    assert_that(ats.acquirerBin, equal_to(t.additionalSettings.acquirerBin))
    assert_that(ats.dstObserved, equal_to(t.additionalSettings.dstObserved))
    assert_that(ats.timeZoneOffset, equal_to(t.additionalSettings.timeZoneOffset))
    assert_that(ats.sharingGroup, equal_to(t.additionalSettings.sharingGroup))
    assert_that(ats.allowLevel2Data, equal_to(t.additionalSettings.allowLevel2Data))
    assert_that(ats.reimbursementAttribute, equal_to(t.additionalSettings.reimbursementAttribute))
    assert_that(ats.cardholderSvcPhoneNumber, equal_to(t.additionalSettings.cardholderSvcPhoneNumber))
    assert_that(ats.merchantLocationNumber, equal_to(t.additionalSettings.merchantLocationNumber))
    assert_that(get_terminal_response.bankSettings.fcsId, equal_to(t.bankSettings.fcsId))


def test_boarding_terminal_sierra_no_allowed_multicurrency():
    t = tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid)
    t.bankSettings.allowMulticurrency = True
    response = wn.boarding().create_terminal(request=t)
    assert_that(response, instance_of(serviceError))
    error = response.validationErrors.validationError[0]
    assert_that(error.target, equal_to('allowMulticurrency'))
    assert_that(error.message, equal_to('Value not allowed when acquirer is TSYS'))


def test_boarding_terminal_sierra_template_get():
    response = wn.boarding().get_terminal_template(tpl)
    assert_that(response, instance_of(terminal))


def test_boarding_terminal_sierra_list_terminal():
    response = wn.boarding().list_terminal(LocalMerchant.GO.itemid)
    assert_that(response, instance_of(terminal))
    # TODO generateDS serialization issue


def test_boarding_terminal_sierra_create_state_validation():
    t = tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid)
    t.country = 'USA'
    t.additionalSettings.usState = None
    response = wn.boarding().create_terminal(request=t)
    assert_that(response, instance_of(serviceError))
    error = response.validationErrors.validationError[0]
    assert_that(error.target, equal_to('usState'))
    assert_that(error.message, equal_to('Mandatory Field'))


def test_boarding_update_sierra_cards():
    card = 'AMEX'
    create_response = wn.boarding().create_terminal(tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid))

    update_request = create_response
    update_request.cards = cardsType([card])
    update_response = wn.boarding().update_terminal(request=update_request)
    assert_that(update_response.cards.card, has_length(1))
    assert_that(update_response.cards.card[0], equal_to(card))


def test_boarding_sierra_allowLevel2Data_update():
    t = tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid)
    t.additionalSettings.allowLevel2Data = True
    create_response = wn.boarding().create_terminal(t)
    assert_that(create_response.additionalSettings.allowLevel2Data, equal_to(t.additionalSettings.allowLevel2Data))

    update_request = create_response
    update_request.additionalSettings.allowLevel2Data = False
    update_response = wn.boarding().update_terminal(request=update_request)
    assert_that(update_response.additionalSettings.allowLevel2Data,
                equal_to(update_request.additionalSettings.allowLevel2Data))


@pytest.mark.parametrize('field, value', [
    ('agentBankNumber', str(fake.random_number(6))), ('acquirerBin', str(fake.random_number(6))),
    ('terminalIdNumber', random_text(8)), ('agentChainNumber', str(fake.random_number(5))),
    ('storeNumber', str(fake.random_number(4))), ('abaNumber', str(fake.random_number(8))),
    ('settlementAgentNo', str(fake.random_number(4))),('industryCode', industryCodeEnum.FINANCIAL),
    ('languageIndicator', languageIndicatorEnum.ENGLISH), ('authenticationCode', str(fake.random_number(9))),
    ('acquirerBin', str(fake.random_number(5))), ('dstObserved', False), ('timeZoneOffset', fake.random_int(0, 12)),
    ('sharingGroup', random_text(30)), ('reimbursementAttribute', reimbursementAttributeEnum.ATTRIBUTE__0),
    ('cardholderSvcPhoneNumber', str(fake.random_number(11))),
])
def test_boarding_terminal_sierra_fields_update(field, value):
    t = tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid)
    response = wn.boarding().create_terminal(t)
    assert_that(response, instance_of(terminal))
    assert_that(response.additionalSettings.dstObserved, equal_to(True))
    assert_that(response.additionalSettings.reimbursementAttribute, equal_to(reimbursementAttributeEnum.ATTRIBUTE_W))
    assert_that(response.additionalSettings.industryCode, equal_to(industryCodeEnum.FOOD))

    update_request = response
    setattr(update_request.additionalSettings, field, value)
    update_response = wn.boarding().update_terminal(update_request)
    assert_that(update_response, instance_of(terminal))
    assert_that(getattr(update_response.additionalSettings, field), equal_to(value))

    get_response = wn.boarding().get_terminal(response.terminalNumber)
    assert_that(get_response, instance_of(terminal))
    assert_that(getattr(get_response.additionalSettings, field), equal_to(value))


@pytest.mark.parametrize('field', ['agentBankNumber', 'terminalIdNumber', 'agentChainNumber', 'storeNumber',
                                   'industryCode', 'languageIndicator', 'authenticationCode', 'acquirerBin',
                                   'reimbursementAttribute'])
def test_boarding_terminal_sierra_mandatory_fields_validation(field):
    t = tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid)
    setattr(t.additionalSettings, field, None)
    response = wn.boarding().create_terminal(t)
    assert_that(response, instance_of(serviceError))
    error = response.validationErrors.validationError[0]
    assert_that(error.target.lower(), equal_to(field.lower()))
    assert_that(error.message, equal_to('Mandatory Field'))


@pytest.mark.parametrize('field, max_length', [
    ('agentBankNumber', 6), ('agentChainNumber', 6), ('storeNumber', 4), ('abaNumber', 9), ('settlementAgentNo', 4),
    ('authenticationCode', 10), ('acquirerBin', 6), ('sharingGroup', 30), ('cardholderSvcPhoneNumber', 11)
])
def test_boarding_terminal_sierra_fields_create_max_length(field, max_length):
    t = tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid)
    setattr(t.additionalSettings, field, random_text(max_length + 1))
    response = wn.boarding().create_terminal(t)
    assert_that(response, instance_of(serviceError))
    error = response.validationErrors.validationError[0]
    assert_that(str(error.target).lower().replace('merchant', ''),
                equal_to(str(field).lower().replace('settlementagentno', 'settleagentnumber')))  # stupid replace I know
    assert_that(error.message, equal_to('Value should not be longer than %s characters' % str(max_length)))


@pytest.mark.parametrize('field', ['industryCode', 'reimbursementAttribute', 'languageIndicator'])
def test_boarding_terminal_sierra_enum_fields_incorrect_value(field):
    t = tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid)
    setattr(t.additionalSettings, field, str(fake.random_number(5)))
    response = wn.boarding().create_terminal(t)
    assert_that(response, instance_of(serviceError))
    error = response.validationErrors.validationError[0]
    assert_that(error.target.lower(), equal_to(field.lower()))
    assert_that(error.message, equal_to('Mandatory Field'))


def test_boarding_terminal_sierra_fcsId_create_max_length():
    t = tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid)
    t.bankSettings.set_fcsId(str(fake.random_number(8)))
    response = wn.boarding().create_terminal(t)
    assert_that(response, instance_of(serviceError))
    error = response.validationErrors.validationError[0]
    assert_that(error.target, equal_to('fcsId'))
    assert_that(error.message, equal_to('Value should not be longer than 7 characters'))


def test_boarding_terminal_sierra_fcsId_update():
    fcs_id = str(fake.random_number(7))
    t = tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid)
    response = wn.boarding().create_terminal(t)

    update_request = response
    update_request.bankSettings.set_fcsId(fcs_id)
    update_response = wn.boarding().update_terminal(update_request)
    assert_that(update_response, instance_of(terminal))
    assert_that(update_response.bankSettings.fcsId, equal_to(fcs_id))

    get_response = wn.boarding().get_terminal(response.terminalNumber)
    assert_that(get_response, instance_of(terminal))
    assert_that(get_response.bankSettings.fcsId, equal_to(fcs_id))


@pytest.mark.parametrize('max_length', [7, 9])
def test_boarding_terminal_sierra_fields_terminal_id_number_length(max_length):
    t = tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid)
    t.additionalSettings.set_terminalIdNumber(str(fake.random_number(max_length)))
    response = wn.boarding().create_terminal(t)
    assert_that(response, instance_of(serviceError))
    error = response.validationErrors.validationError[0]
    assert_that(error.target, equal_to('terminalIdNumber'))
    assert_that(error.message, equal_to('Value should be exactly 8 characters long'))


def test_boarding_terminal_sierra_deactivate():
    response = wn.boarding().create_terminal(request=tsys_sierra_terminal(merchant_id=LocalMerchant.GO.itemid))
    delete_terminal = wn.boarding().delete_terminal(response.terminalNumber)
    assert_that(delete_terminal.deactivationDate, is_not(None))

    activate_terminal = wn.boarding().activate_terminal(response.terminalNumber)
    assert_that(activate_terminal.deactivationDate, equal_to(None))