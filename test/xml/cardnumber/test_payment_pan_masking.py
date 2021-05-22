import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from data.xml_requests import payment_avs, payment_level2, \
    account_verification_request, payment_level3, securecard_registration, preauth, payment, unreferenced_refund, \
    offlinepayment, securecard_update, payment_securecard
from model.gateway import PAYMENTRESPONSE, ERROR, CUSTOMFIELD, ACCOUNT_VERIFICATION_RESPONSE, \
    SECURECARDREGISTRATIONRESPONSE, PREAUTHRESPONSE, UNREFERENCEDREFUNDRESPONSE, OFFLINEPAYMENTRESPONSE
from utils import random_card, split_string, generate_hash
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
TERM_ID = '21001'
# Pilot feature #31369 - Mask card number in request params


@pytest.mark.parametrize('order_id', [random_card().cardnumber, 'a' + random_card().cardnumber + 'b'])
def test_pan_masking_same_cardnumber_as_orderid_not_allowed(order_id):
    p = payment_avs()
    p.ORDERID = order_id
    p.CARDNUMBER = order_id
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid ORDERID field'))


@pytest.mark.parametrize('divider, position', [(' ', 4), ('-', 4), ('-', 3), ('', 0)])
def test_pan_masking_same_cardnumber_orderid_divider_not_allowed(divider, position):
    p = payment_avs()
    p.ORDERID = split_string(p.CARDNUMBER, divider, position)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid ORDERID field'))


@pytest.mark.parametrize('divider, position', [(' ', 4), ('-', 4), ('-', 3), ('', 0)])
def test_pan_masking_payment_avs(divider, position):
    p = payment_avs()
    pan = divider + split_string(p.CARDNUMBER, divider) + divider

    p.CARDNUMBER = pan
    p.CARDHOLDERNAME = pan
    p.POSTCODE = pan
    p.EMAIL = pan + '@local.host'
    p.DESCRIPTION = pan
    p.FULL_NAME = pan
    p.ADDRESS1 = pan
    p.ADDRESS2 = pan
    p.REGION = pan
    p.CITY = pan
    p.DEVICEID = pan
    p.BILLTOFIRSTNAME = pan
    p.BILLTOLASTNAME = pan
    p.ISSUENO = pan

    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    response_hash_string = ':'.join([TERM_ID, response.UNIQUEREF, str(p.AMOUNT), response.DATETIME,
                                     response.RESPONSECODE, response.RESPONSETEXT, response.BANKRESPONSECODE,
                                     'someSecretPhrase'])
    assert_that(response.HASH, equal_to(generate_hash(response_hash_string)))


@pytest.mark.parametrize('divider', ['-', ' '])
def test_pan_masking_payment_divider_only(divider):
    p = payment_avs()
    pan = divider * 10
    p.POSTCODE = pan
    p.DESCRIPTION = pan
    p.FULL_NAME = pan
    p.ADDRESS1 = pan
    p.ADDRESS2 = pan
    p.CARDHOLDERNAME = pan
    p.REGION = pan
    p.CITY = pan
    p.DEVICEID = pan
    p.BILLTOFIRSTNAME = pan
    p.BILLTOLASTNAME = pan

    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


@pytest.mark.parametrize('position', [1, 2, 3])
def test_pan_masking_payment_param_differs_from_cardnumber(position):
    p = payment_avs()
    cardnumber = p.CARDNUMBER
    p.CARDHOLDERNAME = split_string(cardnumber, position=position)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_pan_masking_another_cardnumber_as_orderid_allowed():
    p = payment_avs()
    p.ORDERID = random_card().cardnumber
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


@pytest.mark.parametrize('field, additional_data', [
    ('DESCRIPTION', None),
    ('CARDHOLDERNAME', None),
    ('EMAIL', '@abc.ie'),
])
def test_pan_masking_other_fields(field, additional_data):
    p = payment_avs()
    setattr(p, field, p.CARDNUMBER + additional_data if additional_data else p.CARDNUMBER)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    # TODO check open_transaction table's value


