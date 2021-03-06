import random
from datetime import datetime
from enum import Enum

CARDTYPES = ['VISA', 'MASTERCARD', 'LASER', 'SWITCH', 'SOLO', 'AMEX', 'DINERS', 'MAESTRO', 'DELTA', 'ELECTRON', 'JCB',
             'SECURECARD', 'UKASH NEO', 'DEBIT MASTERCARD', 'DISCOVER', 'VISA DEBIT', 'SANTANDER', 'GIFTCARD', 'SHELL',
             'UNIONPAY', 'APPLEPAY', 'CBIC', 'GOOGLEPAY', 'LINX', 'ACH JH', 'NCB DEBIT', 'NCB KEYCARD', 'JETS DEBIT',
             'ACH INTEGRAPAY', 'INTERAC']

COMMON_CARDTYPES = ['SWITCH', 'SOLO', 'AMEX', 'DELTA', 'JCB',
             'SECURECARD', 'UKASH NEO', 'DISCOVER', 'VISA DEBIT', 'SANTANDER', 'GIFTCARD', 'SHELL',
             'UNIONPAY', 'APPLEPAY', 'CBIC', 'GOOGLEPAY', 'LINX', 'ACH JH', 'NCB DEBIT', 'NCB KEYCARD', 'JETS DEBIT',
             'ACH INTEGRAPAY', 'INTERAC']


class CardType(object):
    def __init__(self, name=None, display_name=None, group=None):
        self.name = name
        self.display_name = display_name
        self.group = group


class BaseCardType(object):
    @classmethod
    def filtered_card_type(cls):
        return list(filter(lambda attribute: getattr(cls, attribute).__class__.__name__ == 'CardType', dir(cls)))

    @classmethod
    def get_all_card_types(cls, group=None):
        card_types = list(map(lambda card_type: getattr(cls, card_type), cls.filtered_card_type()))
        if group:
            return list(filter(lambda g: g.group == group, card_types))
        else:
            return card_types

    @classmethod
    def get_names(cls, group=None):
        return list(map(lambda card_type: card_type.name, cls.get_all_card_types(group=group)))

    @classmethod
    def get_display_names(cls, group=None):
        return list(map(lambda card_type: card_type.display_name, cls.get_all_card_types(group=group)))


class CommonCardType(BaseCardType):
    VISA = CardType('VISA', 'Visa Credit', 'v')
    DELTA = CardType('DELTA', 'Delta', 'v')
    VISA_ELECTRON = CardType('ELECTRON', 'Visa Electron')
    VISA_DEBIT = CardType('VISA DEBIT', 'Visa Debit')

    MASTERCARD = CardType('MASTERCARD', 'MasterCard', 'm')
    MASTERCARD_DEBIT = CardType('DEBIT MASTERCARD', 'Debit MasterCard', 'm')
    MAESTRO = CardType('MAESTRO', 'Maestro', 'm')
    LASER = CardType('LASER', 'Laser', 'm')

    DINERS = CardType('DINERS', 'Diners', 'd')
    DISCOVER = CardType('DISCOVER', 'Discover', 'd')

    AMEX = CardType('AMEX', 'American Express', 'a')


class NCBCardType(CommonCardType):
    JETS_DEBIT = CardType('JETS DEBIT', 'JETS Debit Card', 'n')
    NCB_DEBIT = CardType('NCB DEBIT', 'NCB Debit Card', 'n')
    NCB_KEYCARD = CardType('NCB DEBIT', 'NCB Debit Card', 'n')


