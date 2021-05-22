from faker import Factory

from constants import Acquirer
from model.boarding2 import Terminal, TsysSaratogaTerminal, UnassignedBankSettings
fake = Factory.create()


def boarding2_supported_cards():
    return [
        "AMEX",
        "SANTANDER",
        "ELECTRON",
        "SHELL",
        "LASER",
        "DELTA",
        "DISCOVER",
        "JCB",
        "VISA",
        "GIFTCARD",
        "DINERS",
        "MAESTRO",
        "VISA DEBIT",
        "DEBIT MASTERCARD",
        "UKASH NEO",
        "MASTERCARD",
        "SOLO",
        "SWITCH"
      ]


def boarding2_terminal_base():
    return Terminal(
      secret='someSecretPhrase',
      supported_cards=boarding2_supported_cards()
    )


def boarding2_bank_settings():
    return UnassignedBankSettings(
        base_currency='USD',
        allow_moto=True,
        allow_internet=True,
        display_name=fake.random_number()
    )


def boarding2_tsys_saratoga_terminal():
    terminal = TsysSaratogaTerminal()
    terminal.__dict__.update(boarding2_terminal_base().__dict__)
    terminal.payment_processor = Acquirer.TSYS_SARATOGA
    terminal.bank_settings = boarding2_bank_settings()
    return terminal


