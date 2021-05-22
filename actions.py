import hashlib
import json
from datetime import datetime
from io import BytesIO

from faker import Factory
from lxml import etree

from constants import CARDTYPES, Currency
from data.rest_requests import rest_sale, rest_referenced_refund, rest_unreferenced_card_refund
from data.xml_paylink_requests import send_paylink_request
from data.xml_requests import preauth, payment, ach_payment, ach_secure_registration, securecard_registration, \
    stored_subscription, account_verification_request, send_payment_link_request, create_payment_link_request
from db.db_helpers import TransactionsHelper, UtilityHelper, SecureCardHelper
from decorators import session_logging
from model.boarding import parseLiteral as boardingParseLiteral, cardsType, levelDataEnum, apiAddressModeEnum, \
    merchantGeneralSetup, avsActionEnum
from model.boarding import terminal, merchant, user
from model.gateway import PAYMENT, parseLiteral, PREAUTH, PAYMENTACH, ACHSECUREREGISTRATION, SECURECARDREGISTRATION, \
    ADDSTOREDSUBSCRIPTION, REFUND, ACCOUNT_VERIFICATION, SECURECARDUPDATE, SECURECARDSEARCH, ADDSUBSCRIPTION, \
    SUBSCRIPTIONPAYMENT, GETCARDCURRENCYRATE, SECURECARDREMOVAL, DELETESTOREDSUBSCRIPTION, SECURE_CARD_ADVANCED_SEARCH, \
    PREAUTHCOMPLETION, TERMINAL_CONFIGURATION, UPDATESUBSCRIPTION
from model.paylink import CREATE
from model.paylink import parseLiteral as paylinkParseLiteral
from model.rest import parseLiteral as restParseLiteral, reversal, tipAdjustment, tipType, transactionUpdate, account, \
    terminalType, authTokenRequest, authenticationRequest, secureCard
from serializer import HppSerializable
from utils import logger
from utils import today

fake = Factory.create()


class BaseSource(object):
    def __init__(self, path='/merchant', session=None, terminal_id=None, terminal_secret='someSecretPhrase'):
        self._path = path
        self._session = session
        self._terminal_secret = terminal_secret
        self._terminal_id = terminal_id

    def with_terminal(self, terminal_id):
        self._terminal_id = terminal_id
        return self

    def with_header(self, header):
        self._session.with_headers(header)
        return self


class HppSource(BaseSource):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = self._session.url + self._path

    @session_logging()
    def paymentpage(self, params, silence=False):
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
        params.xml()  # calculate hash
        self._session.with_headers(header).with_method('post').with_url(self.url + '/paymentpage')\
            .with_params(params.__dict__).request.content
        return HppSerializable(self._session.with_headers(header).with_method('post').with_url(self.url + '/payment')
                               .with_params(params.__dict__).request.content)

    @session_logging()
    def securecard(self, params, action='REGISTER', silence=False):
        method = 'post' if action == 'REGISTER' else 'update'
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
        params.xml()  # calculate hash
        request1 = self._session.with_headers(header).with_method(method).with_url(self.url + '/paymentpage').with_params(params.__dict__)
        response1 = request1.request.content
        request2 = self._session.with_headers(header).with_method(method).with_url(self.url + '/payment').with_params(params.__dict__)
        r = HppSerializable(request2.request.content)
        return r


