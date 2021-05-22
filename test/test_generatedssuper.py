from io import BytesIO

import pytest
from hamcrest import assert_that, equal_to, has_length, has_property, not_, instance_of, none

from constants import Currency
from model.gateway import PAYMENT, parseLiteral, CUSTOMFIELD
from model.rest import sale, hash as rhash, amount, account


def test_deserialization():
    orderid = b'ORDER001'
    parsed = parseLiteral(silence=True, inFileName=BytesIO(b'''<?xml version='1.0' encoding='utf-8'?>
    <PAYMENT>
      <ORDERID>%s</ORDERID>
      <CUSTOMFIELD NAME="cfone">vfVal1</CUSTOMFIELD>
      <CUSTOMFIELD NAME="cftwo">vfVal2</CUSTOMFIELD>
    </PAYMENT>''' % orderid))
    assert_that(parsed, instance_of(PAYMENT))
    assert_that(parsed.ORDERID, equal_to(orderid.decode("utf-8")))
    assert_that(parsed.CUSTOMFIELD, has_length(2))


def test_set_secret_and_hash_field():
    expected_hash = 'd50e85c861acf6a4b96daddc5601227b584ccc04620221c15a6580be4ea7aa1f79682b9f17f9f62989109cfe5c8f3cd2' \
                    'd03524c4f2649927480ba8ecc70940a7'
    payment = PAYMENT(
        TERMINALID='20301',
        ORDERID='ORD0001',
        CURRENCY='USD',
        AMOUNT=2.34,
        DATETIME='02-10-2018'
    ).with_secret('anotherSecretPhrase')
    payment.xml()
    assert_that(payment.HASH, equal_to(expected_hash))


def test_with_field_method():
    cardholder_name = 'Card Holder'
    terminal_type = 1
    order_id = 'ORD0002'
    expected_hash = '39b28db2daaa0455878a8d71e0c584baa080b392f59806d82d7818a1f9ad47ff817e0f354daf110432b11bb95b621f26' \
                    'ef2ff838ffe30bbe48a97b3c8423c9bb'
    payment = PAYMENT(
        TERMINALID='20301',
        ORDERID='ORD0001',
        CURRENCY='USD',
        AMOUNT=2.34,
        DATETIME='02-10-2018'
    ).with_field(AUTOREADY='Y', CARDHOLDERNAME=cardholder_name, ORDERID=order_id)
    payment.with_field(**{'TERMINALTYPE': terminal_type})
    payment.xml()
    assert_that(payment.HASH, equal_to(expected_hash))
    assert_that(payment.CARDHOLDERNAME, equal_to(cardholder_name))
    assert_that(payment.TERMINALTYPE, equal_to(terminal_type))


def test_without_field_method():
    expected_hash = '118bfce53853d8462523673e9c2804f2a320e54785690e7e7b792a2e16b6c6932ea7f1108a16b08b1227d1d57f1b200' \
                    '8f9ae0b952c9257b330561483eba58b51'
    payment = PAYMENT(
        TERMINALID='20301',
        ORDERID='ORD0001',
        CURRENCY=Currency.USD.name,
        AMOUNT=2.34,
        DATETIME='02-10-2018'
    ).without_field('ORDERID', 'NOSUCHFIELD')
    payment.xml()
    assert_that(payment.HASH, equal_to(expected_hash))
    assert_that(payment.ORDERID, none())
    assert_that(payment, not_(has_property('NOSUCHFIELD')))


def test_set_hash_field_with_default_secret():
    expected_hash = '27d4a4aa11e1581b354057dbdec23aa2d4f9f69d0116726aaf2b7f9dd1396dd4562ea52a6aabe7a874bd24bbd25a6dd5' \
                    '30f8b1859192b5dfa0b35dc3abaf8f8e'
    payment = PAYMENT(
        TERMINALID='20301',
        ORDERID='ORD0001',
        CURRENCY='USD',
        AMOUNT=2.34,
        DATETIME='02-10-2018'
    )
    payment.is_multicurrency(False).xml()
    assert_that(payment.HASH, equal_to(expected_hash))


@pytest.mark.parametrize("multicurrency", [True, 1, 'abc'])
def test_multicurrency(multicurrency):
    expected_hash = '3fbd820015388f3edcffe6047f480067ff961a9ec0bfafa3845b27be0bb2c76efaca2b4ea7ea4c9692e8fb9032cc20fa' \
                    'db43a0c742a8188fbadead6d4309a4c1'
    payment = PAYMENT(
        TERMINALID='20301',
        ORDERID='ORD0001',
        CURRENCY='USD',
        AMOUNT=2.34,
        CUSTOMFIELD=[
            CUSTOMFIELD(NAME='cfname1', valueOf_='cfval1'),
            CUSTOMFIELD(NAME='cfname2', valueOf_='cfval2'),
        ],
        DATETIME='02-10-2018'
    ).is_multicurrency(multicurrency)
    payment.xml()  # calculates and insert a hash value to the HASH field
    assert_that(payment.HASH, equal_to(expected_hash))


def test_rest_digest():
    expected_digest = '10866e402f53c38105854b9aaebd2b6307b3c98aa21400c95d92711caf7209990948ff8c1a4d0fbd8e4c5c2344fc97' \
                      '003ba6e410c564788eece10199a345706e'
    sale_request = sale(
        orderId='R001',
        account=account(
            terminalId='T001',
            deviceId=''
        ),
        amount=amount(
            currency='USD',
            amount_member=1.34),
        hash=rhash()
    )
    sale_request.json()
    assert_that(sale_request.hash.digest, equal_to(expected_digest))

