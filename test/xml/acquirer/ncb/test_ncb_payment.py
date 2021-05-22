import pytest
from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import Currency, EmvTlv
from data.rest_requests import rest_emv_tlv_sale
from data.xml_requests import payment_chp, payment, payment_chp_jets, payment_chp_ncb
from model.gateway import PAYMENTRESPONSE, ERROR
from model.rest import terminalType, paymentMethod, emvtlv
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.ncb
TERM_ID = '23001'


def test_ncb_internet_card_payment_not_supported():
    p = payment(currency=Currency.JMD)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(ERROR))
    assert_that(response.ERRORSTRING, equal_to('Terminal does not support Internet transactions'))


def test_ncb_chp_payment_ok():
    p = payment_chp(currency=Currency.JMD)
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_ncb_chp_payment_response_code_85():
    # simulator version 2.2.2.r343
    p = payment_chp(currency=Currency.JMD)
    p.AMOUNT = 6
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('A'))
    assert_that(response.RESPONSETEXT, equal_to('No reason to decline'))


def test_ncb_chp_payment_jets():
    p = payment_chp_jets()
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_ncb_chp_payment_ncb_card():
    p = payment_chp_ncb()
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


@pytest.mark.parametrize('tlv, cardtype', [
    (EmvTlv.CONTACTLESS_ICC, 'visa'),
    # (EmvTlv.CONTACTLESS_ICC_MC_CREDIT, 'mastercard'),
    # (EmvTlv.CONTACTLESS_ICC_DISCOVER, 'discover')
])
def test_ncb_emv(tlv, cardtype):
    p = rest_emv_tlv_sale(device_type='WISEPAD')
    p.account.terminalType = terminalType.CHP
    p.paymentMethod = paymentMethod(
        emvTlv=emvtlv(
            contactless='true',
            cardType=cardtype,
            ksn='88888835400002200001',
            # tlvString='4F07A0000000031010500A4d41535445524341524457134444333322221111D20121011796251900000f5A08444433332222111182027C008407A00000000310108A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950508800080009A032007159B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000001010009F03060000000000009F0607A00000000310109F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120210a00003240000000000000000000000ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000100019F1E0831323334353637389F21030931409F260848438A8F1AD9A0589F2701809F33036028C89F34035E03009F3501219F360200019F37047BC6785F9F3901079F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'
            tlvString=tlv.value
        )
    )
    response = wn.rest(terminal_id=TERM_ID).sale(currency=Currency.JMD, request=p)
