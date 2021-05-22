from faker import Factory

from data.xml_requests import payment
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().local.go
TERM_ID = '21001'


def test_elavon_approved_payment():
    p = payment()
    p.TERMINALID = TERM_ID
    p.ORDERID = 'HPP_' + str(fake.random_number(7, False))
    wn.hpp(terminal_id=TERM_ID).paymentpage(p)


def test_elavon_cvv_error_payment():
    p = payment()
    p.CVV = '274273647'
    p.TERMINALID = TERM_ID
    p.ORDERID = 'HPP_' + str(fake.random_number(7, False))
    wn.hpp(terminal_id=TERM_ID).paymentpage(p)


def test_elavon_securecard_reference_payment():
    p = payment()
    p.SECURECARDMERCHANTREF = 'SC_' + str(fake.random_number(7, False))
    p.TERMINALID = TERM_ID
    p.ORDERID = 'HPP_' + str(fake.random_number(7, False))
    wn.hpp(terminal_id=TERM_ID).paymentpage(p)
