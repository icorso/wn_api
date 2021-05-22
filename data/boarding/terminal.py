import json
import os

from faker import Factory

from constants import RoutingNumber, Country, TimeZone, Acquirer, CARDTYPES, Currency, TerminalType
from model.boarding import terminal as terminal_, terminalBankSettings, additionalTerminalSettings, terminalFeatures, \
    cardsType, terminalTypeDefaultEnum, terminalSecurityFraud, cvvResponseEnum, avsActionEnum, terminalIntegration, \
    terminalAchSettings, terminalUnionPayProcessing, terminalReceiptsNotification, reimbursementAttributeEnum, \
    industryCodeEnum, languageIndicatorEnum, terminalDraft256Billing
from utils import today

fake = Factory.create()
root_dir = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root_dir, "../../credentials.json"), "r") as json_file:
    data = json.load(json_file)


def integration():
    return terminalIntegration(
        useUniqueRef=True,
        autoReady=True,
        showMaskedCardDetailsInXmlResponse=True,
        enableAdditionalFieldsInXml=True,
        enableOriginalResponseInXml=True,
        addBankResponseCodeToXML=True
    )


def bank_settings(display_name=fake.domain_word()[:12]):
    return terminalBankSettings(
        currency='USD',
        allowMulticurrency=False,
        allowEmcp=False,
        allowMoto=True,
        allowInternet=True,
        allowRecurring=True,
        allowPreAuth=True,
        allowCHP=True,
        bankTerminalId=str(fake.random_number(8)),
        bankMerchantId=str(fake.random_number(8)),
        enableAutomaticSettle=True,
        batchTime=today(format='%H:%M'),
        displayName=display_name,
        allowEditDisplayName=True,
        forceUniqueOrder=True
    )


def additional_terminal_settings():
    return additionalTerminalSettings(
        agentBankNumber=str(fake.random_number(4)),
        terminalIdNumber=str(fake.random_number(8, fix_len=True)),
        agentChainNumber=str(fake.random_number(6)),
        storeNumber=str(fake.random_number(4)),
        acqInstitutionIdCode=str(fake.random_number(3, fix_len=True)),
        merchantName=fake.name(),
        merchantLocalPhoneNum=str(fake.random_number(10)),
        postalCode=fake.postcode(),
        merchantCity=fake.city()[:13],
        usState=RoutingNumber.rand_us_state_name()
    )


def features():
    return terminalFeatures(
        allowSecurecards=True,
        validateScSecurity=False,
        forceScValidation=False,
        allowHppScStorage=True,
        storeHppScAutomatically=False,
        allowSubscriptions=True,
        subscriptionMaxWaitForPaymentDays=fake.random_int(1, 20),
        subscriptionMaxMissedPeriods=fake.random_int(1, 20),
        subscriptionPaymentNotificationDays=fake.random_int(1, 20),
        subscriptionMissedPeriodsNotification=fake.random_int(1, 20),
        subscriptionRepeatNotificationDays=fake.random_int(1, 20),
        subscriptionAuthMaxAttempts=fake.random_int(1, 20),
        allowDashboard=False,
        allowBulkpayment=True,
        allowVtAutoOrderId=True,
        enableDecryptx=False,
        allowPartialCaptures=True,
        enableAccountUpdaterBackgroundNotifications=False
    )


def security_fraud():
    return terminalSecurityFraud(
        enableAvs=True,
        avsSentAction=avsActionEnum.EDITABLE,
        allowShowCvv=True,
        allowAutoDeclineCvvFailures=True,
        cvvDeclineCodes=[cvvResponseEnum.NOT_MATCH],
        refundAmountLimit=100
    )


def terminal_ach_settings(enabled=False):
    return terminalAchSettings(
        allowAchJhTransactions=enabled,
        achJhMerchantId='322546',
        achJhLocationId='1720378'
    )


def terminal_unionpay_processing(enabled=False):
    return terminalUnionPayProcessing(
        allowUnionPayProcessing=enabled,
        cupMerchantId='322546',
        cupMerchantCategoryCode='1720378',
        cupMerchantName='',
        cupMerchantAbbreviation=''
    )


