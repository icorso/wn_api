from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.rest_requests import rest_sale, rest_tip
from model.rest import tipType, transactionResponse
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21001'


def test_percentage_tip_rest_payment():
        amount = 10
        p = rest_sale(amount=amount)
        tip = rest_tip(amount=0.2, tip_type=tipType.PERCENTAGE)
        tip.percentage = 2
        p.tip = tip
        p.account.terminalType = 'CHP'

        response = wn.rest(terminal_id=TERM_ID, content_type='json').sale(request=p)
        assert_that(response, instance_of(transactionResponse))
        assert_that(response.code, equal_to('A'))
