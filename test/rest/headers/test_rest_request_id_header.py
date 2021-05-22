from faker import Factory
from hamcrest import assert_that, equal_to, instance_of

from data.rest_requests import rest_sale
from model.rest import transactionResponse
from wnclient import WNClient

fake = Factory.create()

TERM_ID = '21001'


def test_rest_cloud_header_normal():
    # 2020-09-10 11:50:02,900 DEBUG [REST300056265128603] [default task-15] [com.worldnettps.common.CustomHttpHandler] - Deleting request id:REST300056265128603
    # 2020-09-10 11:50:02,900 DEBUG [REST300056265128603] [default task-15] [com.worldnettps.common.CustomHttpHandler] - processing time:967 ms
    headers = {'X-Cloud-Trace-Context': "%s/%s" % (str(fake.random_number(32)), 'REST' + str(fake.random_number(16)))}
    r = rest_sale()
    response = WNClient().local.go.with_headers(headers).rest(TERM_ID).sale(r)
    assert_that(response, instance_of(transactionResponse))
    assert_that(response.code, equal_to('A'))
