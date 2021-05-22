from faker import Factory
from hamcrest import assert_that, instance_of

from constants import Currency
from model.gateway import PREAUTHRESPONSE, PREAUTHCOMPLETIONRESPONSE, REFUNDRESPONSE, ERROR
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21004'


def test_tango_preauth_create():
    response = wn.xml(TERM_ID).preauth(currency=Currency.CAD)
    assert_that(response, instance_of(PREAUTHRESPONSE))
"""
See tango request params: 
"TxTp":"RESA" - this is preauth
"SvcAttr":"IRES" - preauth initial reservation 
"""


def test_tango_preauth_void():
    # full refund
    response = wn.xml(TERM_ID).preauth(currency=Currency.CAD)
    assert_that(response, instance_of(PREAUTHRESPONSE))

    refund_preauth_response = wn.xml(TERM_ID).refund(response.UNIQUEREF, response.AMOUNT, Currency.CAD)
    assert_that(refund_preauth_response, instance_of(REFUNDRESPONSE))


def test_tango_preauth_partial_refund_not_allowed():
    # full refund
    response = wn.xml(TERM_ID).preauth(currency=Currency.CAD)
    assert_that(response, instance_of(PREAUTHRESPONSE))

    refund_preauth_response = wn.xml(TERM_ID).refund(response.UNIQUEREF, round(response.AMOUNT/2), Currency.CAD)
    assert_that(refund_preauth_response, instance_of(REFUNDRESPONSE))


def test_tango_preauth_completion_same_amount():
    preauth_response = wn.xml(TERM_ID).preauth(currency=Currency.CAD)
    assert_that(preauth_response, instance_of(PREAUTHRESPONSE))

    preauth_completion_response = wn.xml(TERM_ID).preauthcompletion(preauth_response.UNIQUEREF,
                                                                    preauth_response.AMOUNT,
                                                                    currency=Currency.CAD)
    assert_that(preauth_completion_response, instance_of(PREAUTHCOMPLETIONRESPONSE))


def test_tango_preauth_completion_different_amount():
    preauth_response = wn.xml(TERM_ID).preauth(currency=Currency.CAD)
    assert_that(preauth_response, instance_of(PREAUTHRESPONSE))

    preauth_completion_response = wn.xml(TERM_ID).preauthcompletion(preauth_response.UNIQUEREF,
                                                                    preauth_response.AMOUNT - 1,
                                                                    currency=Currency.CAD)
    assert_that(preauth_completion_response, instance_of(PREAUTHCOMPLETIONRESPONSE))


def test_tango_preauth_completion_already_voided():
    preauth_response = wn.xml(TERM_ID).preauth(currency=Currency.CAD)
    assert_that(preauth_response, instance_of(PREAUTHRESPONSE))

    refund_preauth_response = wn.xml(TERM_ID).refund(preauth_response.UNIQUEREF, preauth_response.AMOUNT, Currency.CAD)
    assert_that(refund_preauth_response, instance_of(REFUNDRESPONSE))

    preauth_completion_response = wn.xml(TERM_ID).preauthcompletion(preauth_response.UNIQUEREF,
                                                                    preauth_response.AMOUNT,
                                                                    currency=Currency.CAD)
    assert_that(preauth_completion_response, instance_of(ERROR))
    assert_that(preauth_completion_response.ERRORSTRING, "Invalid Transaction Status")

