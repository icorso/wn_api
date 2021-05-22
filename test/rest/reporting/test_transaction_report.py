from faker import Factory
from hamcrest import assert_that, equal_to, instance_of

from model.rest import transactionReport
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().vagrant.wn
TERM_ID = '22005'


def test_rest_transaction_report():
    cv = 'Maria Frank'
    tk = wn.rest(TERM_ID).temporary_key().key
    s = wn.rest(TERM_ID).transaction_report(terminal_number=TERM_ID, api_key=tk, settlement_date='20-02-2020',
                                            criterion_type='OPERATOR', criterion_value=cv)
    assert_that(s, instance_of(transactionReport))
    assert_that(s.criterionValue, equal_to(cv))