class Acquirer(object):
    UNASSIGNED = 'Unassigned'
    ELAVON = 'Elavon'
    AIB = 'AIB Merchant'
    BARCLAYCARD = 'Barclaycard'
    WORLDPAY = 'WorldPay'
    VACP_G2G = 'VACP G2G'  # + AnywhereCommerce
    CASHFLOWS = 'CashFlows'
    TSYS = 'TSYS'
    VALITOR = 'Valitor'
    ELAVONPOS = 'Elavon POS'
    CREDORAX = 'Credorax'
    FIRSTCITIZENS='First Citizens'

    # Global One gateway
    TSYS_SARATOGA = 'TSYS Saratoga'
    CTPAY = 'CT Payments'
    PROPAY = 'ProPay'
    NMI = 'NMI'  # + Elavon
    AUTHNET = 'Authorize.Net' # + AnywhereCommerce , Pago, Elavon
    PAYVISION = 'Payvision'
    PAYVISIONV2 = 'PayvisionV2'
    GLOBALCOLLECT = 'GlobalCollect'
    INGENICO = 'Ingenico'
    VACP = 'VACP' # + AnywhereCommerce
    MONERIS = 'Moneris'
    INTEGRAPAY = 'IntegraPay'
    PAYPAL = 'PayPal'
    PAYSAFE = 'PaySafe'
    BEANSTREAM = 'Beanstream'

    # Pago
    RIETUMU='Rietumu'
    FIRSTDATALATVIA='First Data Latvia'

    # AnywhereCommerce
    FDRCDW = 'FDRC DW'

    # NCB
    NCB = 'NCB'

    # nobody
    ACHJH = 'ACH Jack Henry'
    CHINAUNIONPAY = 'ChinaUnionPay'

    def __init__(self, name_):
        self.name_ = name_

    @staticmethod
    def all():
        return list(b.bank for b in Acquirer)


class Gateway(Enum):
    WORLDNETTPS = ('WorldNet TPS')
    GLOBALONEPAY = ('GlobalOnePay')
    ANYWHERECOMMERCE = ('AnywhereCommerce')


class Country(Enum):
    Argentina = ('ARG', 'AR')
    Afghanistan = ('AFG', 'AF')
    Australia = ('AUS', 'AU')
    Brazil = ('BRA', 'BR')
    Colombia = ('COL', 'CO')
    Ireland = ('IRL', 'IE')
    Mexico = ('MEX', 'MX')
    Panama = ('PAN', 'PA')
    Peru = ('PER', 'PE')
    Russia = ('RUS', 'RU')
    Jamaica = ('JM', 'JM')
    USA = ('USA', 'US')
    CANADA = ('CAN', 'CA')

    def __init__(self, code, short_code):
        self.code = code
        self.short_code = short_code


class TimeZone(Enum):
    LONDON = 'Europe/London'
    MOSCOW = 'Europe/Moscow'
    CHICAGO = 'America/Chicago'
    GMT = 'GMT'

    def __init__(self, timezone):
        self.timezone = timezone


class RoutingNumber(Enum):
    ARIZONA = ('122100024', 'AZ')
    CALIFORNIA = ('322271627', 'CA')
    COLORADO = ('102001017', 'CO')
    CONNECTICUT = ('021100361', 'CT')
    FLORIDA = ('267084131', 'FL')
    IDAHO = ('123271978', 'ID')
    ILLINOIS = ('071000013', 'IL')
    INDIANA = ('074000010', 'IN')
    KENTUCKY = ('083000137', 'KY')
    LOUISIANA = ('065400137', 'LA')
    GEORGIA = ('061092387', 'GE')
    MICHIGAN = ('072000326', 'MI')
    NEVADA = ('322271627', 'NV')
    OHIO = ('044000037', 'OH')
    OKLAHOMA = ('103000648', 'OK')
    OREGON = ('325070760', 'OR')
    TEXAS = ('111000614', 'TX')
    UTAH = ('124001545', 'UT')
    WASHINGTON = ('325070760', 'WA')

    def __init__(self, rn, code):
        self.rn = rn
        self.code = code

    @staticmethod
    def rand_rn():
        return random.choice(list(r.rn for r in RoutingNumber))

    @staticmethod
    def rand_code():
        return random.choice(list(r.code for r in RoutingNumber))

    @staticmethod
    def rand_us_state_name():
        return random.choice(list(r.name for r in RoutingNumber))


class CardReadMethod:
    KEYED = 1
    SWIPED = 2
    ICC = 3
    SWIPED_FALLBACK = 4
    CONTACTLESS_MSR = 5
    CONTACTLESS_ICC = 6


class SecCode(Enum):
    WEB = 'WEB'
    PPD = 'PPD'
    CCD = 'CCD'
    TEL = 'TEL'

    def __init__(self, code):
        self.code = code

    def __str__(self):
        return self.type

    @staticmethod
    def all():
        return list(r.rn for r in SecCode)

    @staticmethod
    def rand():
        return random.choice(list(r.code for r in SecCode))