def terminal_draft_256_billing():
    return terminalDraft256Billing(
        cupBankMerchantId=str(fake.random_number(24, True)),
        cupTerminalIdNumber=str(fake.random_number(8, fix_len=True)),
        cupAcqInstitutionIdCode=str(fake.random_number(6, True)),
        cupStoreNumber=str(fake.random_number(4, True)),
        cupMerchantName=fake.name(),
        cupMerchantLocalPhoneNum=str(fake.random_number(11, True)),
        cupPostalCode=str(fake.random_number(6, True)),
        cupMerchantCity=fake.city(),
        merchantStreetAddress=fake.street_name(),  # street_address() will produce RollbackException
        cupMerchantState=RoutingNumber.rand_us_state_name()
    )


def terminal_receipts_notification(notification_email=fake.free_email(), merchant_email=fake.free_email()):
    return terminalReceiptsNotification(
        notificationEmail=notification_email,
        merchantSupportEmail=merchant_email
    )


def terminal(acquirer=Acquirer.ELAVON, merchant_id=None):
    display_name = '{}_{}'.format(acquirer[:6], fake.random_number(4, True))
    email = f"{display_name.lower()}@{fake.free_email_domain()}"
    return terminal_(
        acquirer=acquirer,
        country=Country.Ireland.code,
        timeZone=TimeZone.LONDON.timezone,
        merchantId=merchant_id,
        secret='someSecretPhrase',
        bankSettings=bank_settings(display_name=display_name),
        additionalSettings=additional_terminal_settings(),
        features=features(),
        securityFraud=security_fraud(),
        integration=integration(),
        receiptsNotification=terminal_receipts_notification(
            notification_email=email.replace(' ', ''),
            merchant_email=email.replace(display_name, display_name + '_merchant').replace(' ', '')),
        cards=cardsType(CARDTYPES),
        achSettings=terminal_ach_settings()
    )

# terminals by acquirer


def cashflows_terminal(merchant_id=None):
    cashflows = data['test_hosts'].get('CashFlows')
    t = terminal('CashFlows', merchant_id)
    t.securityFraud.authId = cashflows.get("securityFraud.authId")
    t.securityFraud.authPassword =  cashflows.get('securityFraud.authPassword')
    t.bankSettings.allowPreAuth = False
    t.bankSettings.currency = Currency.EUR.name
    t.bankSettings.allowRecurring = False
    return t


def credorax_terminal(merchant_id=None):
    credorax = data['test_hosts'].get('Credorax')
    t = terminal('Credorax', merchant_id)
    t.bankSettings.allowPreAuth = False
    t.bankSettings.bankMerchantId = credorax.get('bankSettings.bankMerchantId')
    t.bankSettings.bankPassword = credorax.get('bankSettings.bankPassword')
    t.bankSettings.terminalTypeDefault = terminalTypeDefaultEnum.MOTO
    return t


def aib_terminal(merchant_id=None):
    t = terminal('AIB Merchant Services', merchant_id)
    t.bankSettings.allowPreAuth = False
    t.bankSettings.currency = Currency.USD.name
    t.bankSettings.allowRecurring = False
    return t


def allpago_terminal(merchant_id=None):
    t = terminal('AllPago', merchant_id)
    t.country = Country.Mexico.code
    t.bankSettings.allowPreAuth = False
    t.bankSettings.currency = Currency.MXN.name
    t.bankSettings.allowRecurring = False
    return t


def worldpay_terminal(merchant_id=None):
    t = terminal('WorldPay', merchant_id)
    t.bankSettings.allowPreAuth = False
    t.bankSettings.currency = Currency.USD.name
    t.bankSettings.allowRecurring = False
    t.bankSettings.bankCompanyId = '487283324'
    return t


def integrapay_terminal(merchant_id=None):
    t = terminal('IntegraPay', merchant_id)
    cards = CARDTYPES
    cards.append('DIRECTDEBIT')
    t.cards = cardsType(CARDTYPES)
    t.country = Country.Australia.code
    t.bankSettings.bankMerchantId = '1848'
    t.bankSettings.bankPassword = '5t=S$6Pes%9'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    t.achSettings = terminalAchSettings(
        allowAchJhTransactions=False,
        allowAchIpTransactions=True)
    return t


