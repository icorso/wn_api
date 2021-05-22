from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import PaynomixCard
from data.xml_requests import preauth
from model.gateway import PREAUTHRESPONSE
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.wn
TERM_ID = '22015'


def test_paynomix_preauth_success():
    p = preauth()
    p.CARDNUMBER = PaynomixCard.rand().cardnumber
    response = wn.xml(terminal_id=TERM_ID).preauth(request=p)
    assert_that(response, instance_of(PREAUTHRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))