class AccountType(Enum):
    CHEQUE = (0, 'CHECKING')
    SAVINGS = (1, 'SAVINGS')

    def __init__(self, code, description):
        self.code = code
        self.description = description

    def code(self):
        return self.code

    def description(self):
        return self.description

    @staticmethod
    def all():
        return list(at.name for at in AccountType)

    @staticmethod
    def rand():
        return random.choice(list(at for at in AccountType))

    @staticmethod
    def find_by_code(code):
        try:
            return list(filter(lambda c: c.code == int(code), list(c for c in AccountType)))[0]
        except IndexError:
            return None


class TerminalType:
    MOTO = 1
    INTERNET = 2
    CHP = 3


class TransactionType:
    CHP = 0
    RECURRING = 2
    INSTALLMENT = 3
    THREE_DS = 5
    MOTO = 4
    INTERNET = 7


class TransactionStatus:
    PENDING = 1
    READY = 2
    VOID = 3
    DECLINED = 4
    COMPLETE = 5
    REFERRAL = 6
    PICKUP = 7
    REVERSAL = 8
    SENT = 9
    ADMIN = 10
    EXPIRED = 11
    IN_PROGRESS = 12
    REVIEW = 13


class Currency(Enum):
    EUR = (978, 2)
    GBP = (826, 2)
    USD = (840, 2)
    JPY = (392, 0)
    BHD = (48, 3)
    JMD = (388, 2)
    AUD = (36, 2)
    CAD = (124, 2)
    MXN = (484, 2)
    DKK = (208, 2)
    KWD = (414, 3)

    def __init__(self, code, minorunits):
        self.code = code
        self.minorunits = minorunits

    @staticmethod
    def rand():
        return random.choice(list(c for c in Currency))

    @staticmethod
    def get_name(code: int):
        return list(filter(lambda field: field.code == code, list(c for c in Currency)))[0].name


class TestingCardNumber(Enum):  # TODO
    CYBERSOURCESOAP_CARD = '4000100011112224'
    CUP_CARDS = ['6250947000000014', '6250947000000012']


class FiServCard(Enum):
    FS1 = ('6007602801003837964', '51C096C5F32D0E63', 'FFFF5678901234E00001', 'FOOD_STAMP')
    FS2 = ('6007602801003837965', '51C096C5F32D0E63', 'FFFF5678901234E00001', 'FOOD_STAMP')
    FS3 = ('5780369000590202',    '8B899B696B969B36', 'FFFF5678901234E00001', 'FOOD_STAMP')
    C1 = ('6007602801003837967',  '51C096C5F32D0E63', 'FFFF5678901234E00001', 'CASH')
    C2 = ('6007602801003837968',  '51C096C5F32D0E63', 'FFFF5678901234E00001', 'CASH')
    C3 = ('5780369000590574',     '76D7A2B6ECC25C12', 'FFFF5678901234E00001', 'CASH')

    def __init__(self, cardnum, pin, ksn, cardaccount):
        self.cardnum = cardnum
        self.pin = pin
        self.ksn = ksn
        self.cardaccount = cardaccount

    @staticmethod
    def rand():
        return random.choice(list(sfc for sfc in FiServCard))


INTERAC_CARDS = ['4506445205481300', '4506443412734314', '4506447271922985', '4506443486459855', '4506441744944056']


class EdccCard(Enum):
    GBP_VISA = ('4485910301709438', 'VISA')
    JPY_VISA = ('4929545260267764', 'VISA')
    KWD_MC = ('5375750348038510', 'MASTERCARD')
    EUR_AMEX = ('345481249963592', 'AMEX')

    def __init__(self, cardnum, cardtype):
        self.cardnum = cardnum
        self.cardtype = cardtype


class EdccRates(Enum):
    USD = (840, 1)
    EUR = (978, 0.831400)
    JPY = (392, 106.711095)
    GBP = (826, 0.729518)
    KWD = (414, 0.302832)
    CAD = (124, 0.573600)

    def __init__(self, currency_code, rate):
        self.currency_code = currency_code
        self.rate = rate


class DebitCard(Enum):
    VISA_DEBIT = ('4022025545957451', 'Visa Debit')
    DEBIT_MASTERCARD = ('5459318190424243', 'Debit Mastercard')

    def __init__(self, cardnum, cardtype):
        self.cardnum = cardnum
        self.cardtype = cardtype

    @staticmethod
    def rand():
        return random.choice(list(sfc for sfc in DebitCard))


