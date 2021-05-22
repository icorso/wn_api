from faker import Factory
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from model.gateway import PAYMENTRESPONSE, PREAUTHRESPONSE, PREAUTHCOMPLETIONRESPONSE
from utils import generate_hash
from wnclient import WNClient

fake = Factory.create()
go = WNClient().vagrant.go
TERM_ID = '21001'


def test_keyed_payment_response_hash():
    response = go.xml(terminal_id=TERM_ID).payment(is_multicurrency=False)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.HASH, equal_to(generate_hash(response.hash_string)), "Response HASH doesn't correspond "
                                                                              "to expected value")


def test_preauth_response_hash():
    response = go.xml(terminal_id=TERM_ID, terminal_secret='someSecretPhrase').preauth(is_multicurrency=False)
    assert_that(response, instance_of(PREAUTHRESPONSE))
    assert_that(response.HASH, equal_to(generate_hash(response.hash_string)), "Response HASH doesn't correspond "
                                                                              "to expected value")


def test_preauth_completion_response_hash():
    response = go.xml(terminal_id=TERM_ID, terminal_secret='someSecretPhrase').preauth(is_multicurrency=False)
    assert_that(response, instance_of(PREAUTHRESPONSE))

    completion_response = go.xml(terminal_id=TERM_ID, terminal_secret='someSecretPhrase').preauthcompletion(
        uniquerf=response.UNIQUEREF, amount=response.AMOUNT, is_multicurrency=False
    )
    assert_that(completion_response, instance_of(PREAUTHCOMPLETIONRESPONSE))
    assert_that(completion_response.HASH, equal_to(generate_hash(completion_response.hash_string)),
                "Response HASH doesn't correspond to expected value")