def ctpayments_terminal(merchant_id=None):
    t = terminal('CT Payments', merchant_id)
    t.bankSettings.bankMerchantId = '23897412'
    t.bankSettings.bankCompanyId = '92384'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.terminalTypeDefault = terminalTypeDefaultEnum.MOTO
    return t


def barclaycard_terminal(merchant_id=None):
    t = terminal('Barclaycard', merchant_id)
    t.bankSettings.bankMerchantId = '8768767867'
    t.bankSettings.bankTerminalId = '8764'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t


def tsys_saratoga_terminal(merchant_id=None):
    t = terminal('TSYS Saratoga', merchant_id)
    t.groupBank = 'USA'
    t.bankSettings.bankMerchantId = '887000001361'
    t.bankSettings.terminalTypeDefault = terminalTypeDefaultEnum.MOTO
    t.bankSettings.customerServiceEmail = fake.free_email()
    t.payFacSubMerchantIdentifier = str(fake.random_number(4, True))
    t.payFacSubMerchantName = fake.name()
    t.additionalSettings = additional_terminal_settings()
    t.features.isPayFacAllowed = True
    t.allowIntegraPayAch = True
    return t


def fiserv_terminal(merchant_id):
    t = terminal('FiServ', merchant_id)
    t.country = Country.USA.code
    t.bankSettings.fcsId = '0000167'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    t.bankSettings.allowMoto = False
    t.bankSettings.allowInternet = False
    t.bankSettings.bankMerchantId = '5700308'
    t.bankSettings.bankTerminalId = '2501'
    t.bankSettings.terminalTypeDefault = terminalTypeDefaultEnum.MOTO
    t.bankSettings.customerServiceEmail = fake.free_email()
    t.additionalSettings = additional_terminal_settings()
    t.cards = cardsType(['CBIC'])
    return t


def tsys_sierra_terminal(merchant_id):
    ats = additional_terminal_settings()
    ats.agentBankNumber = '000000'
    ats.acquirerBin = str(fake.random_number(6))
    ats.terminalIdNumber = '00010002'
    ats.agentChainNumber = '000001'
    ats.storeNumber = '0001'
    ats.abaNumber = '0002'
    ats.settlementAgentNo = '0003'
    ats.industryCode = industryCodeEnum.FOOD
    ats.languageIndicator = languageIndicatorEnum.ENGLISH
    ats.authenticationCode = '0001'
    ats.dstObserved = True
    ats.timeZoneOffset = -11
    ats.allowLevel2Data = True
    ats.sharingGroup = 'G8WKV'
    ats.allowLevel2 = True
    ats.reimbursementAttribute = reimbursementAttributeEnum.ATTRIBUTE_W
    ats.cardholderSvcPhoneNumber = str(fake.random_number(6))
    ats.cityCode = '22332'

    t = terminal('TSYS', merchant_id)
    t.country = Country.USA.code
    t.bankSettings.fcsId = '0000167'
    t.bankSettings.bankMerchantId = '88500000010'
    t.bankSettings.bankTerminalId = '0001'
    t.bankSettings.terminalTypeDefault = terminalTypeDefaultEnum.MOTO
    t.bankSettings.customerServiceEmail = fake.free_email()
    t.additionalSettings = ats
    t.cards = cardsType(CARDTYPES)
    return t


def nmi_terminal(merchant_id=None):
    t = terminal('NMI', merchant_id)
    t.bankSettings.bankMerchantId = 'demo'
    t.bankSettings.bankPassword = 'password'
    t.bankSettings.terminalTypeDefault = 'MOTO'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = True
    return t


def elavon_terminal(merchant_id=None):
    t = terminal('Elavon', merchant_id)
    t.bankSettings.terminalTypeDefault = 'MOTO'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t


def elavon_pos_terminal(merchant_id=None):
    t = terminal('Elavon POS', merchant_id)
    t.bankSettings.terminalTypeDefault = 'MOTO'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t


def elavon_converge_terminal(merchant_id=None):
    t = terminal('Elavon Converge', merchant_id)
    t.bankSettings.terminalTypeDefault = 'MOTO'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    t.bankSettings.bankMerchantId = '009005'
    t.bankSettings.bankCompanyId = 'devportal'
    t.bankSettings.bankPassword = 'BDDZY5KOUDCNPV4L3821K7PETO4Z7TPYOJB06TYBI1CW771IDHXBVBP51HZ6ZANJ'

    return t