# boarding constants
class LocalMerchant(Enum):
    WN = ('LXME5UYB6I', 'wn', 20)
    GO = ('J68JGA4F5J', 'go', 58)
    PAGO = ('D7VLON2RMA', 'pago', 59)
    AC = ('DLWPLH4G6X', 'ac', 60)
    GOEPAY = ('LXME5UYB6I', 'goepay', 22)
    PAYCONEX = ('LU446NFW8G', 'payconex', 9)
    NCB = ('DLWPLH4G6X', 'ncb', 23)

    def __init__(self, itemid, dba_name, db_id):
        self.itemid = itemid
        self.dba_name = dba_name
        self.db_id = db_id


class VagrantMerchant(Enum):
    WN = ('HLBVO0XFZW', 'merchant_wn', 21)
    GO = ('ETY0YG3JVH', 'merchant_go', 21)

    def __init__(self, itemid, dba_name, db_id):
        self.itemid = itemid
        self.dba_name = dba_name
        self.db_id = db_id


class HoundMerchant(Enum):
    WN = ('FM0CQ6F0TC', 'archiving_wn', 350)
    GO = ('L4S25C2T4N', 'archiving_go', 352)
    PAGO = ('IC8440QRSP', 'archiving_pago', 354)
    AC = ('L37XPOQMB7', 'archiving_ac', 356)
    GOEPAY = ('FIW3UVQNCL', 'archiving_pago', 358)

    def __init__(self, itemid, dba_name, db_id):
        self.itemid = itemid
        self.dba_name = dba_name
        self.db_id = db_id


class EventType(Enum):
    APPROVED = ("Approved", 2)
    BAD_ACCOUNT = ("Returned Bad Account", 17)
    CAPTURED = ("Captured", 5)
    COLLECTION_FAILED = ("Collection Failed", 10)
    COLLECTED = ("Collected", 9)
    DECLINED = ("Declined", 1)
    DISPUTED = ("Disputed", 15)
    ORIGINATED = ("Originated", 11)
    PROCESSED = ("Processed", 8)
    PROCESSING_ERROR = ("Processing Error", 3)
    REFUNDED = ("Refunded", 6)
    RETURNED_NSF = ("Returned NSF", 16)
    SENT_TO_COLLECTION = ("Sent To Collection", 14)
    RETURNED_BAD_ACCOUNT = ("Returned Bad Account", 17)
    SETTLED = ("Settled", 12)
    VOIDED = ("Voided", 4)
    UNAUTHORIZED = ("Unauthorized", 21)
    CHARGED_BACK = ("Charged Back", 22)
    NOTICE_OF_CHANGE = ("Notice Of Change", 19)

    def __init__(self, status, tid):
        self.status = status
        self.tid = tid

    def __str__(self):
        return str(self.status)

    def status(self):
        return str(self.status)

    def tid(self):  # enum AchJhEventTypeEnum index
        return str(self.tid)


class SettlementStatus(Enum):
    CHARGED_BACK = ("Charged Back", 7)
    NO_SETTLEMENT_NEEDED = ("No Settlement Needed", 1)
    PENDING = ("Originated / Settlement Pending", 4)
    SETTLED = ("Settled", 6)
    TO_BE_ORIGINATED = ("To Be Originated", 2)
    ORIGINATING = ("Originating", 3)

    def __init__(self, status, sid):
        self.status = status
        self.sid = sid

    def __str__(self):
        return str(self.status)

    def status(self):
        return str(self.status)

    def sid(self):
        return str(self.sid)


class AchJhTransactionStatus(Enum):
    APPROVED = ("Approved", 2)
    COLLECTED = ("Collected", 6)
    CLOSED_ACCOUNT = ("Invalid / Closed Account", 15)
    DECLINED = ("Declined", 1)
    DISPUTED = ("Disputed", 13)
    ERROR = ("Error", 3)
    IN_COLLECTION = ("In Collection", 10)
    PROCESSED = ("Processed", 5)
    UNCOLLECTED_NSF = ("Uncollected NSF", 14)
    VOIDED = ("Voided", 4)

    def __init__(self, status, tid):
        self.status = status
        self.tid = tid

    def __str__(self):
        return str(self.status)

    def status(self):
        return str(self.status)

    def tid(self):
        return str(self.tid)


