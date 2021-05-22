import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import SecureCard, Currency
from data.xml_requests import payment, preauth, payment_securecard, payment_level3, payment_level2
from model.gateway import ERROR, PAYMENTRESPONSE, CUSTOMFIELD
from utils import random_amount, SurchargeAmount, random_surcharge_percent, random_card
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
wn_boarding = WNClient().vagrant.go.boarding()
TERM_ID = '21001'
MULTICURRENCY_TERM_ID = '21002'
SUR_PERCENT = 4


@pytest.mark.parametrize('cardtype', ['visa'])
def test_payment_surcharge_allowed_cards(cardtype):
    amounts = SurchargeAmount(random_amount(), random_surcharge_percent())
    wn_boarding.update_terminal_surcharge(TERM_ID, True, amounts.percentage, silence=True)

    request = payment_level2(cardtype=cardtype)
    request.AMOUNT = amounts.total_amount
    request.BYPASS_SURCHARGE = False
    request.EMAIL = fake.free_email()
    response = wn.xml(terminal_id=TERM_ID).payment(request=request)

    assert_that(response.RESPONSECODE, equal_to('A'))

    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.UNIQUEREF)
    assert_that(db_surcharge.amount, equal_to(amounts.surcharge))


def test_payment_surcharge_cards_not_allowed():
    amounts = SurchargeAmount(random_amount(), random_surcharge_percent())
    request = payment(cardtype='VISA DEBIT')
    request.CARDNUMBER = SecureCard.VISA_DEBIT.cardnumber
    request.AMOUNT = amounts.total_amount
    request.BYPASS_SURCHARGE = False
    response = wn.xml(terminal_id=TERM_ID).payment(request=request)

    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Given card type does not support surcharges'))


def test_payment_surcharge_routing_terminal():
    # Terminal 21999 rule: Product SKU = 21001 route to terminal 21001
    amounts = SurchargeAmount(random_amount(), random_surcharge_percent())
    wn_boarding.update_terminal_surcharge(TERM_ID, True, amounts.percentage)

    request = payment()
    request.CUSTOMFIELD = [CUSTOMFIELD(NAME='Product SKU', valueOf_=TERM_ID)]
    request.AMOUNT = amounts.total_amount
    request.BYPASS_SURCHARGE = False
    response = wn.xml(terminal_id='21999').payment(request=request)

    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.SURCHARGE_FEE, equal_to(amounts.surcharge))

    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.UNIQUEREF)
    assert_that(db_surcharge.amount, equal_to(amounts.surcharge))


def test_payment_surcharge_multicurrency_terminal():
    amounts = SurchargeAmount(random_amount(), random_surcharge_percent(), currency=Currency.KWD)
    wn_boarding.update_terminal_surcharge(MULTICURRENCY_TERM_ID, True, amounts.percentage)

    request = payment(currency=Currency.KWD).is_multicurrency(True)
    request.CARDNUMBER = '4062608182398294'
    request.AMOUNT = amounts.total_amount
    # request.CURRENCY = 'KWD'
    request.BYPASS_SURCHARGE = False
    response = wn.xml(MULTICURRENCY_TERM_ID).payment(request=request)

    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.SURCHARGE_FEE, equal_to(amounts.surcharge))

    db_surcharge = wn.db(terminal_number=MULTICURRENCY_TERM_ID).get_transaction_surcharge(uniqueref=response.UNIQUEREF)
    assert_that(db_surcharge.amount, equal_to(amounts.surcharge))


@pytest.mark.parametrize('cardtype, req', [('amex', payment()), ('amex', preauth())])
def test_payment_surcharge_cardtype_not_alowed(cardtype, req):
    req.CARDNUMBER = random_card(cardtype).cardnumber
    req.BYPASS_SURCHARGE = False

    response = wn.xml(terminal_id=TERM_ID).payment(request=req)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Given card type does not support surcharges'))


@pytest.mark.parametrize('req', [payment(), preauth()])
def test_payment_bypass_surcharge_default_value(req):
    payment = SurchargeAmount(random_amount(), random_surcharge_percent())
    wn_boarding.update_terminal_surcharge(TERM_ID, True, payment.percentage)
    # Selfcare > Settings > Terminal : Surcharges is turned on
    req.AMOUNT = payment.total_amount

    response = wn.xml(terminal_id=TERM_ID).payment(request=req)
    assert_that(response.RESPONSECODE, equal_to('A'))
    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.UNIQUEREF)
    assert_that(db_surcharge.amount, equal_to(payment.surcharge))


@pytest.mark.parametrize('req', [payment(), preauth()])
def test_surcharge_bypass_surcharge_true(req):
    payment = SurchargeAmount(random_amount(), random_surcharge_percent())
    wn_boarding.update_terminal_surcharge(terminal_number=TERM_ID, allow_surcharge=True, surcharge_percent=payment.percentage)
    # Selfcare > Settings > Terminal : Surcharges is turned on
    req.AMOUNT = payment.total_amount
    req.BYPASS_SURCHARGE = True

    response = wn.xml(terminal_id=TERM_ID).payment(request=req)
    assert_that(response.RESPONSECODE, equal_to('A'))
    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.UNIQUEREF)
    assert_that(db_surcharge, equal_to(None))


@pytest.mark.parametrize('req', [payment(), preauth()])
def test_payment_bypass_surcharge_type_validation(req):
    wn_boarding.update_terminal_surcharge(terminal_number=TERM_ID, allow_surcharge=True, surcharge_percent=SUR_PERCENT)

    req.BYPASS_SURCHARGE = ''
    response = wn.xml(terminal_id=TERM_ID).payment(request=req)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to("cvc-datatype-valid.1.2.1: '' is not a valid value for 'boolean'."))


def test_payment_bypass_surcharge_ignores():
    wn_boarding.update_terminal_surcharge(terminal_number=TERM_ID, allow_surcharge=False)

    request = payment()
    request.BYPASS_SURCHARGE = False
    response = wn.xml(terminal_id=TERM_ID).payment(request=request)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.UNIQUEREF)
    assert_that(db_surcharge, equal_to(None))


def test_payment_surcharge_credit_securecard_payment():
    amounts = SurchargeAmount(random_amount(), random_surcharge_percent())
    wn_boarding.update_terminal_surcharge(TERM_ID, True, amounts.percentage)

    request = payment_securecard(cardreference=SecureCard.VISA.card_ref)
    request.AMOUNT = amounts.total_amount
    request.BYPASS_SURCHARGE = False
    response = wn.xml(terminal_id=TERM_ID).payment(request=request)
    assert_that(response.RESPONSECODE, equal_to('A'))

    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.UNIQUEREF)
    assert_that(db_surcharge.amount, equal_to(amounts.surcharge))


def test_payment_surcharge_debit_securecard_payment():
    amounts = SurchargeAmount(random_amount(), random_surcharge_percent())
    wn_boarding.update_terminal_surcharge(TERM_ID, True, amounts.percentage)

    request = payment_securecard(cardreference=SecureCard.VISA_DEBIT.card_ref)
    request.AMOUNT = amounts.total_amount
    request.BYPASS_SURCHARGE = False
    response = wn.xml(terminal_id=TERM_ID).payment(request=request)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Given card type does not support surcharges'))