tsys = boarding2_tsys_saratoga_terminal()
print(tsys.json())
#
# {
#   "paymentProcessor": "TSYS Saratoga",
#   "terminalNumber": "21001",
#   "secret": "someSecretPhrase",
#   "unionPayProcessing": {
#     "enable": true,
#     "merchantId": "198012400000002",
#     "merchantName": "Pivotal",
#     "merchantAbbreviation": "Pivotal",
#     "merchantCategoryCode": "8394",
#     "draft256Billing": {
#       "bankMerchantId": "86",
#       "terminalIdNumber": "82",
#       "acqInstitutionIdCode": "9982",
#       "storeNumber": "7786",
#       "cardAcceptorName": "Lisa Martinez",
#       "localPhoneNumber": "60829348",
#       "state": "US-AL",
#       "city": "New Kathy",
#       "postalCode": "952395",
#       "streetAddress": "30920"
#     }
#   },
#   "volumeLimits": {
#     "enableTerminalLevelLimits": false,
#     "enableCardLevelLimits": false
#   },
#   "supportedCards": [
#     "AMEX",
#     "SANTANDER",
#     "ELECTRON",
#     "SHELL",
#     "LASER",
#     "DELTA",
#     "DISCOVER",
#     "JCB",
#     "VISA",
#     "GIFTCARD",
#     "DINERS",
#     "MAESTRO",
#     "VISA DEBIT",
#     "DEBIT MASTERCARD",
#     "UKASH NEO",
#     "MASTERCARD",
#     "SOLO",
#     "SWITCH"
#   ],
#   "bankSettings": {
#     "groupBankName": "USA",
#     "allowMulticurrency": false,
#     "allowEmcp": false,
#     "allowEdcc": false,
#     "baseCurrency": "USD",
#     "allowMoto": true,
#     "allowInternet": true,
#     "allowChp": true,
#     "defaultTerminalType": "MOTO",
#     "allowRecurring": true,
#     "allowPreAuth": true,
#     "bankMerchantId": "887000001361",
#     "bankTerminalId": "87490785",
#     "agentBankNumber": "7450",
#     "agentChainNumber": "292598",
#     "storeNumber": "4062",
#     "terminalIdNumber": "84459177",
#     "acqInstitutionIdCode": "565",
#     "markUpPercentage": 3.5,
#     "customerServiceEmail": "ortegajohn@hotmail.com",
#     "enableAutomaticSettle": true,
#     "batchTime": "14:15",
#     "displayName": "TSYS Sara_124",
#     "allowEditDisplayName": true,
#     "forceUniqueOrderId": true
#   },
#   "terminalLocation": {
#     "cardAcceptorName": "Alfred Russell",
#     "country": "US",
#     "state": "US-WA",
#     "city": "Perezfort",
#     "postalCode": "51514",
#     "timeZone": "Europe/London",
#     "useTerminalAddress": false,
#     "contactPhone": "5732780178"
#   },
#   "terminalFeatures": {
#     "allowPartialCaptures": true,
#     "allowAcquiring": false,
#     "allowOfflineSales": true,
#     "allowDashboard": false,
#     "allowBulkPayments": true,
#     "allowScheduleReports": false,
#     "allowVirtualTerminalAutoOrderId": true,
#     "enableDecryptx": false,
#     "enableGooglePay": false,
#     "enableApplePay": false,
#     "appleStoreName": "",
#     "payLink": {
#       "enable": true
#     },
#     "shopify": {
#       "enable": false
#     },
#     "surcharge": {
#       "enable": true,
#       "percent": 4.0
#     },
#     "secureCredentials": {
#       "enable": true,
#       "enableSecureCardValidation": true,
#       "forceSecureCardValidation": false,
#       "allowHostedPageStorage": true,
#       "allowHostedPageAutomaticStorage": false,
#       "hostedPageEmailFieldSetup": "OPTIONAL",
#       "secureCredentialsReceiptUrl": "",
#       "allowSubscriptions": true,
#       "subscriptionMaxMissedPeriods": 1,
#       "subscriptionMaxAuthorizationAttempts": 16,
#       "subscriptionMaxDaysWaitingForPayment": 10,
#       "subscriptionNotificationRepeatIntervalInDays": 12,
#       "subscriptionPaymentNotificationIntervalInDays": 9,
#       "subscriptionMissedPeriodsThresholdForNotification": 12,
#       "subscriptionReceiptUrl": "",
#       "subscriptionNotificationUrl": "http://simulator.wntps.com:8282/vagrant/?timeout1=10",
#       "accountUpdater": {
#         "enableVau": false,
#         "enableAbu": false,
#         "enableBackgroundNotifications": true,
#         "enableBackgroundNotificationsForFailures": false,
#         "backgroundNotificationsUrl": "http://simulator.wntps.com:8282/vagrant/?timeout1=10"
#       }
#     },
#     "amexOptBlue": {
#       "enable": false
#     },
#     "enhancedData": {
#       "enable": false,
#       "enableTemplateAutofill": false
#     },
#     "paymentFacilitator": {
#       "enable": false
#     },
#     "dynamicDescriptor": {
#       "enable": false
#     }
#   },
#   "fraudDetection": {
#     "allowCardholderSignatureBypass": false,
#     "allowCvvComplianceRuleBypass": false,
#     "allowUnreferencedRefunds": true,
#     "unreferencedRefundAmountLimit": 0,
#     "refundPercentageLimit": 100.0,
#     "addressVerification": {
#       "enable": true,
#       "action": "EDITABLE",
#       "compulsory": false,
#       "autoDeclineOnFailure": false
#     },
#     "cvvVerification": {
#       "enable": true,
#       "autoDeclineOnFailure": true,
#       "declineCodes": [
#         "N"
#       ]
#     },
#     "threeDSecure": {
#       "enable": true,
#       "merchantId": "1",
#       "password": "password123",
#       "supportedCards": [
#         "MASTERCARD"
#       ]
#     },
#     "maxMind": {
#       "enable": false,
#       "rejectOnError": false,
#       "riskScoreThreshold": 50.0
#     },
#     "sentinelDefend": {
#       "enable": false,
#       "rejectOnError": false,
#       "riskScoreThreshold": 0
#     }
#   },
#   "integrationSettings": {
#     "useUniqueRef": true,
#     "enableAutoReady": true,
#     "autoReadyAmountLimit": 0,
#     "hostedPageVersion": "VERSION_2",
#     "enableBackgroundValidation": false,
#     "backgroundValidationUrl": "http://simulator.wntps.com:8282/vagrant/?timeout1=10",
#     "receiptPageUrl": "http://simulator.wntps.com:8181/receipt",
#     "mpiReceiptUrl": "",
#     "enableAdditionalFieldXmlResponseTag": true,
#     "enableOriginalResponseXmlResponseTag": true,
#     "enableBankResponseCodeXmlResponseTag": true,
#     "enableMaskedCardXmlResponseTag": true,
#     "enableSupportsApplePayXmlResponseTag": true,
#     "enableSupportsGooglePayXmlResponseTag": true,
#     "enableEnable3dsXmlResponseTag": true,
#     "enableSupportedCardsXmlResponseTag": true
#   },
#   "receiptNotifications": {
#     "showEmailFieldOnVirtualTerminal": false,
#     "merchantSupportEmail": "tsyss_5920@yahoo.com",
#     "notificationEmails": [
#       "tsyss_5920@yahoo.com"
#     ],
#     "disableReceipts": false,
#     "enableCardholderEmailReceipt": false,
#     "enableCardholderSmsReceipt": false
#   },
#   "achProcessing": {
#     "enable": true,
#     "locationId": "472938472",
#     "merchantId": "239489233",
#     "groupBankName": "Central Bank of Texas"
#   }
# }