class StoredCredentialTxType(Enum):
    FIRST_TXN = '1'
    SUBSEQUENT_MERCHANT_INITIATED_TXN = '2'
    SUBSEQUENT_CARDHOLDER_INITIATED_TXN = '3'
    EMPTY = ''
    INCORRECT = '4'

    def __init__(self, sid):
        self.sid = sid

    def __str__(self):
        return str(self.text)

    def sid(self):
        return self.sid

    @staticmethod
    def rand():
        return random.choice(list(sctt for sctt in StoredCredentialTxType))


class MerchantPortfolio(Enum):
    WN = 'HLBVO0XFZW'
    GO = 'ETY0YG3JVH'
    PAGO = 'KCPQDLRC7R'
    AC = 'C101T7XH12'
    GOEPAY = 'ESDWISRD95'

    def __init__(self, mpid):
        self.mpid = mpid


class StoredCredentialUse(Enum):
    UNSCHEDULED = 1
    RECURRING = 2
    INSTALLMENT = 3

    def __init__(self, sid):
        self.sid = sid

    def sid(self):
        return self.sid

    @staticmethod
    def rand():
        return random.choice(list(scu for scu in StoredCredentialUse))


class SecureCardAchJh(Enum):
    ACH_SAVING = ('2967533122408153', 'sc_ach_saving', '5202907946145241')
    ACH_CHECKING = ('2967536702391871', 'sc_ach_checking', '7868562')

    def __init__(self, card_ref, merchant_ref, cardnumber):
        self.card_ref = card_ref
        self.merchant_ref = merchant_ref
        self.cardnumber = cardnumber

    @staticmethod
    def rand():
        return random.choice(list(scach for scach in SecureCardAchJh))


class SecureCard(Enum):
    AMEX = ('2967533079202096', 'sc_amex', '371291766048785', 'Curt Ashcraft', '3453409893', 'sc_amex@local.host', datetime(2019, 10, 10))
    DINERS = ('2967538120028127', 'sc_diners', '36001264340965', 'Suzanne Willis', '3458973495893', 'sc_diners@local.host', datetime(2019, 10, 9))
    MASTERCARD_DEBIT = ('2967532561720953', 'sc_mastercard_debit', '5459318190424243', 'Vickey Ornelas', '34332523223', 'sc_mastercard_debit@local.host', datetime(2019, 10, 8))
    JCB = ('2967535856939949', 'sc_jcb', '1800055108046305', 'Sonia Turney', '348573894789', 'sc_jcb@local.host', datetime(2019, 10, 7))
    VISA_ELECTRON = ('2967536006966170', 'sc_visa_electron', '4056145993378536', 'Cory Vendoka', '3458275878', 'sc_visa_electron@local.host', datetime(2019, 10, 6))
    VISA_DEBIT = ('2967535794723470', 'sc_visa_debit', '4022025545957451', 'Blair Rabideau', '2348723894', 'sc_visa_debit@local.host', datetime(2019, 10, 5))
    VISA = ('2967538835220910', 'sc_visa', '4532310185413129', 'Rosario S Sherman', '2384293849238', 'sc_visa@local.host', datetime(2019, 10, 4))
    MASTERCARD = ('2967538872030685', 'sc_mastercard', '5533986315065685', 'David M Blair', '349857893457', 'sc_mastercard@local.host', datetime(2019, 10, 3))

    def __init__(self, card_ref, merchant_ref, cardnumber, cardholdername, phone, email, creationdate):
        self.card_ref = card_ref
        self.merchant_ref = merchant_ref
        self.cardnumber = cardnumber
        self.cardholdername = cardholdername
        self.phone = phone
        self.email = email
        self.creationdate = creationdate

    @staticmethod
    def rand():
        return random.choice(list(sc for sc in SecureCard))


class CashFlowsSecureCard(Enum):
    VISA_UNSC = ('sc_visa_unsc', '4000000000000002', '123', StoredCredentialUse.UNSCHEDULED)
    VISA_INST = ('sc_visa_inst', '4000000000000002', '123', StoredCredentialUse.INSTALLMENT)
    VISA_SUBS = ('sc_visa_subs', '4000000000000002', '123', StoredCredentialUse.RECURRING)
    MC_UNSC = ('sc_mc_unsc', '5555555555554444', '321', StoredCredentialUse.UNSCHEDULED)
    MC_INST = ('sc_mc_inst', '5555555555554444', '321', StoredCredentialUse.INSTALLMENT)
    MC_SUBS = ('sc_mc_subs', '5555555555554444', '321', StoredCredentialUse.RECURRING)

    def __init__(self, merchant_ref, cardnumber, cvv, cof_use):
        self.merchant_ref = merchant_ref
        self.cardnumber = cardnumber
        self.cvv = cvv
        self.cof_use = cof_use


