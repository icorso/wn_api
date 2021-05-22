# coding: utf-8
from model.serializable import SwaggerSerializable


class TerminalFeatures(SwaggerSerializable):
    swagger_types = {
        'allow_dashboard': 'bool',
        'allow_bulk_payments': 'bool',
        'allow_schedule_reports': 'bool',
        'enable_decryptx': 'bool'
    }

    attribute_map = {
        'allow_dashboard': 'allowDashboard',
        'allow_bulk_payments': 'allowBulkPayments',
        'allow_schedule_reports': 'allowScheduleReports',
        'enable_decryptx': 'enableDecryptx'
    }

    def __init__(self, allow_dashboard=False, allow_bulk_payments=False, allow_schedule_reports=False, enable_decryptx=False):  # noqa: E501
        self._allow_dashboard = None
        self._allow_bulk_payments = None
        self._allow_schedule_reports = None
        self._enable_decryptx = None
        self.discriminator = None
        if allow_dashboard is not None:
            self.allow_dashboard = allow_dashboard
        if allow_bulk_payments is not None:
            self.allow_bulk_payments = allow_bulk_payments
        if allow_schedule_reports is not None:
            self.allow_schedule_reports = allow_schedule_reports
        if enable_decryptx is not None:
            self.enable_decryptx = enable_decryptx

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
    def enable_decryptx(self):
        return self._enable_decryptx

    @enable_decryptx.setter
    def enable_decryptx(self, enable_decryptx):
        self._enable_decryptx = enable_decryptx

