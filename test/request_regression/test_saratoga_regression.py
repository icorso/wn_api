from faker import Factory
from hamcrest import assert_that, instance_of, equal_to

from constants import TransactionType, TerminalType, Currency
from data.rest_requests import rest_emv_tlv_sale, rest_sale, rest_taxes, rest_tip, rest_reversal
from data.xml_requests import payment_avs, payment, payment_applepay_visa, payment_chp, account_verification_request, \
    payment_securecard, securecard_registration, preauth, \
    stored_subscription, subscription, payment_subscription, unreferenced_refund
from model.boarding import levelDataEnum, apiAddressModeEnum
from model.gateway import PAYMENTRESPONSE, REFUNDRESPONSE, ACCOUNT_VERIFICATION_RESPONSE, \
    SECURECARDREGISTRATIONRESPONSE, PREAUTHRESPONSE, ADDSTOREDSUBSCRIPTIONRESPONSE, ADDSUBSCRIPTIONRESPONSE, \
    SUBSCRIPTIONPAYMENTRESPONSE, LEVEL_2_DATA, SHIPPING_ADDRESSType, LEVEL_3_DATA, SUMMARYType, LINE_ITEMSType, \
    LINE_ITEMType, CARDCURRENCYRATERESPONSE, FOREIGNCURRENCYINFORMATION, UNREFERENCEDREFUNDRESPONSE, CUSTOMFIELD
from model.rest import account, terminalType, customer, transactionResponse
from wnclient import WNClient

fake = Factory.create()
wn = WNClient().vagrant.go
# wn = WNClient().iron.go
TERM_ID = '21001'
TERM_MC_ID = '21002'
# TERM_ID = '203002'
TERM_ID_MULTICURRENCY = '21002'
TERM_APPLEPAY = '21003'
VISA = '4929003080058898'
VISA_SECURECARD = '4021610650777298'
MC_SECURECARD = '5230170097694626'
VISA_DECLINED = '4716564020255842'
MC = '5338738114454702'
AMEX = '378027104217770'
DISCOVER = '6011948752367734'
VISA_EDCC = '4485910301709438'  # GPB > USD
TRACKDATA = ';4024007118320745=201210114991888?'
TRACKDATA_AMEX = ';378027104217770=201210114991888?'


def test_saratoga_internet_visa_payment():
    p = payment()
    p.CARDNUMBER = VISA
    p.AMOUNT = 1.01
    p.DESCRIPTION = 'DESC 001'
    p.CARDHOLDERNAME = 'Erin Nelson'
    p.CARDEXPIRY = '0323'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_chp_visa_payment():
    p = payment_chp(amount=1.02)
    p.TRACKDATA = TRACKDATA
    p.DESCRIPTION = 'DESC 002'
    p.CARDHOLDERNAME = 'Jayde Buckridge'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_internet_mastercard_payment():
    p = payment()
    p.CARDNUMBER = MC
    p.CARDTYPE = 'MASTERCARD'
    p.AMOUNT = 1.03
    p.DESCRIPTION = 'DESC 003'
    p.CARDHOLDERNAME = 'Holly Hart'
    p.CARDEXPIRY = '0421'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_internet_visa_declined():
    p = payment()
    p.CARDNUMBER = VISA_DECLINED
    p.AMOUNT = 1.04
    p.DESCRIPTION = 'DESC 004'
    p.CARDHOLDERNAME = 'John Baxter'
    p.CARDEXPIRY = '1122'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))
    assert_that(response.RESPONSECODE, equal_to('D'))


def test_saratoga_avs_payment():
    p = payment_avs()
    p.CARDNUMBER = VISA
    p.AMOUNT = 1.05
    p.DESCRIPTION = 'DESC 005'
    p.CARDHOLDERNAME = 'Abigale Mills'
    p.CARDEXPIRY = '0920'
    p.EMAIL = 'Abigale66@gmail.com'
    p.ADDRESS1 = '07992 Rutherford Hill'
    p.ADDRESS2 = 'app 19'
    p.POSTCODE = '5229235'
    p.IPADDRESS = '119.17.49.92'
    p.CITY = 'Vena'
    p.REGION = 'Cassin'
    p.COUNTRY = 'US'
    p.BILLTOFIRSTNAME = 'Jesse'
    p.BILLTOLASTNAME = 'Bruen'
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))