class CashFlowsNoCofSecureCard(Enum):
    # Disable CoF for acquirer before creating secure cards
    # UPDATE `acquirer` SET `allow_account_verification_request`='0', `supports_cof`='0' WHERE `id`='5';
    VISA_NO_COF = ('sc_visa_no_cof', '4000000000000002', '123', None)
    MC_NO_COF = ('sc_mc_no_cof', '5555555555554444', '321', None)

    def __init__(self, merchant_ref, cardnumber, cvv, cof_use):
        self.merchant_ref = merchant_ref
        self.cardnumber = cardnumber
        self.cvv = cvv
        self.cof_use = cof_use


class MsrPayload(Enum):
    # KSN 88888835400002200001, BDK index 2, WISEPAD
    VISA = ('4444333322221111', '2210', '10114991888', '031EDDDCEE644A11C1F4A977D23CD990BE4F75DEC4C1F045')
    MASTERCARD = ('5132529831559065', '2304', '10224891777', '9709EC7933CBF4E1B1F7A21049AC3C3E1A047AC55DC2EE85')
    MASTERCARD_ICC = ('5485039916479513', '2410', '10225892787', '')

    def __init__(self, cardnumber, expiry, postfix, encrypted):
        self.cardnumber = cardnumber
        self.expiry = expiry
        self.postfix = postfix
        self.encrypted = encrypted

    def get_payload(self):
        return f';{self.cardnumber}={self.expiry}{self.postfix}?'

    def get_masked_pan(self, separator='*'):
        return self.cardnumber[:6] + separator * 6 + self.cardnumber[-4:]


class PaynomixCard(Enum):
    VISA = ('4242424242424242', 'sc_visa')
    VISA_DEBIT = ('4000056655665556', 'sc_visa_debit')
    MASTERCARD = ('5555555555554444', 'sc_mc')
    MASTERCARD_DEBIT = ('2223003122003222', 'sc_mc_debit')
    MASTERCARD_PREPAID = ('5105105105105100', 'sc_mc_prepaid')
    AMEX = ('378282246310005', 'sc_amex')
    DISCOVER = ('6011111111111117', 'sc_discover')

    def __init__(self, cardnumber, merchant_ref):
        self.cardnumber = cardnumber
        self.merchant_ref = merchant_ref

    @staticmethod
    def rand():
        return random.choice(list(sc for sc in PaynomixCard))


class MpiData(Enum):
    FIRST = ('2B3Bf0kvk8Hyjt2dbKCFdDWvHUw=', 'jDfp08DVR6+2CBEAMOuyAigAAAA=', 'dd9d6ca0857435af1d4c')

    def __init__(self, xid, cavv, mpiref):
        self.xid = xid
        self.cavv = cavv
        self.mpiref = mpiref


class PaylinkAuthType(Enum):
    PAYMENT = 'PAYMENT'
    PRE_AUTH = 'PRE_AUTH'

    def __str__(self):
        return self.value


class ApiKey(Enum):
    BOARDING_WN_FULL = 'boarding_wn_full'
    BOARDING_WN_READ = 'boarding_wn_read'
    BOARDING_NCB_FULL = 'boarding_ncb_full'
    BOARDING_GO_FULL = 'boarding_go_full'
    BOARDING_GO_READ = 'boarding_go_read'
    BOARDING_GOEPAY_FULL = 'boarding_goepay_full'
    API_GO_FULL = 'api_go_full'
    API_WN_FULL = 'api_wn_full'
    API_NCB_FULL = 'api_ncb_full'

    def __str__(self):
        return str(self.value)

    def __get__(self, instance=None, owner=None):
        return str(self.value)


