import pytest
from faker import Factory
from hamcrest import assert_that, instance_of

from data.rest_requests import rest_securecard_sale, rest_keyed_securecard
from model.rest import secureCardRegisterRestResponse, transactionResponse
from utils import split_string
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21001'


@pytest.mark.parametrize('divider', [''])
def test_rest_securecard_payment_fields_pan_masking(divider):
    r = rest_keyed_securecard()
    securecard_response = wn.rest(TERM_ID).create_securecard(r)
    assert_that(securecard_response, instance_of(secureCardRegisterRestResponse))

    card_reference = securecard_response.cardReference
    pan = split_string(r.tokenMethod.keyedSecureCard.cardNumber, divider)
    request = rest_securecard_sale(cardreference=card_reference)
    request.customer.city = pan
    request.customer.country = pan
    request.customer.eMail = f'{pan}@local.host'

    request.account.operator = pan
    request.account.deviceId = pan

    response = wn.rest(TERM_ID).sale(request=request)
    assert_that(response, instance_of(transactionResponse))