@pytest.mark.parametrize('divider, position', [('', 0), (' ', 4), ('-', 4), ('-', 3)])
def test_pan_masking_level_2_fields(divider, position):
    # boarding update terminal to enable level3
    p = payment_level2()
    pan = split_string(p.CARDNUMBER, divider, position)
    p.LEVEL_2_DATA.CUSTOMER_REF_NUMBER = pan
    p.LEVEL_2_DATA.SHIPPING_ADDRESS.FULL_NAME = pan
    p.LEVEL_2_DATA.SHIPPING_ADDRESS.ADDRESS1 = pan
    p.LEVEL_2_DATA.SHIPPING_ADDRESS.ADDRESS2 = pan
    p.LEVEL_2_DATA.SHIPPING_ADDRESS.CITY = pan
    p.LEVEL_2_DATA.SHIPPING_ADDRESS.REGION = pan
    p.LEVEL_2_DATA.SHIPPING_ADDRESS.POSTCODE = pan
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    # TODO check with level_card_data table


@pytest.mark.parametrize('divider, position', [('', 0), (' ', 4), ('-', 4), ('-', 3)])
def test_pan_masking_level_3_fields(divider, position):
    # boarding update terminal to enable level3
    p = payment_level3()
    pan = split_string(p.CARDNUMBER, divider, position)
    p.LEVEL_3_DATA.LINE_ITEMS.LINE_ITEM[0].COMMODITY_CODE = pan
    p.LEVEL_3_DATA.LINE_ITEMS.LINE_ITEM[0].PRODUCT_CODE = pan
    p.LEVEL_3_DATA.LINE_ITEMS.LINE_ITEM[0].DESCRIPTION = pan
    p.LEVEL_3_DATA.LINE_ITEMS.LINE_ITEM[0].UNIT_OF_MEASURE = pan
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    # TODO check with level_card_data table


@pytest.mark.parametrize('divider, position', [(' ', 4), ('-', 4), ('-', 3), ('', 0)])
def test_pan_masking_custom_field(divider, position):
    p = payment_avs()
    p.CUSTOMFIELD = [CUSTOMFIELD(NAME='CustomString', valueOf_=split_string(p.CARDNUMBER, divider, position))]
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    # TODO check for transaction_custom_field table


@pytest.mark.parametrize('cardnumber, cardtype', [
    ('4314229999999913', 'visa'), ('4314220000000056', 'visa'), ('4037660000001115', 'visa'),
    ('4295550031729387', 'visa'), ('4012888818888', 'visa'), ('4111111111111111', 'visa'), ('4012888888881881', 'visa'),
    ('6771771771771771774', 'visa'), ('4222222222222', 'visa'), ('4124939999999990', 'visa'), ('4921818425002311', 'visa'),
    ('4917300800000000', 'visa'), ('679999123456', 'maestro'), ('67999989000002010', 'maestro'), ('6799851000000016', 'maestro'),
    ('6759649826438453', 'maestro'), ('6771771771771771774', 'maestro'), ('6799990100000000019', 'maestro'),
    ('38000000000006', 'diners'), ('6510000000000216', 'discover'), ('370000000000002', 'amex'), ('3088000000000017', 'jcb'),
    ('5424000000000015', 'mastercard'), ('5500000000000004', 'mastercard'), ('5555555555554444', 'mastercard'),
    ('5105105105105100', 'mastercard'), ('5555444433331111', 'mastercard'), ('5437551000000020', 'mastercard'),
    ('5413330000000019', 'mastercard'), ('5223450000000015', 'mastercard'), ('5583420021684448', 'mastercard')
])
def test_pan_masking_orderid_cardnumber_length(cardnumber, cardtype):
    p = payment_avs()
    p.CARDNUMBER = cardnumber
    p.CARDTYPE = cardtype
    p.ORDERID = cardnumber
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid ORDERID field'))


@pytest.mark.parametrize('cardnumber, cardtype', [
    ('6771771771771771774', 'visa'), ('4222222222222', 'visa'),
    ('6799990100000000019', 'maestro'), ('38000000000006', 'diners')])
def test_pan_masking_cardnumber_length(cardnumber, cardtype):
    p = payment_avs()
    pan = split_string(cardnumber, ' ', 4)
    p.CARDNUMBER = cardnumber
    p.CARDTYPE = cardtype
    p.CARDHOLDERNAME = pan
    p.DESCRIPTION = pan
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


@pytest.mark.parametrize('divider', [' ', '-'])
def test_pan_masking_leading_trailing_divider(divider):
    p = payment_avs()
    cardnumber = p.CARDNUMBER
    p.CARDHOLDERNAME = divider + split_string(cardnumber, divider) + divider
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


