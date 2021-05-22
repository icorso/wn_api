from hamcrest import assert_that, instance_of

from data.xml_requests import securecard_registration, payment_applepay_visa
from model.gateway import SECURECARDREGISTRATIONRESPONSE, PAYMENTRESPONSE
from wnclient import WNClient

wn = WNClient().vagrant.wn
TERM_ID = '22005'


def test_fdrc_securecard_registration_ok():
    sc = securecard_registration(cvv='999')
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


def test_fdrc_securecard_registration_cvv_falied():
    sc = securecard_registration(cvv='111')
    response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(response, instance_of(SECURECARDREGISTRATIONRESPONSE))


def test_fdrc_applepay_payment():
    p = payment_applepay_visa()
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
