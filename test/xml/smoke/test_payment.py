import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency
from data.xml_requests import payment_chp, payment, payment_androidpay, payment_avs
from model.boarding import terminal
from model.gateway import PAYMENTRESPONSE, ERROR
from utils import random_text
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
go = WNClient().vagrant.go
TERM_ID = '21001'
VISA_DECLINED = '4716568913084649'


def test_3ds_payment():
    # TODO use xml request
    p = payment()
    p.CARDNUMBER = '5463855637581592'
    p.CARDEXPIRY = '0120'
    p.AMOUNT = 10.01
    p.MPIREF = '5463855637581592abcd'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_elavon_keyed_card_avs_payment():
    response = wn.xml(terminal_id='22001').payment(payment_avs())
    assert_that(response, instance_of(PAYMENTRESPONSE))


@pytest.mark.parametrize('field, max_length', [
    ('CARDHOLDERNAME', 50),
    ('POSTCODE', 50),
    ('ADDRESS1', 50),
    ('ADDRESS2', 50),
    ('CARDNUMBER', 40),
    ('CARDEXPIRY', 4),
])
def test_payment_max_length(field, max_length):

    av = payment_avs()
    field_value = random_text(max_length + 1)
    setattr(av, field, field_value)
    response = go.xml(TERM_ID).payment(av)
    expected_text = "cvc-maxLength-valid: Value '%s' with length = '%s' is not facet-valid with respect to maxLength " \
                    "'%s' for type '#AnonType_%s'."
    if field == 'CARDEXPIRY':
        expected_text = expected_text.replace('maxLength', 'length')
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to(expected_text % (field_value,
                                                                str(max_length + 1), str(max_length), field)))


def test_chp_payment():
    response = go.xml(TERM_ID).payment(payment_chp())
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_androidpay_payment():
    response = wn.xml('22015').payment(payment_androidpay(currency=Currency.USD))
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_keyed_threatmetrix_card_payment():
    t = go.boarding().get_terminal(TERM_ID)
    t.securityFraud.threatMetrixEnabled = True
    t.securityFraud.threatMetrixApiKey = 'w2v4h5yb1c2hrbaj'
    t.securityFraud.threatMetrixOrgId = '1008xb81'
    t.securityFraud.threatMetrixPolicyName = 'review_all'
    t.securityFraud.threatMetrixRejectOnError = False
    t.securityFraud.threatMetrixRiskScoreThreshold = None
    r = go.vagrant.go.boarding().update_terminal(request=t)
    assert_that(r, instance_of(terminal))

    p = payment()
    p.FRAUDREVIEWSESSIONID = fake.md5()
    response = go.xml(TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.FRAUDREVIEWRESPONSE.FRAUDREVIEWSTATUS, equal_to('REVIEW'))

    t.securityFraud.threatMetrixEnabled = False
    go.boarding().update_terminal(request=t)
    assert_that(r, instance_of(terminal))
