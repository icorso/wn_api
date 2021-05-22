from faker import Factory
from hamcrest import assert_that, equal_to, instance_of

from data.rest_requests import rest_sale, rest_transaction_update
from model.rest import transactionResponse, response, customerDetails
from utils import random_amount
from wnclient import WNClient

fake = Factory.create()

wn = WNClient().local.go
TERM_ID = '21001'


def test_rest_trasnsaction_update_customer_details():
    email = fake.free_email()
    mobile_number = str(fake.random_number(10))
    sale_request = rest_sale(random_amount())
    sale_request.account.terminalType = 'MOTO'
    sale_request.account.terminalId = TERM_ID
    s = wn.rest(TERM_ID).sale(request=sale_request)
    assert_that(s, instance_of(transactionResponse))

    r = rest_transaction_update()
    r.account.terminalType = 'MOTO'
    r.customerDetails = customerDetails(eMail=email, mobileNumber=mobile_number)
    r.uniqueRef = s.uniqueRef
    tu_response = wn.rest(TERM_ID).transaction_update(request=r)
    db_txn = wn.db(terminal_number=TERM_ID).get_transaction(uniqueref=s.uniqueRef)
    assert_that(tu_response, instance_of(response))
    assert_that(tu_response.description, equal_to('Notifications applied and sent'))
    assert_that(db_txn.cardholderemail, equal_to(email))
    assert_that(db_txn.mobilenumber, equal_to(mobile_number))