@pytest.mark.parametrize('divider, position', [(' ', 4), ('-', 4), ('-', 3), ('', 0)])
def test_pan_masking_orderid_preauth(divider, position):
    p = preauth()
    p.ORDERID = split_string(p.CARDNUMBER, divider, position)
    response = wn.xml(TERM_ID).preauth(p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid ORDERID field'))


@pytest.mark.parametrize('divider, position', [('', 0), (' ', 3), (' ', 2), ('-', 4)])
def test_pan_masking_avs_fields_preauth(divider, position):
    p = preauth()
    pan = split_string(p.CARDNUMBER, divider, position)
    p.POSTCODE = pan
    p.PHONE = pan
    p.EMAIL = pan + '@local.host'
    p.DESCRIPTION = pan
    p.FULL_NAME = pan
    p.ADDRESS1 = pan
    p.ADDRESS2 = pan
    p.CARDHOLDERNAME = pan
    p.REGION = pan
    p.CITY = pan
    response = wn.xml(TERM_ID).preauth(p)
    assert_that(response, instance_of(PREAUTHRESPONSE))


@pytest.mark.parametrize('divider', ['', ' ', '-'])
def test_pan_masking_account_verification(divider):
    r = account_verification_request(cardtype='amex')
    pan = split_string(string=r.CARDNUMBER, divider=' ')
    r.CARDHOLDERNAME = pan
    r.ADDRESS1 = pan
    r.ADDRESS2 = pan
    r.POSTCODE = pan
    response = wn.xml(TERM_ID).account_verification(r)
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))


@pytest.mark.parametrize('divider', ['', ' ', '-'])
def test_pan_masking_offline_payment(divider):
    p = offlinepayment()
    pan = split_string(p.CARDNUMBER, divider)
    p.CARDNUMBER = pan
    p.CARDHOLDERNAME = pan
    p.ADDRESS1 = pan
    p.ADDRESS2 = pan
    p.DESCRIPTION = pan
    p.EMAIL = pan + '@local.host'
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(OFFLINEPAYMENTRESPONSE))


@pytest.mark.parametrize('divider', ['', ' ', '-'])
def test_pan_masking_unreference_refund_invalid_orderid(divider):
    p = unreferenced_refund()
    p.ORDERID = split_string(p.CARDDETAILS.CARDNUMBER, divider)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Invalid ORDERID field'))


@pytest.mark.parametrize('divider', ['', ' ', '-'])
def test_pan_masking_unreference_refund_fields(divider):
    p = unreferenced_refund()
    pan = split_string(p.CARDDETAILS.CARDNUMBER, divider)
    p.CARDDETAILS.CARDHOLDERNAME = pan
    p.OPERATOR = pan
    p.DESCRIPTION = pan
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(UNREFERENCEDREFUNDRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))


@pytest.mark.parametrize('divider', ['', ' ', '-'])
def test_pan_masking_fraudreview(divider):
    p = payment()
    p.FRAUDREVIEWSESSIONID = split_string(p.CARDNUMBER, divider)
    response = wn.xml(TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


@pytest.mark.parametrize('divider', ['-'])
def test_pan_masking_3ds_payment(divider):
    p = payment()
    p.MPIREF = '25d7433d30de4a80b6a3'
    p.XID = split_string(p.CARDNUMBER, divider)
    p.CAVV = split_string(p.CARDNUMBER, divider)
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


@pytest.mark.parametrize('divider', ['', ' ', '-'])
def test_pan_masking_securecard_payment(divider):
    sc = securecard_registration()
    secure_card = wn.xml(TERM_ID).secure_card_registration(request=sc, silence=False)
    assert_that(secure_card, instance_of(SECURECARDREGISTRATIONRESPONSE))
    pan = split_string(sc.CARDNUMBER, divider)

    p = payment_securecard(cardreference=secure_card.CARDREFERENCE)
    p.DESCRIPTION = sc.CARDNUMBER
    p.CARDHOLDERNAME = pan
    p.ADDRESS1 = pan
    p.ADDRESS2 = pan
    p.DESCRIPTION = pan
    p.CITY = pan
    p.REGION = pan
    p.EMAIL = pan + '@local.host'
    p.CUSTOMFIELD = [CUSTOMFIELD(NAME='CustomString', valueOf_=split_string(pan, divider))]

    response = wn.xml(TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))

    wn.xml(TERM_ID).secure_card_removal(secure_card.MERCHANTREF, secure_card.CARDREFERENCE)