class XmlSource(BaseSource):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = self._session.url + self._path + '/xmlpayment'
        self._session.with_headers({'Content-Type': 'application/xml'})

    @session_logging()
    def payment(self, request: PAYMENT = None, is_multicurrency=False, silence=False):
        request = (request if request is not None else payment())
        request.multicurrency = is_multicurrency

        self._session.with_method('post').with_url(self.url).with_data(
            request.with_field(TERMINALID=self._terminal_id).xml()
        )
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        response.terminal_id = self._terminal_id
        response.multicurrency = is_multicurrency
        setattr(response, 'AMOUNT', request.AMOUNT)
        setattr(response, 'SECRET', self._terminal_secret)
        setattr(response, 'CURRENCY', request.CURRENCY)
        return response

    @session_logging()
    def preauth(self, request: PREAUTH = None, currency=Currency.USD, is_multicurrency=False, silence=False):
        request = (request if request is not None else preauth(currency=currency))
        request.multicurrency = is_multicurrency

        self._session.with_method('post').with_url(self.url).with_data(
            request.with_field(TERMINALID=self._terminal_id).xml()
        )
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        response.terminal_id = self._terminal_id
        response.multicurrency = is_multicurrency

        setattr(response, 'AMOUNT', request.AMOUNT)
        setattr(response, 'SECRET', self._terminal_secret)
        setattr(response, 'CURRENCY', request.CURRENCY)
        return response

    @session_logging()
    def preauthcompletion(self, uniquerf, amount: float, currency: Currency = Currency.USD, is_multicurrency=False, silence=False):
        request = PREAUTHCOMPLETION(
            UNIQUEREF=uniquerf,
            AMOUNT=amount,
            DATETIME=str(today())
        )
        setattr(request, 'CURRENCY', currency.name)
        self._session.with_method('post').with_url(self.url).with_data(request.with_field(TERMINALID=self._terminal_id).xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        response.terminal_id = self._terminal_id
        response.multicurrency = is_multicurrency
        setattr(response, 'CURRENCY', currency.name)
        setattr(response, 'AMOUNT', request.AMOUNT)
        setattr(response, 'SECRET', self._terminal_secret)
        return response

    @session_logging()
    def secure_card_registration(self, request: SECURECARDREGISTRATION = None, silence=False):
        self._session.with_method('post').with_url(self.url).with_data(
            (request if request is not None else securecard_registration()).with_field(TERMINALID=self._terminal_id).xml()
        )
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        response.terminal_id = self._terminal_id
        return response

    @session_logging()
    def secure_card_update(self, request: SECURECARDUPDATE = None, silence=False):
        self._session.with_method('post').with_url(self.url).with_data(request.with_field(TERMINALID=self._terminal_id).xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def secure_card_search(self, merchantref: str, silence=False):
        request = SECURECARDSEARCH(
            MERCHANTREF=merchantref,
            TERMINALID=self._terminal_id,
            DATETIME=str(today())
        )
        self._session.with_method('post').with_url(self.url).with_data(request.xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def secure_card_advanced_search(self, **kwargs):
        request = SECURE_CARD_ADVANCED_SEARCH(TERMINALID=self._terminal_id, DATETIME=str(today()))
        request.with_field(**kwargs)
        self._session.with_method('post').with_url(self.url).with_data(request.xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def secure_card_removal(self, merchantref: str, cardreference: str, silence=False):
        request = SECURECARDREMOVAL(
            MERCHANTREF=merchantref,
            TERMINALID=self._terminal_id,
            CARDREFERENCE=cardreference,
            DATETIME=str(today())
        )
        self._session.with_method('post').with_url(self.url).with_data(request.xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        response.terminal_id = self._terminal_id
        return response

    @session_logging()
    def add_stored_subscription(self, request: ADDSTOREDSUBSCRIPTION = None, currency: Currency = Currency.USD, silence=False):
        r = (request if request is not None else stored_subscription())
        r.CURRENCY = currency.name
        self._session.with_method('post').with_url(self.url).with_data(r.with_field(TERMINALID=self._terminal_id).xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        response.terminal_id = self._terminal_id
        return response

    @session_logging()
    def delete_stored_subscription(self, merchantref: str, silence=False):
        request = DELETESTOREDSUBSCRIPTION(
            MERCHANTREF=merchantref,
            TERMINALID=self._terminal_id,
            DATETIME=str(today())
        )
        self._session.with_method('post').with_url(self.url).with_data(request.xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        response.terminal_id = self._terminal_id
        return response

    @session_logging()
    def add_subscription(self, request: ADDSUBSCRIPTION, currency=Currency.USD, silence=False):
        request.CURRENCY = currency.name
        self._session.with_method('post').with_url(self.url)\
            .with_data(request.with_field(TERMINALID=self._terminal_id).xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def update_subscription(self, request: UPDATESUBSCRIPTION, currency=Currency.USD, silence=False):
        request.CURRENCY = currency.name
        self._session.with_method('post').with_url(self.url)\
            .with_data(request.with_field(TERMINALID=self._terminal_id).xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def subscription_payment(self, request: SUBSCRIPTIONPAYMENT, currency: Currency, silence=False):
        setattr(request, 'CURRENCY', currency.name)
        self._session.with_method('post').with_url(self.url)\
            .with_data(request.with_field(TERMINALID=self._terminal_id).xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def ach_payment(self, request: PAYMENTACH = None, silence=False):
        self._session.with_method('post').with_url(self.url).with_data(
            (request if request is not None else ach_payment()).with_field(TERMINALID=self._terminal_id).xml()
        )
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def ach_secure_registration(self, request: ACHSECUREREGISTRATION = None, silence=False):
        self._session.with_method('post').with_url(self.url).with_data(
            (request if request is not None else ach_secure_registration()).with_field(TERMINALID=self._terminal_id).xml()
        )
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def refund(self, uniqueref, amount: float, currency: Currency, silence=False):
        refund = REFUND(
            UNIQUEREF=uniqueref,
            AMOUNT=amount,
            DATETIME=str(today()),
            OPERATOR=fake.name(),
            REASON=fake.text(15),
            AUTOREADY='C'
        )
        setattr(refund, 'CURRENCY', currency.name)
        self._session.with_method('post').with_url(self.url).with_data(
            refund.with_field(TERMINALID=self._terminal_id).xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def account_verification(self, request: ACCOUNT_VERIFICATION=None, silence=False):
        self._session.with_method('post').with_url(self.url).with_data(
            (request if request is not None else account_verification_request()).with_field(TERMINALID=self._terminal_id).xml()
        )

        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        response.terminal_id = self._terminal_id
        return response

    @session_logging()
    def get_card_currency_rate(self, card_bin, base_amount, silence=False):
        request = GETCARDCURRENCYRATE(
            CARDBIN=card_bin,
            BASEAMOUNT=base_amount,
            DATETIME=str(today())
        )
        self._session.with_method('post').with_url(self.url).with_data(
            request.with_field(TERMINALID=self._terminal_id).xml()
        )

        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def terminal_configuration(self, silence=False):
        request = TERMINAL_CONFIGURATION(DATETIME=str(today()))
        self._session.with_method('post').with_url(self.url).with_data(request.with_field(TERMINALID=self._terminal_id).xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def payment_link_send(self,  merchantref, email_body=None, silence=False):
        self._session.with_method('post').with_url(self.url).with_data(
            send_payment_link_request(merchantref).with_field(TERMINALID=self._terminal_id).with_field(email_body)
                .xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def payment_link_create(self, merchantref=None, amount=None, currency: Currency = Currency.USD, silence=False):
        self._session.with_method('post').with_url(self.url).with_data(
            create_payment_link_request(merchantref, amount, currency).with_field(TERMINALID=self._terminal_id).xml())
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response


class RestSource(BaseSource):
    """
    types http://wn:8080/merchant/terminal/application.wadl
    resources http://wn:8080/merchant/terminal/application.wadl/xsd0.xsd
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._path += '/terminal'
        self.url = self._session.url + self._path
        self.content_type = self._session.headers.get('Content-Type')

    @session_logging()
    def sale(self, request=None, currency=Currency.USD, silence=False):
        r = request if request is not None else rest_sale()
        r.account.terminalId = self._terminal_id
        r.amount.currency = currency.name
        req = self.__serialize(r)
        self._session.with_method('post').with_url(self.url + '/payment/sale').with_data(req)
        response = self._session.request.content
        # avoid emvTagReceiptFieldsVO parser error
        response = etree.tostring(etree.fromstring(response, etree.XMLParser(recover=True)))
        response = restParseLiteral(inFileName=BytesIO(response), silence=True)
        return response

    @session_logging()
    def reversal(self, request: reversal, silence=False):
        request.account.terminalId = self._terminal_id
        self._session.with_method('post').with_url(self.url + '/payment/reversal').with_data(self.__serialize(request))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def refund_referenced(self, uniqueref, amount, currency: Currency = Currency.USD, payment_type=None,
                          terminal_type=terminalType.CHP, silence=False):
        request = rest_referenced_refund(uniqueref=uniqueref, amount=amount)
        request.amount.currency = currency.name
        request.account.terminalId = self._terminal_id
        request.account.paymentType = payment_type
        request.account.terminalType = terminal_type
        self._session.with_method('post').with_url(self.url + '/payment/refund').with_data(self.__serialize(request))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def refund_unreferenced(self, amount, currency: Currency = Currency.USD, payment_type=None, silence=False):
        request = rest_unreferenced_card_refund(amount=amount, currency=currency)
        request.amount.currency = currency.name
        request.account.terminalId = self._terminal_id
        request.account.paymentType = payment_type
        self._session.with_method('post').with_url(self.url + '/payment/refund').with_data(self.__serialize(request))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def refund(self, request, currency: Currency = Currency.USD, silence=False):
        request.amount.currency = currency.name
        request.account.terminalId = self._terminal_id
        self._session.with_method('post').with_url(self.url + '/payment/refund').with_data(self.__serialize(request))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def transaction_update(self, request: transactionUpdate, silence=False):
        request.account.terminalId = self._terminal_id
        self._session.with_method('post').with_url(self.url + '/payment/updateTransaction').with_data(self.__serialize(request))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def tip_adjustment(self, uniqueref, tip_type: tipType, amount=None, percentage=None,
                       currency: Currency = Currency.USD, silence=False):
        ta = transactionUpdate(
            uniqueRef=uniqueref,
            dateTime=datetime.now().replace(microsecond=0),
            deviceType='WALKER',
            account=account(deviceId='WALKER', operator=fake.name(), terminalType=terminalType.CHP, terminalId=self._terminal_id),
            tipAdjustment=tipAdjustment(
                amount_member=amount, currency=currency.name, percentage=percentage, tipType=tip_type
            )
        )

        self._session.with_method('post').with_url(self.url + '/payment/updateTransaction').with_data(self.__serialize(ta))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def balance_inquiry(self, request, silence=False):
        request.account.terminalId = self._terminal_id
        self._session.with_method('post').with_url(self.url + '/payment/balanceInquiry').with_data(self.__serialize(request))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def temporary_key(self, silence=True):
        self._session.with_method('get').with_url(self.url + '/security/temporaryKey/' + self._terminal_id)
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def authentication_token(self, account: account, temporary_key, silence=True):
        auth_token_request = authTokenRequest(
            userName='user',
            password='1',
            dateTime=today(format='%Y-%m-%dT%H:%M:%S'),
            account=account,
            apiKey=temporary_key,
            gatewayId='6',
            merchantId='21'
        )
        self._session.with_method('post').with_url(self.url + '/security/authenticationToken')\
            .with_data(self.__serialize(auth_token_request))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def authentication_request(self, terminal_id, terminal_type, temporary_key, silence=False):
        auth_request = authenticationRequest(
            dateTime=today(format='%Y-%m-%dT%H:%M:%S'),
            account=account(
                terminalId=terminal_id,
                terminalType=terminal_type
            ),
            apiKey=temporary_key,
        )
        self._session.with_method('post').with_url(self.url + '/security/authenticationRequest')\
            .with_data(self.__serialize(auth_request))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def get_terminal_configuration(self, terminal_configuration_request, silence=True):
        self._session.with_method('post').with_url(self.url + '/settings/get').with_data(self.__serialize(terminal_configuration_request))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def update_terminal_settings(self, terminal_update, silence=True):
        self._session.with_method('post').with_url(self.url + '/settings/update')\
            .with_data(self.__serialize(terminal_update))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def reporting_list(self, terminal_number=None, open='true', closed='true', date=today(format='%Y-%m-%dT%H:%M:%S'),
                       order_id='', silence=True):
        if not terminal_number:
            terminal_number = self._terminal_id
        count = 25
        page = 1
        hash_string = [str(count), closed, open]
        if order_id:
            hash_string.append(order_id)
        hash_string.append(str(page))
        hash_string.append(date)
        hash_string.append('someSecretPhrase')
        m = hashlib.sha256()
        m.update(str.encode(':' + ':'.join(hash_string)))
        digest = m.hexdigest()
        query_string = f'{terminal_number}?orderId={order_id}&count={count}&page={page}&open={open}&closed={closed}&' \
                       f'digest={digest}&messageDigestAlgorithm=SHA_256&dateTime={date}'
        self._session.with_method('get').with_url(self.url + '/reporting/list/%s' % query_string)
        # json serialisation issue, so it's better to use xml to get full list of txns
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def transaction_report(self, terminal_number, api_key, settlement_date, criterion_type, criterion_value, silence=True):
        # EBT txn only, use terminal 22003 to test
        # settlement_date format %d-%m-%Y
        m = hashlib.sha512()
        m.update(str.encode(f':{api_key}:{criterion_type}:{criterion_value}:{settlement_date}:'
                            f'{terminal_number}:someSecretPhrase'))
        digest = m.hexdigest()
        query_string = f'{terminal_number}?apiKey={api_key}&criterionType={criterion_type}&' \
                       f'criterionValue={criterion_value}&settlementDate={settlement_date}&' \
                       f'digest={digest}&messageDigestAlgorithm=SHA_512'
        self._session.with_method('get').with_url(self.url + '/reporting/transactionReport/%s' % query_string)
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def get_securecard(self, merchant_ref, silence=False):
        # http://go:8080/merchant/terminal/securecard/REST_SC_3832188?terminalId=21001&digest=
        # &messageDigestAlgorithm=SHA_256&dateTime=2017-06-22T13:38:55
        date_time = today(format='%Y-%m-%dT%H:%M:%S')
        m = hashlib.sha512()
        m.update(str.encode(f':{merchant_ref}:{self._terminal_id}:{date_time}:someSecretPhrase'))
        digest = m.hexdigest()
        query_string = f'{merchant_ref}?terminalId={self._terminal_id}&digest={digest}&messageDigestAlgorithm=SHA_512&' \
                       f'dateTime={date_time}'

        self._session.with_method('get').with_url(self.url + '/securecard/%s' % query_string)
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=False)

    @session_logging()
    def create_securecard(self, request: secureCard, silence=False):
        r = request
        r.terminalId = self._terminal_id
        self._session.with_method('post').with_url(self.url + '/securecard/register').with_data(self.__serialize(request))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def update_securecard(self, request: secureCard, silence=False):
        r = request
        r.terminalId = self._terminal_id
        self._session.with_method('post').with_url(self.url + '/securecard/update').with_data(self.__serialize(request))
        return restParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    def __serialize(self, request, is_hashable=True):
        r = request.xml(is_hashable=is_hashable)
        if self.content_type and 'json' in self.content_type:
            r = request.json(is_hashable=is_hashable)
        return r


class PayLinkSource(BaseSource):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._path += '/xmlpaylink'
        self.url = self._session.url + self._path
        self._session.with_headers({'Content-Type': 'application/xml'})

    @session_logging()
    def create_paylink(self, request: CREATE, silence=False):
        self._session.with_method('post').with_url(self.url).with_data(request.with_field(TERMINALID=self._terminal_id).xml())
        response = paylinkParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def send(self, merchantref, silence=False):
        self._session.with_method('post').with_url(self.url).with_data(
            send_paylink_request(merchantref).with_field(TERMINALID=self._terminal_id).xml()
        )
        response = parseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

        # self._session.with_method('post').with_url(self.url).with_data(send_paylink_request(merchantref)
        #                                                                .with_field(TERMINALID=self._terminal_id).xml())
        # response = paylinkParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response


class BoardingSource(BaseSource):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._path += '/boarding/'
        self.url = self._session.url + self._path
        self.content_type = self._session.headers.get('Content-Type')

    def get_merchant_template(self, template_id):
        url = self.url + 'merchant/merchantTemplate/%s' % str(template_id)

    @session_logging()
    def get_merchant(self, merchant_id, silence=False):
        self._session.with_method('get').with_url(self.url + f'merchant/{merchant_id}')
        response = boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def get_merchant_portfolio(self, merchant_portfolio_id, silence=False):
        self._session.with_method('get').with_url(self.url + f'merchantPortfolio/{merchant_portfolio_id}')
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def update_merchant_general_setup(self, merchant_id, share_sc: bool = False,
                                      share_sc_deactivated_terminal: bool = False, silence=False):
        request = self.get_merchant(merchant_id, silence=silence)
        request.merchantGeneralSetup = merchantGeneralSetup(
            shareAllSecureCards=share_sc,
            shareCardsFromDeactivatedTerminals=share_sc_deactivated_terminal
        )
        self._session.with_method('put').with_url(self.url + 'merchant').with_data(self.__serialize(request, False))
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def update_merchant(self, merchant_id, **kwargs):
        request = self.get_merchant(merchant_id, silence=kwargs.get('silence'))
        request.with_field(**kwargs)
        self._session.with_method('put').with_url(self.url + 'merchant').with_data(self.__serialize(request, False))
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def update_merchant_portfolio(self, merchant_portfolio_id, **kwargs):
        request = self.get_merchant_portfolio(merchant_portfolio_id, silence=kwargs.get('silence'))
        request.with_field(**kwargs)

        # Stupid serialization problem with the root tag
        xml_request = self.__serialize(request, False)
        xml_request = xml_request.replace('Merchantportfolio', 'MerchantPortfolio')

        self._session.with_method('put').with_url(self.url + 'merchantPortfolio').with_data(xml_request)
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def create_terminal(self, request: terminal, silence=False):
        self._session.with_method('post').with_url(self.url + 'terminal').with_data(self.__serialize(request, False))

        if 'json' in self.content_type:
            response = json.dumps(json.loads(self._session.request.content.decode('utf-8')), indent=4, sort_keys=True)
        else:
            response = boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def update_terminal_cards(self, terminal_number, cardtype=None, silence=False):
        request = self.get_terminal(terminal_number)
        request.cards = cardsType(CARDTYPES) if cardtype is None else cardsType(cardtype)
        self._session.with_method('put').with_url(self.url + 'terminal').with_data(self.__serialize(request, False))
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def update_terminal(self, request: terminal, silence=True):
        self._session.with_method('put').with_url(self.url + 'terminal').with_data(self.__serialize(request, False))
        response = boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def update_terminal_surcharge(self, terminal_number, allow_surcharge=False, surcharge_percent=0, silence=True):
        request = self.get_terminal(terminal_number)
        request.features.allowSurcharge = allow_surcharge
        request.features.surchargePercent = surcharge_percent
        self._session.with_method('put').with_url(self.url + 'terminal').with_data(self.__serialize(request, False))
        response = boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

    @session_logging()
    def update_terminal_max_mind(self, terminal_number, use_max_mind: bool = False, reject_errors: bool = False,
                                 risk_threshold: float = None, silence = False):
        request = self.get_terminal(terminal_number)
        request.securityFraud.maxMindActive = use_max_mind
        request.securityFraud.maxMindRejectOnError = reject_errors
        request.securityFraud.maxMindRiskScoreThreshold = risk_threshold

        self._session.with_method('put').with_url(self.url + 'terminal').with_data(self.__serialize(request, False))
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def update_terminal_integration(self, terminal_number, property_name, property_value, silence=False):
        request = self.get_terminal(terminal_number)

        setattr(request.integration, property_name, property_value)
        self._session.with_method('put').with_url(self.url + 'terminal').with_data(self.__serialize(request, False))
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def update_terminal_bank_settings(self, terminal_number, property_name, property_value, silence=False):
        request = self.get_terminal(terminal_number)

        setattr(request.bankSettings, property_name, property_value)
        self._session.with_method('put').with_url(self.url + 'terminal').with_data(self.__serialize(request, False))
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def update_terminal_batch_time(self, terminal_number, batch_time, silence=False):
        request = self.get_terminal(terminal_number)
        request.bankSettings.batchTime = batch_time

        self._session.with_method('put').with_url(self.url + 'terminal').with_data(self.__serialize(request, False))
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    def update_terminal_level_data(self, level_data: levelDataEnum, api_address_mode: apiAddressModeEnum):
        """Action to mange a level data of the processing terminals:
              <xs:element name="txnDataLevel" type="levelDataEnum" minOccurs="0"/>
              <xs:element name="apiShippingAddressMode" type="apiAddressModeEnum" minOccurs="0"/>
              <xs:element name="enableTemplateAutofill" type="xs:boolean" minOccurs="0"/>
              <xs:element name="merchantTaxId" type="xs:string" minOccurs="0"/>
              <xs:element name="merchantTypeCode" type="xs:string" minOccurs="0"/>
        """

        request = self.get_terminal(self._terminal_id)
        request.features.txnDataLevel = level_data
        request.features.apiShippingAddressMode = api_address_mode
        self._session.with_method('put').with_url(self.url + 'terminal').with_data(self.__serialize(request, False))

        logger.warning('\nRequest:\n%s' % self._session)
        response = boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        logger.warning('\nResponse:\n%s' % response.xml(is_hashable=False))
        return response

    @session_logging()
    def update_terminal_currency(self, terminal_id: int, currency: Currency, silence=False):
        request = self.get_terminal(terminal_id)
        request.bankSettings.currency = currency.name
        self._session.with_method('put').with_url(self.url + 'terminal').with_data(self.__serialize(request, False))
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def update_terminal_avs(self, terminal_number: int, enable_avs=True,
                            avs_sent_action: avsActionEnum=avsActionEnum.HIDE, silence=False):
        request = self.get_terminal(terminal_number)
        request.securityFraud.enableAvs = enable_avs
        request.securityFraud.avsSentAction = avs_sent_action
        self._session.with_method('put').with_url(self.url + 'terminal').with_data(self.__serialize(request, False))

        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def update_terminal_validation(self, terminal_number: int, enable_validation: bool,
                                   response_code='OK', receipt_url='http://simulator.wntps.com:8181/receipt', silence=False):
        validation_url = f'http://simulator.wntps.com:8282/vagrant/?timeout1=100&timeout2=100&response-code={response_code}'
        request = self.get_terminal(terminal_number)
        request.integration.enableBackgroundValidation = enable_validation
        if enable_validation:
            request.integration.enableBackgroundValidation = enable_validation
        request.integration.backgroundValidationUrl = validation_url
        request.integration.receiptPageUrl = receipt_url
        request.integration.receiptMpiUrl = receipt_url
        request.integration.receiptSecureCardUrl = receipt_url
        request.integration.receiptSubscriptionUrl = receipt_url
        self._session.with_method('put').with_url(self.url + 'terminal').with_data(self.__serialize(request, False))
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    def get_terminal(self, terminal_number: int):
        self._session.with_method('get').with_url(self.url + 'terminal/%s' % terminal_number)
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def delete_terminal(self, terminal_number: int, silence=False):
        self._session.with_method('delete').with_url(self.url + 'terminal/%s' % terminal_number)
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def activate_terminal(self, terminal_number: int, silence=False):
        self._session.with_method('get').with_url(self.url + 'terminal/activateTerminal/%s' % terminal_number)
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def list_terminal(self, merchant_id: int, silence=False):
        self._session.with_method('get').with_url(self.url + 'terminal/listTerminal/%s' % merchant_id)
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def get_terminal_template(self, temaplate_name: str, silence=False):
        self._session.with_method('get').with_url(self.url + 'terminal/terminalTemplate/%s' % temaplate_name)
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def create_merchant(self, request: merchant, silence=False):
        self._session.with_method('post').with_url(self.url + 'merchant').with_data(self.__serialize(request, False))
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def create_user(self, request: user, silence=False):
        self._session.with_method('post').with_url(self.url + 'user').with_data(self.__serialize(request, False))
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def update_user(self, request: user, silence=False):
        self._session.with_method('put').with_url(self.url + 'user').with_data(self.__serialize(request, False))
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def get_user(self, user_id: str, silence=False):
        self._session.with_method('get').with_url(self.url + 'user/%s' % user_id)
        return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    @session_logging()
    def list_user(self, merchant_id: str, silence=False):
        self._session.with_method('get').with_url(self.url + 'user/listUser/%s' % merchant_id)

        logger.warning('\nRequest:\n%s' % self._session)
        if 'json' in self.content_type:
            response = json.dumps(json.loads(self._session.request.content.decode('utf-8')), indent=4, sort_keys=True)
        else:
            response = boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)
        return response

        # self._session.with_method('get').with_url(self.url + 'user/listUser/%s' % merchant_id)
        # return boardingParseLiteral(inFileName=BytesIO(self._session.request.content), silence=True)

    def __serialize(self, request, is_hashable=True):
        r = request.xml(is_hashable=is_hashable)
        if self.content_type and 'json' in self.content_type:
            r = request.json(is_hashable=is_hashable)
        return r


class HttpSource(BaseSource):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.url = self._session.url + self._path

    def test_settle(self, params: dict):
        request = self._session.with_method('post').with_url(self.url + '/test-settle/').with_data(params) \
            .with_headers({'Content-Type': 'application/x-www-form-urlencoded'})
        logger.warning('\nSession:\n%s' % self._session)
        response = request.request
        logger.warning('\nResponse:\n%s' % response)
        return response


class DatabaseSource(object):
    def __init__(self, **kwargs):
        self.txn_helper = TransactionsHelper(kwargs.get('terminal_number'))
        self.sc_helper = SecureCardHelper(terminal_number=kwargs.get('terminal_number'))
        self.utl_helper = UtilityHelper()

    def get_transaction(self, **kwargs):
        return self.txn_helper.get_transaction(**kwargs)

    def get_transaction_cof_details(self, **kwargs):
        txn = self.txn_helper.get_transaction(**kwargs)
        txn_cof_details = self.txn_helper.get_transaction_cof_details(transaction_id=txn.id) if txn else None
        logger.warning('Transaction CoF details: %s' % txn_cof_details)
        return txn_cof_details

    def get_transaction_surcharge(self, **kwargs):
        txn = self.txn_helper.get_transaction(**kwargs)
        txn_surcharge = self.txn_helper.get_transaction_surcharge(transaction_id=txn.id) if txn else None
        logger.warning('Transaction Surcharge: %s' % txn_surcharge)
        return txn_surcharge

    def get_transaction_tip(self, **kwargs):
        txn = self.txn_helper.get_transaction(**kwargs)
        txn_tip = self.txn_helper.get_transaction_tip(transaction_id=txn.id) if txn else None
        logger.warning('Transaction Tip: %s' % txn_tip)
        return txn_tip

    def get_fdrc_transaction(self, **kwargs):
        txn = self.txn_helper.get_transaction(**kwargs)
        fdrc_txn = self.txn_helper.get_fdrc_transaction(tx_id=txn.id) if txn else None
        logger.warning('Fdrc transaction: %s' % fdrc_txn)
        return fdrc_txn

    def get_secure_card(self, merchantref: str):
        return self.sc_helper.get_secure_card(merchantref)

    def get_secure_card_additional_settings(self, merchantref: str):
        return self.sc_helper.get_secure_card_additional_settings(merchantref)

    def get_api_key(self, key_alias: str):
        return self.utl_helper.get_api_key(key_alias).authentication_key
