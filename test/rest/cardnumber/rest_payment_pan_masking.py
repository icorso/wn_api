import pytest
from hamcrest import assert_that, equal_to, instance_of

from constants import Currency
from data.rest_requests import rest_sale, rest_unreferenced_card_refund
from model.rest import transactionResponse, serviceError, avs, customFieldsType, customField
from utils import split_string
from wnclient import WNClient

wn = WNClient().vagrant.go
TERM_ID = '21001'


@pytest.mark.parametrize('divider', ['', '-', ' '])
def test_rest_keyed_pan_masking(divider):
    request = rest_sale()
    pan = split_string(request.paymentMethod.keyedCard.cardNumber, divider)
    request.customer.city = pan
    request.customer.country = pan
    if divider != ' ':
        request.customer.eMail = f'{pan}@local.host'
    request.customer.region = pan

    request.account.operator = pan
    request.account.deviceId = pan

    request.avs = avs(
        address1=pan,
        address2=pan,
        postCode=pan
    )

    request.paymentMethod.keyedCard.cardHolderName = pan
    request.paymentMethod.keyedCard.cardType = pan

    response = wn.rest(TERM_ID).sale(request=request)
    assert_that(response, instance_of(transactionResponse))


@pytest.mark.parametrize('divider', ['', '-', ' '])
def test_rest_order_id_pan_masking(divider):
    request = rest_sale()
    pan = split_string(request.paymentMethod.keyedCard.cardNumber, divider)
    request.orderId = pan
    response = wn.rest(TERM_ID).sale(request=request)
    assert_that(response, instance_of(serviceError))
    assert_that(response.message, equal_to('Inappropriate PAN usage'))


@pytest.mark.parametrize('divider', ['', '-', ' '])
def test_rest_mobile_number_pan_masking(divider):
    request = rest_sale()
    pan = split_string(request.paymentMethod.keyedCard.cardNumber, divider)
    request.customer.mobileNumber = pan
    response = wn.rest(TERM_ID).sale(request=request)
    assert_that(response, instance_of(serviceError))
    assert_that(response.message, equal_to("Invalid 'sale.arg0.customer.mobileNumber' argument: Invalid Phone Number"))


@pytest.mark.parametrize('divider', ['', ' ', '-'])
def test_rest_custom_field_pan_masking(divider):
    request = rest_sale()
    pan = split_string(request.paymentMethod.keyedCard.cardNumber, divider)
    request.customFields = customFieldsType([customField(name='CustomString', value=pan)])
    response = wn.rest(TERM_ID).sale(request=request)
    assert_that(response, instance_of(transactionResponse))
    # see issue #33415


@pytest.mark.parametrize('divider', ['', '-', ' '])
def test_rest_unreferenced_refund_pan_masking(divider):
    request = rest_unreferenced_card_refund(currency=Currency.USD)
    pan = split_string(request.refundMethod.unreferenced.cardDetails.cardNumber, divider)
    request.customer.city = pan
    request.customer.country = pan
    if divider != ' ':
        request.customer.eMail = f'{pan}@local.host'
    request.customer.region = pan

    request.account.operator = pan
    request.account.deviceId = pan

    request.refundMethod.unreferenced.reason = pan

    refund_response = wn.rest(TERM_ID).refund(request=request, currency=Currency.USD)
    assert_that(refund_response, instance_of(transactionResponse))
    assert_that(refund_response.authorizedAmount, equal_to(float(request.amount.amount) * -1))
