# coding: utf-8

from __future__ import absolute_import

# import models into model package
from model.boarding2.terminal import Terminal
from model.boarding2.access_token import AccessToken
from model.boarding2.account_updater import AccountUpdater
from model.boarding2.address_verification_system import AddressVerificationSystem
from model.boarding2.amex_opt_blue_participation import AmexOptBlueParticipation
from model.boarding2.authorize_net_bank_settings import AuthorizeNetBankSettings
from model.boarding2.authorize_net_features import AuthorizeNetFeatures
from model.boarding2.authorize_net_fraud_detection import AuthorizeNetFraudDetection
from model.boarding2.authorize_net_integration_settings import AuthorizeNetIntegrationSettings
from model.boarding2.authorize_net_terminal import AuthorizeNetTerminal
from model.boarding2.card_level_limit import CardLevelLimit
from model.boarding2.card_security_code_verification import CardSecurityCodeVerification
from model.boarding2.card_volume_limit import CardVolumeLimit
from model.boarding2.credorax_bank_settings import CredoraxBankSettings
from model.boarding2.credorax_dynamic_descriptor import CredoraxDynamicDescriptor
from model.boarding2.credorax_features import CredoraxFeatures
from model.boarding2.credorax_fraud_detection import CredoraxFraudDetection
from model.boarding2.credorax_integration_settings import CredoraxIntegrationSettings
from model.boarding2.credorax_terminal import CredoraxTerminal
from model.boarding2.ct_payments_bank_settings import CtPaymentsBankSettings
from model.boarding2.ct_payments_features import CtPaymentsFeatures
from model.boarding2.ct_payments_fraud_detection import CtPaymentsFraudDetection
from model.boarding2.ct_payments_integration_settings import CtPaymentsIntegrationSettings
from model.boarding2.ct_payments_location_details import CtPaymentsLocationDetails
from model.boarding2.ct_payments_terminal import CtPaymentsTerminal
from model.boarding2.cyber_source_bank_settings import CyberSourceBankSettings
from model.boarding2.cyber_source_features import CyberSourceFeatures
from model.boarding2.cyber_source_fraud_detection import CyberSourceFraudDetection
from model.boarding2.cyber_source_integration_settings import CyberSourceIntegrationSettings
from model.boarding2.cyber_source_soap_bank_settings import CyberSourceSoapBankSettings
from model.boarding2.cyber_source_soap_features import CyberSourceSoapFeatures
from model.boarding2.cyber_source_soap_terminal import CyberSourceSoapTerminal
from model.boarding2.cyber_source_terminal import CyberSourceTerminal
from model.boarding2.draft256_billing import Draft256Billing
from model.boarding2.elavon_bank_settings import ElavonBankSettings
from model.boarding2.elavon_features import ElavonFeatures
from model.boarding2.elavon_fraud_detection import ElavonFraudDetection
from model.boarding2.elavon_integration_settings import ElavonIntegrationSettings
from model.boarding2.elavon_terminal import ElavonTerminal
from model.boarding2.error import Error
from model.boarding2.error_detail import ErrorDetail
from model.boarding2.error_source import ErrorSource
from model.boarding2.fdrc_bank_settings import FdrcBankSettings
from model.boarding2.fdrc_enhanced_data import FdrcEnhancedData
from model.boarding2.fdrc_features import FdrcFeatures
from model.boarding2.fdrc_fraud_detection import FdrcFraudDetection
from model.boarding2.fdrc_integration_settings import FdrcIntegrationSettings
from model.boarding2.fdrc_terminal import FdrcTerminal
from model.boarding2.fi_serv_bank_settings import FiServBankSettings
from model.boarding2.fi_serv_fraud_detection import FiServFraudDetection
from model.boarding2.fi_serv_integration_settings import FiServIntegrationSettings
from model.boarding2.fi_serv_location_details import FiServLocationDetails
from model.boarding2.fi_serv_terminal import FiServTerminal
from model.boarding2.hypermedia_link import HypermediaLink
from model.boarding2.integra_pay_bank_settings import IntegraPayBankSettings
from model.boarding2.integra_pay_features import IntegraPayFeatures
from model.boarding2.integra_pay_fraud_detection import IntegraPayFraudDetection
from model.boarding2.integra_pay_integration_settings import IntegraPayIntegrationSettings
from model.boarding2.integra_pay_terminal import IntegraPayTerminal
from model.boarding2.max_mind import MaxMind
from model.boarding2.merchant import Merchant
from model.boarding2.merchant_compact import MerchantCompact
from model.boarding2.merchant_custom_settings import MerchantCustomSettings
from model.boarding2.merchant_general_setup import MerchantGeneralSetup
from model.boarding2.merchant_level_limit import MerchantLevelLimit
from model.boarding2.merchant_paginated_result import MerchantPaginatedResult
from model.boarding2.merchant_portfolio import MerchantPortfolio
from model.boarding2.merchant_portfolio_compact import MerchantPortfolioCompact
from model.boarding2.merchant_portfolio_paginated_result import MerchantPortfolioPaginatedResult
from model.boarding2.merchant_pricing import MerchantPricing
from model.boarding2.nmi_bank_settings import NmiBankSettings
from model.boarding2.nmi_features import NmiFeatures
from model.boarding2.nmi_fraud_detection import NmiFraudDetection
from model.boarding2.nmi_integration_settings import NmiIntegrationSettings
from model.boarding2.nmi_terminal import NmiTerminal
from model.boarding2.partner_compact import PartnerCompact
from model.boarding2.partner_paginated_result import PartnerPaginatedResult
from model.boarding2.partner_portfolio import PartnerPortfolio
from model.boarding2.pay_link import PayLink
from model.boarding2.payment_facilitator import PaymentFacilitator
from model.boarding2.processing_rule import ProcessingRule
from model.boarding2.processing_rule_instruction import ProcessingRuleInstruction
from model.boarding2.processing_rule_predicate import ProcessingRulePredicate
from model.boarding2.secure_credentials import SecureCredentials
from model.boarding2.sentinel_defend import SentinelDefend
from model.boarding2.shopify import Shopify
from model.boarding2.surcharge import Surcharge
from model.boarding2.tender_type_predicate import TenderTypePredicate
from model.boarding2.terminal_ach_jack_henry_processing import TerminalAchJackHenryProcessing
from model.boarding2.terminal_ach_processing import TerminalAchProcessing
from model.boarding2.terminal_compact import TerminalCompact
from model.boarding2.terminal_features import TerminalFeatures
from model.boarding2.terminal_level_limit import TerminalLevelLimit
from model.boarding2.terminal_location_details import TerminalLocationDetails
from model.boarding2.terminal_paginated_result import TerminalPaginatedResult
from model.boarding2.terminal_receipt_notifications import TerminalReceiptNotifications
from model.boarding2.terminal_union_pay_processing import TerminalUnionPayProcessing
from model.boarding2.terminal_volume_limits import TerminalVolumeLimits
from model.boarding2.three_d_secure import ThreeDSecure
from model.boarding2.tsys_saratoga_bank_settings import TsysSaratogaBankSettings
from model.boarding2.tsys_saratoga_dynamic_descriptor import TsysSaratogaDynamicDescriptor
from model.boarding2.tsys_saratoga_enhanced_data import TsysSaratogaEnhancedData
from model.boarding2.tsys_saratoga_features import TsysSaratogaFeatures
from model.boarding2.tsys_saratoga_fraud_detection import TsysSaratogaFraudDetection
from model.boarding2.tsys_saratoga_integration_settings import TsysSaratogaIntegrationSettings
from model.boarding2.tsys_saratoga_location_details import TsysSaratogaLocationDetails
from model.boarding2.tsys_saratoga_terminal import TsysSaratogaTerminal
from model.boarding2.tsys_sierra_bank_settings import TsysSierraBankSettings
from model.boarding2.tsys_sierra_features import TsysSierraFeatures
from model.boarding2.tsys_sierra_fraud_detection import TsysSierraFraudDetection
from model.boarding2.tsys_sierra_integration_settings import TsysSierraIntegrationSettings
from model.boarding2.tsys_sierra_location_details import TsysSierraLocationDetails
from model.boarding2.tsys_sierra_terminal import TsysSierraTerminal
from model.boarding2.unassigned_bank_settings import UnassignedBankSettings
from model.boarding2.unassigned_features import UnassignedFeatures
from model.boarding2.unassigned_integration_settings import UnassignedIntegrationSettings
from model.boarding2.unassigned_terminal import UnassignedTerminal
from model.boarding2.user import User
from model.boarding2.user_compact import UserCompact
from model.boarding2.user_paginated_result import UserPaginatedResult
from model.boarding2.vacp_g2_g_bank_settings import VacpG2GBankSettings
from model.boarding2.vacp_g2_g_features import VacpG2GFeatures
from model.boarding2.vacp_g2_g_fraud_detection import VacpG2GFraudDetection
from model.boarding2.vacp_g2_g_integration_settings import VacpG2GIntegrationSettings
from model.boarding2.vacp_g2_g_terminal import VacpG2GTerminal
from model.boarding2.paynomix_bank_settings import PaynomixBankSettings
from model.boarding2.paynomix_features import PaynomixFeatures
from model.boarding2.paynomix_fraud_detection import PaynomixFraudDetection
from model.boarding2.paynomix_integration_settings import PaynomixIntegrationSettings
from model.boarding2.paynomix_terminal import PaynomixTerminal