def tango_terminal(merchant_id=None):
    # boarding is not working for Tango
    t = terminal('Tango', merchant_id)
    t.groupBank = 'Canada'
    t.country = 'CAN'
    t.additionalSettings = additional_terminal_settings()
    t.additionalSettings.canadianRegion = 'ALBERTA'  # AB ?
    t.additionalSettings.usState = None
    t.bankSettings.terminalTypeDefault = 'MOTO'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.currency = 'CAD'
    t.bankSettings.bankTerminalId = '7800003833'
    t.bankSettings.bankMerchantId = '10000089'
    t.bankSettings.bankCompanyId = '0.00'

    return t


def ncb_terminal(merchant_id=None):
    t = terminal('NCB', merchant_id)
    t.country = Country.Ireland.code
    t.timeZone = TimeZone.LONDON.timezone
    t.cards = cardsType(['VISA', 'MASTERCARD', 'JETS', 'NCB', 'NCB DEBIT'])
    t.currency = 'JMD'
    t.bankSettings.terminalTypeDefault = terminalTypeDefaultEnum.CHP
    t.bankSettings.bankMerchantId = '601100126194455'
    t.bankSettings.bankTerminalId = 'S0004057'
    t.bankSettings.tpdu = '6000040000'
    t.bankSettings.nii = '004'
    t.bankSettings.allowRecurring = False
    t.bankSettings.allowPreAuth = False
    return t


# Exigo acquirers
#
# Braintree
#
def braintree_terminal(merchant_id=None):
    t = terminal('Braintree', merchant_id)
    t.bankSettings.bankMerchantId = '12345'
    t.bankSettings.bankTerminalId = 'mkbmgpwdghnz4kp4'                 # public key
    t.bankSettings.bankCompanyId = 'mgx649jf74rm3y58'                  # GatewayId
    t.bankSettings.bankPassword = '891283f296298a3795ebb75069ee185c'   # PrivateKey
    t.bankSettings.allowMulticurrency = False
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t


def cybersourcesoap_terminal(merchant_id=None):
    t = terminal('CyberSourceSoap', merchant_id)
    t.country = Country.Ireland.code
    t.timeZone = TimeZone.LONDON.timezone
    t.bankSettings.bankMerchantId = 'neriumcysourcepayments'
    t.bankSettings.bankPassword = 'Ef4frYXJ97kVv59xsljHGQiEaS4Vmjp9gNi65dcjLUOtWEalXizzmVkAV1iKGliqVzfQW1AykuIYzZdV/JpwbWhdvNgFdj1q1AoD4vFHR8uh/Zpu/EtrgQk0IozHlJv77UfwcuSSssaZtd/utXLkEfYidfz2TdxDIkjjekXMiHSqbZw59L9GuEIdVpG+dzVUuXfphy+yyAx4p+0g440n5HKE48yE4Bx5G7RCKbOzVktD6wjJtjuAxUqiVZpWA1Olcj+YZdIq4+9YhJWAuz08yWIy5Uiq4/ZZzmfx7ldEOoHzXhrWumrE2vLQnNj0a809an2FK43y9Rs1boH1XetSUQ=='
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = True
    return t


def fdrc_terminal(merchant_id=None):
    t = terminal('FDRC PTCP', merchant_id)
    t.bankSettings.allowPreAuth = False
    t.bankSettings.bankMerchantId = 'RCTST0000008076'
    t.bankSettings.bankTerminalId = '00000001'
    t.bankSettings.frontEndGroupId = '10001'
    t.bankSettings.customerServiceUrl = 'http://local.host'
    t.bankSettings.customerServicePhone = str(fake.random_number(8, True))
    t.bankSettings.terminalTypeDefault = 'MOTO'
    t.securityFraud.allowUnreferencedRefundsAfterRefundDecline = True
    t.securityFraud.allowUnreferencedRefunds = True
    return t


def flapws_terminal(merchant_id=None):
    t = terminal('FlapWS', merchant_id)
    t.country = Country.Ireland.code
    t.bankSettings.bankMerchantId = '1'  # Entity Id
    t.bankSettings.bankTerminalId = 'fjkasdhfk'  # Admin Id
    t.bankSettings.bankPassword = '239847298742938'  # Encryption Key
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t