class EmvTlv(Enum):
    # ksn = 88888835400002200001, device = WALKER
    # 4444333322221111
    # 9F39: 07 - Contactless ICC
    CONTACTLESS_ICC = '4F07A0000000031010500A4d41535445524341524457134444333322221111D20121011796251900000f5A08444433332222111182027C008407A00000000310108A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950508800080009A032007159B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000001010009F03060000000000009F0607A00000000310109F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120210a00003240000000000000000000000ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000100019F1E0831323334353637389F21030931409F260848438A8F1AD9A0589F2701809F33036028C89F34035E03009F3501219F360200019F37047BC6785F9F3901079F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'
    CONTACTLESS_NO_TRACK2 = '82027C008407A00000000310108A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950508800080009A032007159B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000001010009F03060000000000009F0607A00000000310109F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120210a00003240000000000000000000000ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000100019F1E0831323334353637389F21030931409F260848438A8F1AD9A0589F2701809F33036028C89F34035E03009F3501219F360200019F37047BC6785F9F3901079F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'
    CONTACTLESS_ICC_MC_CREDIT = '4F07a0000000041010500A4d41535445524341524457115485039916479513D241020111438780895A085485039916479513820258008407a00000000410108A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950542000080009A032007309B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000000103009F03060000000000009F0607a00000000410109F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120210a00003240000000000000000000000ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000010119F1E0831323334353637389F21031253529F260810CE4CE5A7E926DF9F2701809F33036028C89F34035E03009F3501219F360200049F370428B3CE3A9F3901059F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'
    CONTACTLESS_ICC_VISA_DEBIT = '4F050000000000500A4d41535445524341524457114022025545957451D241220111438780895A084022025545957451840500000000008A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950500000800009A032007309B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000000101009F03060000000000009F060500000000009F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120210a00003240000000000000000000000ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000010119F1E0831323334353637389F21031133389F26082FAEDBB4DFFB52CF9F2701809F33036028C89F34035E03009F3501219F360200029F37041AD233539F3901059F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'
    CONTACTLESS_ICC_MC_DEBIT = '4F050000000000500A4d41535445524341524457115459318190424243D241120111438780895A085459318190424243840500000000008A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950500000800009A032007309B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000000102009F03060000000000009F060500000000009F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120210a00003240000000000000000000000ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000010119F1E0831323334353637389F21031133389F26080B1F187C2AF5525E9F2701809F33036028C89F34035E03009F3501219F360200039F37045DE22C4C9F3901059F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'
    CONTACTLESS_ICC_AMEX = '4F07A0000000250000500A4d4153544552434152445711376398252446046D26112011143878089f5A08376398252446046f820200008407A00000002500008A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950500000000009A032007319B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000000104009F03060000000000009F0607A00000002500009F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120210a00003240000000000000000000000ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000010119F1E0831323334353637389F21031355149F26081B144E4D6094AA7E9F2701809F33036028C89F34035E03009F3501219F360200059F37046A909B829F3901059F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'
    CONTACTLESS_ICC_DISCOVER = '4F07A0000001523010500A4d41535445524341524457116011398438856405D261220111438780895A086011398438856405820200008407A00000015230108A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950500000000009A032007319B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000000105009F03060000000000009F0607A00000015230109F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120210a00003240000000000000000000000ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000010119F1E0831323334353637389F21031355149F26081096BF0E8FC8E9079F2701809F33036028C89F34035E03009F3501219F360200069F37041ADF47BF9F3901059F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'
    # 9F10 = 0220ab0003250000000000000000000011ff instead of 0210a00003240000000000000000000000ff
    CONTACTLESS_ICC_9F10_CHANGED = '4F07A0000000031010500A4d41535445524341524457134444333322221111D20121011796251900000f5A08444433332222111182027C008407A00000000310108A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950508800080009A032007159B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000001010009F03060000000000009F0607A00000000310109F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120220ab0003250000000000000000000011ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000100019F1E0831323334353637389F21030931409F260848438A8F1AD9A0589F2701809F33036028C89F34035E03009F3501219F360200019F37047BC6785F9F3901079F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'
    # 9F39: 91 - Contactless MSR
    CONTACTLESS_MSR = '4F07A0000000031010500A4d41535445524341524457134444333322221111D20121011796251900000f5A08444433332222111182027C008407A00000000310108A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950508800080009A032007159B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000001010009F03060000000000009F0607A00000000310109F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120210a00003240000000000000000000000ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000100019F1E0831323334353637389F21030931409F2608F564AEF2EBFACA6D9F2701809F33036028C89F34035E03009F3501219F360200029F3704736EA8629F3901919F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'
    # 9F39: 00 - Unspecified
    UNSPECIFIED = '4F07A0000000031010500A4d41535445524341524457134444333322221111D20121011796251900000f5A08444433332222111182027C008407A00000000310108A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950508800080009A032007159B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000001010009F03060000000000009F0607A00000000310109F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120210a00003240000000000000000000000ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000100019F1E0831323334353637389F21030931409F26080D30ACA866E06B6B9F2701809F33036028C89F34035E03009F3501219F360200039F37046990B7BA9F3901009F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'
    # 9F39: absent
    TAG_9F39_ABSENT = '4F07A0000000031010500A4d41535445524341524457134444333322221111D20121011796251900000f5A08444433332222111182027C008407A00000000310108A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950508800080009A032007159B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000001010009F03060000000000009F0607A00000000310109F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120210a00003240000000000000000000000ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000100019F1E0831323334353637389F21030931409F2608922C9B7727370FE69F2701809F33036028C89F34035E03009F3501219F360200049F3704119A0E529F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'
    # 9F66:8F72C0D9
    TAG_9F66 = '4F07A0000000031010500A4d41535445524341524457114444333322221111D201220111438780895A08444433332222111182027C008407A00000000310108A025a318C159F02069F03069F1A0295055F2A029A039C019F37048D0C910a8a0295059f37049f4c088E0C910a8a0295059f37049f4c08950508800080009A032007239B02E8009C0150C00A88888835400002200001C408541333ffffff0681C70A88828888888888e00174C81860d743c93014856dbed7bd9815914b4bc32f47e76c53b006CD082a2a18971dcafc43CE0A88858888888888e0026f5F20084A6F686E20446F655F24031912315F25030401015F2A0208405F300202015F3401179F01060000000000019F02060000001010009F03060000000000009F0607A00000000310109F0702ff009F090200029F0D05fc50a000009F0E0500000000009F0F05f870a498009F10120210a00003240000000000000000000000ff9F120A4d6173746572436172649F160F3132333435363738393031323334359F1A0208409F1C04000010119F1E0831323334353637389F21031259529F2608739D41D02EC7063E9F2701809F33036028C89F34035E03009F3501219F360200019F37047B77AE089F3901059F40057e0020b0019F4104000002559F420208409F4E152020202020202d2054657374204d65726368616e749F66048F72C0D99F6E06005611123031DF780788888835400002DF791000003300b135ff832636454e1f000830'


