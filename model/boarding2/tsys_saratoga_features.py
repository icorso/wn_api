# coding: utf-8
from model.serializable import SwaggerSerializable


class TsysSaratogaFeatures(SwaggerSerializable):
    swagger_types = {
        'allow_partial_captures': 'bool',
        'allow_acquiring': 'bool',
        'allow_offline_sales': 'bool',
        'allow_dashboard': 'bool',
        'allow_bulk_payments': 'bool',
        'allow_schedule_reports': 'bool',
        'allow_virtual_terminal_auto_order_id': 'bool',
        'enable_decryptx': 'bool',
        'enable_google_pay': 'bool',
        'enable_apple_pay': 'bool',
        'apple_store_name': 'str',
        'pay_link': 'PayLink',
        'shopify': 'Shopify',
        'surcharge': 'Surcharge',
        'secure_credentials': 'SecureCredentials',
        'amex_opt_blue': 'AmexOptBlueParticipation',
        'enhanced_data': 'TsysSaratogaEnhancedData',
        'payment_facilitator': 'PaymentFacilitator',
        'dynamic_descriptor': 'TsysSaratogaDynamicDescriptor'
    }

    attribute_map = {
        'allow_partial_captures': 'allowPartialCaptures',
        'allow_acquiring': 'allowAcquiring',
        'allow_offline_sales': 'allowOfflineSales',
        'allow_dashboard': 'allowDashboard',
        'allow_bulk_payments': 'allowBulkPayments',
        'allow_schedule_reports': 'allowScheduleReports',
        'allow_virtual_terminal_auto_order_id': 'allowVirtualTerminalAutoOrderId',
        'enable_decryptx': 'enableDecryptx',
        'enable_google_pay': 'enableGooglePay',
        'enable_apple_pay': 'enableApplePay',
        'apple_store_name': 'appleStoreName',
        'pay_link': 'payLink',
        'shopify': 'shopify',
        'surcharge': 'surcharge',
        'secure_credentials': 'secureCredentials',
        'amex_opt_blue': 'amexOptBlue',
        'enhanced_data': 'enhancedData',
        'payment_facilitator': 'paymentFacilitator',
        'dynamic_descriptor': 'dynamicDescriptor'
    }

    def __init__(self, allow_partial_captures=False, allow_acquiring=False, allow_offline_sales=False, allow_dashboard=False, allow_bulk_payments=False, allow_schedule_reports=False, allow_virtual_terminal_auto_order_id=False, enable_decryptx=False, enable_google_pay=False, enable_apple_pay=False, apple_store_name=None, pay_link=None, shopify=None, surcharge=None, secure_credentials=None, amex_opt_blue=None, enhanced_data=None, payment_facilitator=None, dynamic_descriptor=None):  # noqa: E501
        self._allow_partial_captures = None
        self._allow_acquiring = None
        self._allow_offline_sales = None
        self._allow_dashboard = None
        self._allow_bulk_payments = None
        self._allow_schedule_reports = None
        self._allow_virtual_terminal_auto_order_id = None
        self._enable_decryptx = None
        self._enable_google_pay = None
        self._enable_apple_pay = None
        self._apple_store_name = None
        self._pay_link = None
        self._shopify = None
        self._surcharge = None
        self._secure_credentials = None
        self._amex_opt_blue = None
        self._enhanced_data = None
        self._payment_facilitator = None
        self._dynamic_descriptor = None
        self.discriminator = None
        if allow_partial_captures is not None:
            self.allow_partial_captures = allow_partial_captures
        if allow_acquiring is not None:
            self.allow_acquiring = allow_acquiring
        if allow_offline_sales is not None:
            self.allow_offline_sales = allow_offline_sales
        if allow_dashboard is not None:
            self.allow_dashboard = allow_dashboard
        if allow_bulk_payments is not None:
            self.allow_bulk_payments = allow_bulk_payments
        if allow_schedule_reports is not None:
            self.allow_schedule_reports = allow_schedule_reports
        if allow_virtual_terminal_auto_order_id is not None:
            self.allow_virtual_terminal_auto_order_id = allow_virtual_terminal_auto_order_id
        if enable_decryptx is not None:
            self.enable_decryptx = enable_decryptx
        if enable_google_pay is not None:
            self.enable_google_pay = enable_google_pay
        if enable_apple_pay is not None:
            self.enable_apple_pay = enable_apple_pay
        if apple_store_name is not None:
            self.apple_store_name = apple_store_name
        if pay_link is not None:
            self.pay_link = pay_link
        if shopify is not None:
            self.shopify = shopify
        if surcharge is not None:
            self.surcharge = surcharge
        if secure_credentials is not None:
            self.secure_credentials = secure_credentials
        if amex_opt_blue is not None:
            self.amex_opt_blue = amex_opt_blue
        if enhanced_data is not None:
            self.enhanced_data = enhanced_data
        if payment_facilitator is not None:
            self.payment_facilitator = payment_facilitator
        if dynamic_descriptor is not None:
            self.dynamic_descriptor = dynamic_descriptor

    @property
    def allow_partial_captures(self):
        return self._allow_partial_captures

    @allow_partial_captures.setter
    def allow_partial_captures(self, allow_partial_captures):
        self._allow_partial_captures = allow_partial_captures

    @property
    def allow_acquiring(self):
        return self._allow_acquiring

    @allow_acquiring.setter
    def allow_acquiring(self, allow_acquiring):
        self._allow_acquiring = allow_acquiring

    @property
    def allow_offline_sales(self):
        return self._allow_offline_sales

    @allow_offline_sales.setter
    def allow_offline_sales(self, allow_offline_sales):
        self._allow_offline_sales = allow_offline_sales

    @property
    def allow_dashboard(self):
        return self._allow_dashboard

    @allow_dashboard.setter
    def allow_dashboard(self, allow_dashboard):
        self._allow_dashboard = allow_dashboard

    @property
    def allow_bulk_payments(self):
        return self._allow_bulk_payments

    @allow_bulk_payments.setter
    def allow_bulk_payments(self, allow_bulk_payments):
        self._allow_bulk_payments = allow_bulk_payments

    @property
    def allow_schedule_reports(self):
        return self._allow_schedule_reports

    @allow_schedule_reports.setter
    def allow_schedule_reports(self, allow_schedule_reports):
        self._allow_schedule_reports = allow_schedule_reports

    @property
    def allow_virtual_terminal_auto_order_id(self):
        return self._allow_virtual_terminal_auto_order_id

    @allow_virtual_terminal_auto_order_id.setter
    def allow_virtual_terminal_auto_order_id(self, allow_virtual_terminal_auto_order_id):
        self._allow_virtual_terminal_auto_order_id = allow_virtual_terminal_auto_order_id

    @property
    def enable_decryptx(self):
        return self._enable_decryptx

    @enable_decryptx.setter
    def enable_decryptx(self, enable_decryptx):
        self._enable_decryptx = enable_decryptx

    @property
    def enable_google_pay(self):
        return self._enable_google_pay

    @enable_google_pay.setter
    def enable_google_pay(self, enable_google_pay):
        self._enable_google_pay = enable_google_pay

    @property
    def enable_apple_pay(self):
        return self._enable_apple_pay

    @enable_apple_pay.setter
    def enable_apple_pay(self, enable_apple_pay):
        self._enable_apple_pay = enable_apple_pay

    @property
    def apple_store_name(self):
        return self._apple_store_name

    @apple_store_name.setter
    def apple_store_name(self, apple_store_name):
        self._apple_store_name = apple_store_name

    @property
    def pay_link(self):
        return self._pay_link

    @pay_link.setter
    def pay_link(self, pay_link):
        self._pay_link = pay_link

    @property
    def shopify(self):
        return self._shopify

    @shopify.setter
    def shopify(self, shopify):
        self._shopify = shopify

    @property
    def surcharge(self):
        return self._surcharge

    @surcharge.setter
    def surcharge(self, surcharge):
        self._surcharge = surcharge

    @property
    def secure_credentials(self):
        return self._secure_credentials

    @secure_credentials.setter
    def secure_credentials(self, secure_credentials):
        self._secure_credentials = secure_credentials

    @property
    def amex_opt_blue(self):
        return self._amex_opt_blue

    @amex_opt_blue.setter
    def amex_opt_blue(self, amex_opt_blue):
        self._amex_opt_blue = amex_opt_blue

    @property
    def enhanced_data(self):
        return self._enhanced_data

    @enhanced_data.setter
    def enhanced_data(self, enhanced_data):
        self._enhanced_data = enhanced_data

    @property
    def payment_facilitator(self):
        return self._payment_facilitator

    @payment_facilitator.setter
    def payment_facilitator(self, payment_facilitator):
        self._payment_facilitator = payment_facilitator

    @property
    def dynamic_descriptor(self):
        return self._dynamic_descriptor

    @dynamic_descriptor.setter
    def dynamic_descriptor(self, dynamic_descriptor):
        self._dynamic_descriptor = dynamic_descriptor