def maxconnect_terminal(merchant_id=None):
    t = terminal('Maxconnect', merchant_id)
    t.bankSettings.currency = 'JPY'
    t.bankSettings.bankMerchantId = '32302604'  # Entity Id
    t.bankSettings.bankPassword = 'TjHEaJr4'    # Encryption Key
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t


def global_payroll_terminal(merchant_id=None):
    t = terminal('Global Payroll Gateway', merchant_id)
    t.bankSettings.allowMulticurrency = True
    t.bankSettings.bankMerchantId = '3demo'  # Bank API Username
    t.bankSettings.bankTerminalId = '1009'  # Bank Client ID
    t.bankSettings.bankPassword = 'password'    # Bank API Password
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t


def propay_terminal(merchant_id=None):
    t = terminal('ProPay', merchant_id)
    t.bankSettings.bankMerchantId = str(fake.random_number())
    t.bankSettings.bankPassword = fake.ipv6()
    t.bankSettings.allowPreAuth = False
    return t


def first_citizens_terminal(merchant_id=None):
    t = terminal('First Citizens', merchant_id)
    t.bankSettings.bankMerchantId = str(fake.random_number())
    t.bankSettings.bankPassword = fake.ipv6()
    t.bankSettings.allowPreAuth = False
    t.bankSettings.terminalTypeDefault = 'MOTO'
    t.bankSettings.allowRecurring = False
    t.additionalSettings.postalCode = fake.postcode()
    return t


def authnet_terminal(merchant_id=None):
    t = terminal('Authorize Net', merchant_id)
    t.bankSettings.bankMerchantId = str(fake.random_number(8))
    t.bankSettings.bankPassword = str(fake.random_number(16))
    t.bankSettings.allowPreAuth = False
    return t


def netaxcept_terminal(merchant_id=None):
    t = terminal('NETAXCEPT', merchant_id)
    t.bankSettings.bankMerchantId = '12000480'
    t.bankSettings.bankPassword = '8Ez!Jf+9'
    t.bankSettings.terminalTypeDefault = 'MOTO'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t


def paysafe_terminal(merchant_id=None):
    t = terminal('PaySafe', merchant_id)
    t.bankSettings.currency = 'USD'
    t.bankSettings.bankMerchantId = '10012'
    t.bankSettings.bankPassword = 'c22a63ee-2e7a-4ace-96ac-0958dc8d953f'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t


def payulatam_terminal(merchant_id=None, country: Country=Country.Panama):
    environment = {Country.Argentina: '512322',
                   Country.Brazil: '512327',
                   Country.Colombia: '512321',
                   Country.Mexico: '512324',
                   Country.Panama: '512326',
                   Country.Peru: '512323'}

    t = terminal('PayULatam', merchant_id)
    t.country = country.code
    t.bankSettings.currency = 'USD'
    t.bankSettings.bankMerchantId = '508029'
    t.bankSettings.bankTerminalId = 'pRRXKOl8ikMmt9u'  # api login
    t.bankSettings.bankCompanyId = environment.get(country)  # bank account id
    t.bankSettings.bankPassword = '4Vj8eK4rloUd272L48hsrarnUA'  # bank merchant key
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t


def moneris_terminal(merchant_id=None):
    t = terminal('Moneris', merchant_id)
    t.bankSettings.currency = 'USD'
    t.bankSettings.bankMerchantId = 'store5'
    t.bankSettings.bankPassword = 'yesguy'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t


def payvision_terminal(merchant_id=None):
    t = terminal('Payvision', merchant_id)
    t.bankSettings.currency = 'USD'
    t.bankSettings.bankMerchantId = '1003215'
    t.bankSettings.bankPassword = '33434834-6F51-4D47-9159-8010257F5BAB'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t


def securepay_terminal(merchant_id=None):
    t = terminal('SecurePay', merchant_id)
    t.bankSettings.currency = 'USD'
    t.bankSettings.bankMerchantId = 'ABC0001'
    t.bankSettings.bankPassword = 'abc123'
    t.bankSettings.allowPreAuth = False
    t.bankSettings.allowRecurring = False
    return t

# end of Exigo terminals
