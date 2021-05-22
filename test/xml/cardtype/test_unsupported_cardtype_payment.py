from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import TerminalType, SecureCard
from data.xml_requests import payment, payment_chp, payment_securecard, \
    payment_applepay_mastercard_3ds, unreferenced_refund, account_verification_request
from model.gateway import PAYMENTRESPONSE, ERROR
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.go
wn_boarding = WNClient().local.go.boarding
TERM_ID = '21001'
TERM_ID_MULTICURRENCY = '21002'
INSTAPAYMENT_CARD = '6385087787065456'


def test_account_verification_unsupported_by_acquirer():
    r = account_verification_request(cardtype='amex')
    response = wn.xml(TERM_ID).account_verification(r)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Unsupported CARDTYPE'))


def test_account_verification_unsupported_by_terminal():
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, ['visa'], silence=True)
    r = account_verification_request(cardtype='mastercard')
    response = wn.xml(TERM_ID).account_verification(r)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Unsupported CARDTYPE'))
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)


def test_account_verification_unsupported_totally():
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, ['visa'], silence=True)
    r = account_verification_request()
    r.CARDNUMBER = INSTAPAYMENT_CARD
    response = wn.xml(TERM_ID).account_verification(r)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid card type'))
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)


def test_chp_not_supported_and_not_determined_card():
    p = payment_chp()
    p.TRACKDATA = ';%s=241210114991888?' % INSTAPAYMENT_CARD
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_internet_not_supported_and_not_determined_card():
    p = payment()
    p.CARDNUMBER = INSTAPAYMENT_CARD
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_not_supported_cardtype_by_acquirer():
    """
    WARN  [default task-16] [com.merchant.XMLPaymentServlet] - AMEX card type is not supported by terminal 21001
    INFO  [default task-16] [com.merchant.XMLPaymentServlet] - AMEX card type is not supported by acquirer of
          the terminal: 21001
    """
    p = payment(cardtype='amex')
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Unsupported CARDTYPE'))


def test_internet_payment_unsupported_cardtype_by_terminal():
    """
    WARN  [default task-16] [com.merchant.XMLPaymentServlet] - MASTERCARD card type is not supported by terminal 21001
    """
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, ['visa'], silence=True)
    p = payment(cardtype='mastercard')
    p.CARDTYPE = 'VISA'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Unsupported CARDTYPE'))
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)


def test_chp_payment_unsupported_cardtype_by_terminal():
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, ['mastercard'], silence=True)
    response = wn.xml(terminal_id=TERM_ID).payment(request=payment_chp())
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Unsupported CARDTYPE'))
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)


def test_chp_payment_unsupported_cardtype_by_acquirer():
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)
    response = wn.xml(terminal_id=TERM_ID).payment(request=payment_chp(cardtype='amex'))
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Unsupported CARDTYPE'))


def test_unsupported_cardtype_by_acquirer_in_multicurrency_terminal():
    wn_boarding().with_terminal(TERM_ID_MULTICURRENCY).update_terminal_cards(TERM_ID, ['visa'], silence=True)
    p = payment(cardtype='amex').is_multicurrency(True)
    response = wn.xml(terminal_id=TERM_ID_MULTICURRENCY).payment(request=p)
    assert_that(response.ERRORSTRING, equal_to('Unsupported CARDTYPE'))
    assert_that(response, instance_of(ERROR))


def test_securecard_payment_unsupported_by_terminal_cardtype():
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, ['visa'], silence=True)
    p = payment_securecard(cardreference=SecureCard.MASTERCARD.card_ref)
    p.TERMINALTYPE = TerminalType.INTERNET,
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid Card Type'))
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence= True)


def test_securecard_payment_unsupported_by_acquirer_card():
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)
    p = payment_securecard(cardreference=SecureCard.AMEX.card_ref)
    p.TERMINALTYPE = TerminalType.INTERNET,
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid Card Type'))


def test_unreferenced_refund_unsupported_cardtype_by_acquirer():
    response = wn.xml(terminal_id=TERM_ID).payment(request=unreferenced_refund(cardtype='amex'))
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Unsupported CARDTYPE'))


def test_unreferenced_refund_unsupported_cardtype_by_terminal():
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, ['visa'], silence=True)
    response = wn.xml(terminal_id=TERM_ID).payment(request=unreferenced_refund(cardtype='mastercard'))
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Unsupported CARDTYPE'))
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)


def test_applepay_unsupported_cardtype_by_terminal():
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, ['visa'], silence=True)
    response = wn.xml(terminal_id=TERM_ID).payment(payment_applepay_mastercard_3ds())
    assert_that(response, instance_of(PAYMENTRESPONSE))
    wn_boarding().with_terminal(TERM_ID).update_terminal_cards(TERM_ID, silence=True)