def test_saratoga_visa_refund():
    p = payment()
    p.CARDNUMBER = VISA
    p.AMOUNT = 1.06
    p.DESCRIPTION = 'DESC 006'
    p.CARDHOLDERNAME = 'Bernhard Rogahn'
    p.CARDEXPIRY = '0121'
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    uniqueref = payment_response.UNIQUEREF
    amount = p.AMOUNT / 2
    refund_response = wn.xml(terminal_id=TERM_ID).refund(uniqueref, amount)
    assert_that(refund_response, instance_of(REFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_saratoga_unreferenced_visa_refund():
    p = unreferenced_refund(amount=1.07)
    p.CARDDETAILS.CARDNUMBER = VISA
    p.CARDDETAILS.CARDEXPIRY = '1219'

    refund_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(refund_response, instance_of(UNREFERENCEDREFUNDRESPONSE))
    assert_that(refund_response.RESPONSECODE, equal_to('A'))


def test_saratoga_applepay_payment():
    p = payment_applepay_visa()
    p.DESCRIPTION = 'DESC 008'
    p.CARDHOLDERNAME = 'Florence Collins'
    response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_account_verification():
    r = account_verification_request()
    r.CARDNUMBER = VISA
    r.CARDEXPIRY = '1224'
    r.ADDRESS1 = '07992 Rutherford Hill'
    r.POSTCODE = '5229235'
    response = wn.xml(TERM_ID).account_verification(request=r)
    assert_that(response, instance_of(ACCOUNT_VERIFICATION_RESPONSE))
    assert_that(response.STATUS, equal_to('VERIFIED'))


def test_saratoga_securecard_registration_and_payment():
    s = securecard_registration()
    s.CARDNUMBER = VISA_SECURECARD
    s.CARDEXPIRY = '1024'
    s.CARDTYPE = 'VISA'
    s.CARDHOLDERNAME = 'Michael Blake'
    s.CVV = '482'
    s.POSTCODE = '12676'
    s.EMAIL = 'garzarussell@yahoo.com'
    s.PHONE = '1294515098346'
    secure_card = wn.xml(TERM_ID).secure_card_registration(request=s)
    assert_that(secure_card, instance_of(SECURECARDREGISTRATIONRESPONSE))

    p = payment_securecard(cardreference=secure_card.CARDREFERENCE)
    p.AMOUNT = 1.09
    p.CVV = '999'
    p.ADDRESS1 = '3204 Davis Ports'
    p.ADDRESS2 = 'Apt. 92'
    p.POSTCODE = '08084'
    p.CITY = 'Atlanta'
    p.REGION = 'AT'
    p.DESCRIPTION = 'DESC 009'

    response = wn.xml(TERM_ID).payment(request=p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_visa_preauth():
    p = preauth()
    p.AMOUNT = 1.10
    p.CARDNUMBER = VISA
    p.CARDEXPIRY = '0825'
    p.DESCRIPTION = 'DESC 010'

    response = wn.xml(TERM_ID).preauth(request=p)
    assert_that(response, instance_of(PREAUTHRESPONSE))


def test_saratoga_emv_rest_payment():
    p = rest_emv_tlv_sale(amount=1.11)
    p.deviceType = 'WALKER'
    p.customer = customer(
        city='Mckeefurt',
        country='US',
        eMail='etaylor1185@gmail.com',
        ipAddress='192.31.212.139',
        mobileNumber='1185907071825',
        region='North Carolina',
    )
    p.account = account(
        operator='Frank Douglas',
        terminalType=terminalType.CHP
    )
    response = wn.rest(terminal_id=TERM_ID).sale(request=p)
    assert_that(response, instance_of(transactionResponse))


def test_saratoga_subscription_visa_payment():
    recurring_amount = 1.12

    ss = stored_subscription()
    ss.NAME = 'Balistreri'
    ss.DESCRIPTION = 'DESC 012'
    ss.RECURRINGAMOUNT = recurring_amount
    ss.INITIALAMOUNT = 2.01

    stored_subscription_response = wn.xml(TERM_ID).add_stored_subscription(request=ss)
    assert_that(stored_subscription_response, instance_of(ADDSTOREDSUBSCRIPTIONRESPONSE))

    sc = securecard_registration()
    sc.CARDNUMBER = VISA_SECURECARD
    sc.CARDEXPIRY = '0322'
    sc.CARDTYPE = 'VISA'
    sc.CARDHOLDERNAME = 'Boyd Hartmann'
    sc.CVV = '875'
    sc.POSTCODE = '36521'
    sc.EMAIL = 'Boyd12@yahoo.com'
    sc.PHONE = '1475957136'
    secure_card_response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(secure_card_response, instance_of(SECURECARDREGISTRATIONRESPONSE))

    s = subscription(stored_subscriptionref=stored_subscription_response.MERCHANTREF)
    s.SECURECARDMERCHANTREF = sc.MERCHANTREF
    subscription_response = wn.xml(TERM_ID).add_subscription(request=s)
    assert_that(subscription_response, instance_of(ADDSUBSCRIPTIONRESPONSE))

    sp = payment_subscription(subscription_response.MERCHANTREF)
    sp.AMOUNT = recurring_amount
    sp.DESCRIPTION = 'DESC 012'
    sp.EMAIL = 'jsanchez@yahoo.com'
    subscription_payment_response = wn.xml(TERM_ID).subscription_payment(request=sp)
    assert_that(subscription_payment_response, instance_of(SUBSCRIPTIONPAYMENTRESPONSE))


def test_saratoga_level_3_payment():
    wn_boarding = wn.boarding().with_terminal(TERM_ID)
    wn_boarding.update_terminal_level_data(level_data=levelDataEnum.LEVEL_III,
                                           api_address_mode=apiAddressModeEnum.EXACT)

    level_2 = LEVEL_2_DATA(
        CUSTOMER_REF_NUMBER='CRN_013',
        TAX_AMOUNT='2.13',
        SHIPPING_ADDRESS=SHIPPING_ADDRESSType(
            FULL_NAME='Valerie Ayers',
            ADDRESS1='60476 Derek Well Suite 417',
            ADDRESS2='APt. 251',
            CITY='Adamsport',
            REGION='Washingtom',
            POSTCODE='89894',
            COUNTRY='US'
        )
    )

    level_3 = LEVEL_3_DATA(
        SUMMARY=SUMMARYType(
            TOTAL_DISCOUNT_AMOUNT='9.95',
            TOTAL_FREIGHT_AMOUNT='9.43',
            TOTAL_DUTY_AMOUNT='8.12',
        ),
        LINE_ITEMS=LINE_ITEMSType(
            [LINE_ITEMType(
                COMMODITY_CODE='CC_4.12',
                PRODUCT_CODE='PC_4.75',
                DESCRIPTION='ITEM DESC 014',
                QUANTITY=4.12,
                UNIT_OF_MEASURE='UNIT_014',
                UNIT_PRICE=4.75,
                TOTAL_AMOUNT='19.57',
                DISCOUNT_RATE=0.32,
                TAX_RATE=9.24
            )]
        )
    )

    p = payment_avs()
    p.CARDNUMBER = VISA
    p.AMOUNT = 1.14
    p.CARDHOLDERNAME = 'Nathan Reed'
    p.CARDEXPIRY = '0920'
    p.ADDRESS1 = '07992 Rutherford Hill'
    p.POSTCODE = '5229235'

    p.LEVEL_2_DATA = level_2
    p.LEVEL_3_DATA = level_3
    response = wn.xml(TERM_ID).payment(p)
    assert_that(response, instance_of(PAYMENTRESPONSE))


def test_saratoga_tax_rest_payment():
    p = rest_sale(amount=1.15, cardtype='VISA', cvv='999')
    p.account.operator = 'Sarah Walker'
    p.customer.city = 'Atlanta'
    p.customer.country = 'US'
    p.customer.email = 'jduncan@yahoo.com'
    p.customer.ipAddress = '169.245.196.59'
    p.customer.mobileNumber = '7594934041745'
    p.customer.region = 'Hawaii'
    p.paymentMethod.keyedCard.cardHolderName = 'Ashley Johnson'
    p.paymentMethod.keyedCard.cardNumber = VISA
    p.paymentMethod.keyedCard.expiryDate = '1126'

    p.taxes = rest_taxes(tax_name='VAT', percentage=20, amount=0.19)
    response = wn.rest(terminal_id=TERM_ID).sale(request=p)
    assert_that(response, instance_of(transactionResponse))


def test_saratoga_tip_rest_payment():
    p = rest_sale(amount=1.16, cardtype='VISA', cvv='999')
    p.account.operator = 'Adam Foster'
    p.customer.city = 'West Jordan'
    p.customer.country = 'US'
    p.customer.email = 'adamfo91@yahoo.com'
    p.customer.ipAddress = '192.88.98.61'
    p.customer.mobileNumber = '1045790728465'
    p.customer.region = 'Mississippi'
    p.paymentMethod.keyedCard.cardHolderName = 'Peter Son'
    p.paymentMethod.keyedCard.cardNumber = VISA
    p.paymentMethod.keyedCard.expiryDate = '0921'

    p.tip = rest_tip(amount=0.16)
    response = wn.rest(terminal_id=TERM_ID).sale(request=p)
    assert_that(response, instance_of(transactionResponse))


def test_saratoga_edcc_payment():
    '''
    <PAYMENT>
  <ORDERID>ORID_017</ORDERID>
  <TERMINALID>21001</TERMINALID>
  <AMOUNT>1.17</AMOUNT>
  <DATETIME>03-09-2019:18:12:50:000</DATETIME>
  <CARDNUMBER>4485910301709438</CARDNUMBER>
  <CARDTYPE>visa</CARDTYPE>
  <CARDEXPIRY>0121</CARDEXPIRY>
  <CARDHOLDERNAME>Bernhard Rogahn</CARDHOLDERNAME>
  <HASH>c457b0974c65db8e16f4435d25774026607a9d1a26439d9998c4819c8f9f367b56f8dafa4780fe300c79d6be78695d9633e646a0f3776fdf9c7c3ac57116789e</HASH>
  <CURRENCY>USD</CURRENCY>
  <FOREIGNCURRENCYINFORMATION>
    <CARDCURRENCY>GBP</CARDCURRENCY>
    <CARDAMOUNT>0.8</CARDAMOUNT>
    <CONVERSIONRATE>0.684114</CONVERSIONRATE>
  </FOREIGNCURRENCYINFORMATION>
  <TERMINALTYPE>2</TERMINALTYPE>
  <TRANSACTIONTYPE>7</TRANSACTIONTYPE>
  <AUTOREADY>Y</AUTOREADY>
  <CVV>999</CVV>
  <DESCRIPTION>DESC 017</DESCRIPTION>
</PAYMENT>
    '''
    edcc_response = wn.xml(terminal_id=TERM_ID).get_card_currency_rate(VISA_EDCC[:6], 1.17)
    assert_that(edcc_response, instance_of(CARDCURRENCYRATERESPONSE))

    fa = FOREIGNCURRENCYINFORMATION(
        CARDCURRENCY=edcc_response.CARDCURRENCY,
        CARDAMOUNT=edcc_response.FOREIGNAMOUNT,
        CONVERSIONRATE=edcc_response.CONVERSIONRATE,
    )

    p = payment()
    p.CARDNUMBER = VISA_EDCC
    p.AMOUNT = 1.17
    p.ORDERID = 'ORID_017'
    p.DESCRIPTION = 'DESC 017'
    p.CARDHOLDERNAME = 'Bernhard Rogahn'
    p.CARDEXPIRY = '0121'
    p.FOREIGNCURRENCYINFORMATION = fa
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))


def test_saratoga_rest_reversal():
    p = payment()
    p.CARDNUMBER = VISA
    p.AMOUNT = 1.18
    p.DESCRIPTION = 'DESC 018'
    p.CARDHOLDERNAME = 'John Adamson'
    p.CARDEXPIRY = '1122'
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))

    uniqueref = payment_response.UNIQUEREF
    wn.rest(terminal_id=TERM_ID).reversal(rest_reversal(uniqueref))


