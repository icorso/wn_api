from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import payment_level2
from model.gateway import PAYMENTRESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21010'


def test_tango_level2_payment_approved():
    p = payment_level2(cardtype='visa')
    p.AUTOREADY = 'C'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

