from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import preauth
from model.gateway import PREAUTHCOMPLETIONRESPONSE
from utils import random_amount, SurchargeAmount
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
wn_boarding = WNClient().vagrant.go.boarding()
TERM_ID = '21001'
SUR_PERCENT = 4


def test_preauth_completion_exact_amount():
    payment = SurchargeAmount(random_amount(), SUR_PERCENT)
    wn_boarding.update_terminal_surcharge(terminal_number=TERM_ID, allow_surcharge=True, surcharge_percent=SUR_PERCENT)
    # perform pre-auth
    request = preauth()
    request.AMOUNT = payment.total_amount
    request.BYPASS_SURCHARGE = False
    response = wn.xml(terminal_id=TERM_ID).payment(request=request)
    assert_that(response.RESPONSECODE, equal_to('A'))
    # complete pre-auth
    completion_response = wn.xml(TERM_ID).preauthcompletion(uniquerf=response.UNIQUEREF, amount=payment.total_amount)
    assert_that(completion_response, instance_of(PREAUTHCOMPLETIONRESPONSE))
    assert_that(completion_response.RESPONSECODE, equal_to('A'))
    # compare with the DB
    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.UNIQUEREF)
    assert_that(db_surcharge.amount, equal_to(payment.surcharge))


def test_preauth_completion_less_than_amount():
    payment = SurchargeAmount(random_amount(), SUR_PERCENT)
    completion_payment = SurchargeAmount(round(payment.amount/2, 2), SUR_PERCENT)
    wn_boarding.update_terminal_surcharge(terminal_number=TERM_ID, allow_surcharge=True, surcharge_percent=SUR_PERCENT)
    # perform pre-auth
    request = preauth(amount=payment.total_amount)
    request.BYPASS_SURCHARGE = False
    response = wn.xml(terminal_id=TERM_ID).payment(request=request)
    assert_that(response.RESPONSECODE, equal_to('A'))
    # complete pre-auth
    completion_response = wn.xml(TERM_ID).preauthcompletion(uniquerf=response.UNIQUEREF, amount=completion_payment.total_amount)
    assert_that(completion_response, instance_of(PREAUTHCOMPLETIONRESPONSE))
    assert_that(completion_response.RESPONSECODE, equal_to('A'))
    # compare with the DB
    db_surcharge = wn.db(terminal_number=TERM_ID).get_transaction_surcharge(uniqueref=response.UNIQUEREF)
    assert_that(db_surcharge.amount, equal_to(completion_payment.surcharge))