def test_saratoga_custom_fields_payment():
    p = payment()
    p.AMOUNT = 1.19
    p.CARDNUMBER = VISA
    p.DESCRIPTION = 'DESC 019'
    p.CARDHOLDERNAME = 'Lincoln Runolfsson'
    p.CARDEXPIRY = '0828'
    p.CUSTOMFIELD = [
        CUSTOMFIELD(NAME='CustomString100', valueOf_='cf100 value'),
        CUSTOMFIELD(NAME='CustomNumeric', valueOf_='25')
    ]
    wn.xml(terminal_id=TERM_ID).payment(request=p)


def test_saratoga_multicurrency_terminal_amex_payment():
    p = payment().is_multicurrency(True)
    p.AMOUNT = 1.20
    p.CARDNUMBER = AMEX
    p.DESCRIPTION = 'DESC 020'
    p.CARDHOLDERNAME = 'Annabelle Barrows'
    p.CARDEXPIRY = '1221'
    wn.xml(terminal_id=TERM_MC_ID).payment(request=p)


def test_saratoga_moto_visa_payment():
    p = payment()
    p.TRANSACTIONTYPE = TransactionType.MOTO
    p.TERMINALTYPE = TerminalType.MOTO
    p.CARDNUMBER = VISA
    p.AMOUNT = 1.21
    p.DESCRIPTION = 'DESC 021'
    p.CARDHOLDERNAME = 'Catharine Adams'
    p.CARDEXPIRY = '1221'
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))