class PosDevice(Enum):
    BLUEPAD50 = (1, 'BLUEPAD50', None)
    RAMBLER = (2, 'RAMBLER', 'RAN003')
    WISEPAD = (24, 'WISEPAD', 'RWO010')
    WALKER_C2X = (27, 'WALKER_C2X', 'RWO010')
    PAX_A80_ATTENDED = (48, 'PAX_A80_ATTENDED', 'RWO013')
    PAX_A920_ATTENDED = (49, 'PAX_A80_ATTENDED', 'RWO013')

    def __init__(self, device_id, device_name, tpp_id):
        self.device_id = device_id
        self.device_name = device_name
        self.tpp_id = tpp_id

    def __str__(self):
        return str(self.device_name)


class IsvToken(Enum):
    WN = ('1639bab678e410c2a01f887bf8f8865cebdbc83bf20bd27ec79f8c5fa44b5691bcbcb02aa47cbf290dadabb12340cf1ae2c8ff5544120c151802b461f813b3a3',
          '2016c90c83490cc04cbe6d22a679788743f2df4ac3351464e2a52c40bc50cb7bdcb5d8780569b0a6f7bfb54d56fb6f02b6e5ce49835172d4b5e72212c28d5cee')
    GO = ('bdd56591ac0d18e494228344daaf6e8e0bd2ec1a1bafe7ac3f82bd591450a61e92e1f177080be28037e40aec50ee9ff3ddcaa8223242eee2b55bae73c800d11a',
          'cf7ea3d2a4291cbf1d33a2e5c4f32b1353b776b6a1964e8e4d9eca3159872a9ee9022200f69eab8d9bce619d462f77df394a59fb869466f2a3fe1d6b2b9e3b6')

    def __init__(self, token_rest_api, token_merchant_api):
        self.token_rest_api = token_rest_api
        self.token_merchant_api = token_merchant_api