def test_saratoga_moto_discover_payment():
    p = payment()
    p.TRANSACTIONTYPE = TransactionType.MOTO
    p.TERMINALTYPE = TerminalType.MOTO
    p.CARDNUMBER = DISCOVER
    p.AMOUNT = 1.22
    p.DESCRIPTION = 'DESC 022'
    p.CARDHOLDERNAME = 'Catharine Adams'
    p.CARDEXPIRY = '1221'
    payment_response = wn.xml(terminal_id=TERM_ID).payment(request=p)
    assert_that(payment_response, instance_of(PAYMENTRESPONSE))


def test_saratoga_subscription_mastercard_payment():
    recurring_amount = 1.24

    ss = stored_subscription()
    ss.NAME = 'Ferry-Rosenbaum'
    ss.DESCRIPTION = 'DESC 024'
    ss.RECURRINGAMOUNT = recurring_amount
    ss.INITIALAMOUNT = 2.04

    stored_subscription_response = wn.xml(TERM_ID).add_stored_subscription(request=ss)
    assert_that(stored_subscription_response, instance_of(ADDSTOREDSUBSCRIPTIONRESPONSE))

    sc = securecard_registration()
    sc.CARDNUMBER = MC_SECURECARD
    sc.CARDEXPIRY = '0322'
    sc.CARDTYPE = 'MASTERCARD'
    sc.CARDHOLDERNAME = 'Vivienne Blanda'
    sc.CVV = '987'
    sc.POSTCODE = '348989'
    sc.EMAIL = 'Vivienne_Blanda4@hotmail.com'
    sc.PHONE = '3459239489'
    secure_card_response = wn.xml(TERM_ID).secure_card_registration(request=sc)
    assert_that(secure_card_response, instance_of(SECURECARDREGISTRATIONRESPONSE))

    s = subscription(stored_subscriptionref=stored_subscription_response.MERCHANTREF)
    s.SECURECARDMERCHANTREF = sc.MERCHANTREF
    subscription_response = wn.xml(TERM_ID).add_subscription(request=s)
    assert_that(subscription_response, instance_of(ADDSUBSCRIPTIONRESPONSE))

    sp = payment_subscription(subscription_response.MERCHANTREF)
    sp.AMOUNT = recurring_amount
    sp.DESCRIPTION = 'DESC 025'
    sp.EMAIL = 'Naomie61@hotmail.com'
    subscription_payment_response = wn.xml(TERM_ID).subscription_payment(request=sp, currency=Currency.USD)
    assert_that(subscription_payment_response, instance_of(SUBSCRIPTIONPAYMENTRESPONSE))


def test_saratoga_securecard_preauth():
    s = securecard_registration()
    s.CARDNUMBER = VISA_SECURECARD
    s.CARDEXPIRY = '0120'
    s.CARDTYPE = 'VISA'
    s.CARDHOLDERNAME = 'Mike Lake'
    s.CVV = '392'
    s.POSTCODE = '25487'
    s.EMAIL = 'mkidbla@glool.com'
    s.PHONE = '823728374'
    secure_card = wn.xml(TERM_ID).secure_card_registration(request=s)
    assert_that(secure_card, instance_of(SECURECARDREGISTRATIONRESPONSE))

    p = preauth()
    p.CARDTYPE = 'SECURECARD'
    p.AMOUNT = 1.26
    p.CARDNUMBER = secure_card.CARDREFERENCE
    p.DESCRIPTION = 'DESC 026'

    response = wn.xml(TERM_ID).preauth(request=p)
    assert_that(response, instance_of(PREAUTHRESPONSE))
