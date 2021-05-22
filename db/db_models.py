from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime
from sqlalchemy import Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class AchjhTransaction(Base):
    __tablename__ = 'ach_jh_transaction'

    id = Column(Integer, primary_key=True)
    account_type = Column(Integer())
    sec_code = Column(Integer())
    check_number = Column(String)
    routing_number = Column(String)
    originated_as = Column(String)
    response_code = Column(Integer())
    response_message = Column(String)
    reinitiation = Column(Integer())
    event_last = Column(Integer())
    event_last_date = Column(DateTime)
    transaction_status_last = Column(Integer())
    settlement_status_last = Column(Integer())
    region = Column(String)
    city = Column(String)
    return_code = Column(String)
    gray_area = Column(Integer())
    terminal_id = Column(Integer())
    rrn = Column(String)
    reinitiation_first_date = Column(DateTime)
    reinitiation_second_date = Column(DateTime)
    dl_state = Column(String)
    dl_number = Column(String)

    def __repr__(self):
        return "<AchjhTransaction(id='%s', rrn='%s', routing_number='%s')>" % (self.id, self.rrn, self.routing_number)


class AchjhTransactionStateHistory(Base):
    __tablename__ = 'ach_jh_transaction_state_history'
    id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer())
    event_date_time = Column(DateTime)
    event_type = Column(Integer())
    transaction_status = Column(Integer())
    settlement_status = Column(Integer())

    def __repr__(self):
        return "<AchjhTransactionStateHistory(id='%s', transaction_id='%s')>" % (self.id, self.transaction_id)


class OpenTransaction(Base):
    __tablename__ = 'open_transaction'

    id = Column(Integer, primary_key=True)
    terminalid = Column(Integer())
    txndate = Column(DateTime)
    status = Column(Integer())
    currency = Column(Integer())
    amount = Column(Float)
    cardholderemail = Column(String)
    cardholdername = Column(String)
    cardtype = Column(Integer())
    orderid = Column(String)
    cardreadmethod = Column(Integer)
    description = Column(String)
    responsecode = Column(String)
    responsetext = Column(String)
    originaltransactionid = Column(String)
    approvalcode = Column(String)
    uniqueref = Column(String)
    rrn = Column(String)
    bank_id = Column(Integer())
    commercetype = Column(String(length=2))
    mobilenumber = Column(String(length=32))

    def __repr__(self):
        return "<OpenTransaction(id='%s', rrn='%s', uniqueref='%s')>" % (self.id, self.rrn, self.uniqueref)


class ClosedTransaction(Base):
    __tablename__ = 'closed_transaction'

    id = Column(Integer, primary_key=True)
    terminalid = Column(Integer())
    txndate = Column(DateTime)
    status = Column(Integer())
    amount = Column(Float)
    cardholdername = Column(String)
    orderid = Column(String)
    description = Column(String)
    responsecode = Column(String)
    responsetext = Column(String)
    originaltransactionid = Column(String)
    approvalcode = Column(String)
    uniqueref = Column(String)
    rrn = Column(String)
    cardreadmethod = Column(Integer)

    def __repr__(self):
        return "<ClosedTransaction(id='%s', rrn='%s', uniqueref='%s')>" % (self.id, self.rrn, self.uniqueref)


class AchIntegrapayTransactionStateHistory(Base):
    __tablename__ = 'ach_integrapay_transaction_state_history'

    id = Column(Integer, primary_key=True)
    original_transaction_id = Column(Integer())
    business_id = Column(String)
    business_name = Column(String)
    business_reference = Column(String)
    txn_original_time = Column(DateTime)
    transaction_id = Column(String)
    secondary_transaction_id = Column(String)
    reference = Column(String)
    description = Column(String)
    schedule_reference = Column(String)
    amount = Column(Float)
    amount_refunded = Column(Float)
    currency = Column(String)
    transaction_type = Column(String)
    type_description = Column(String)
    transaction_status = Column(String)
    status_description = Column(String)
    sub_status_code = Column(String)
    sub_status_code_description = Column(String)
    payment_method = Column(String)
    debit_date = Column(DateTime)
    event_date = Column(DateTime)
    payer_id = Column(String)
    payer_unique_reference = Column(String)
    payer_group_reference = Column(String)
    family_business_name = Column(String)
    given_name = Column(String)
    addressLine1 = Column(String)
    addressLine2 = Column(String)
    suburb = Column(String)
    state = Column(String)
    postCode = Column(String)
    country = Column(String)
    email = Column(String)
    phone = Column(String)
    mobile = Column(String)
    account_id = Column(String)
    account_branch = Column(String)
    account_number = Column(String)
    account_type = Column(String)
    account_name = Column(String)
    scheduled_payment_id = Column(String)
    audit_username = Column(String)

    def __repr__(self):
        return "<AchIntegrapayTransactionStateHistory(id='%s', original_transaction_id='%s',business_id='%s')>" \
               % (self.id, self.original_transaction_id, self.business_id)


class Currency(Base):
    __tablename__ = 'currency'

    id = Column(Integer, primary_key=True)
    number = Column(Integer())
    code = Column(String)
    supported = Column(Integer())
    minorunits = Column(Integer())


class ApiKey(Base):
    __tablename__ = 'api_key'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer())
    key_alias = Column(String)
    authentication_key = Column(String)


class TransactionCofDetails(Base):
    __tablename__ = 'transaction_cof_details'

    id = Column(Integer, primary_key=True)
    stored_credential_tx_type = Column(Integer())
    stored_credential_use = Column(Integer())
    original_brand_tx_identifier = Column(String(length=64))
    brand_tx_identifier = Column(String(length=64))

    def __repr__(self):
        return "<TransactionCofDetails(id='%s')>" % self.id


class TransactionSurcharge(Base):
    __tablename__ = 'transaction_surcharge'

    id = Column(Integer, primary_key=True)
    percentage = Column(Float(precision=5))
    amount = Column(Float(precision=3))
    currency_id = Column(Integer())

    def __repr__(self):
        return "<TransactionSurcharge(id='%s', percentage=%s, amount=%s)>" % (self.id, str(self.percentage),
                                                                              str(self.amount))


class TransactionTip(Base):
    __tablename__ = 'transaction_tip'

    id = Column(Integer, primary_key=True)
    type = Column(Integer)
    percentage = Column(Float(precision=4))
    amount = Column(Float(precision=3))
    currency_id = Column(Integer())
    adjustment = Column(Integer)

    def __repr__(self):
        return "<TransactionTip(id='%s', percentage=%s, amount=%s, currency_id=%s)>" \
               % (str(self.id), str(self.percentage), str(self.amount), str(self.currency_id))


class SecureCard(Base):
    __tablename__ = 'secure_card'

    id = Column(Integer, primary_key=True)
    terminalid = Column(Integer())
    cardtype = Column(Integer())
    status = Column(Integer())
    modificationdate = Column(DateTime)
    merchantref = Column(String(length=48))
    cardnumber = Column(String(length=128))
    cardholdername = Column(String(length=50))
    cardexpiry = Column(String(length=4))
    reference = Column(String(length=128))
    securityvalidationresult = Column(Integer())
    referencedby = Column(Integer, unique=True)
    email = Column(String(length=128))
    country_id = Column(Integer, unique=True)
    region = Column(String(length=128))
    address1 = Column(String(length=128))
    city = Column(String(length=128))
    postcode = Column(String(length=128))
    bill_to_first_name = Column(String(length=60))
    bill_to_last_name = Column(String(length=60))
    creation_date = Column(DateTime)
    updater_status = Column(Integer())
    updater_modification_date = Column(DateTime)
    additional_setting_id = Column(Integer())
    reference_hash = Column(String(length=64))

    def __repr__(self):
        return "<SecureCard(id='%s, terminal=%s, %s, %s')>" % (self.id, self.terminalid, self.merchantref,
                                                      self.cardnumber.split('|')[2] + '/' + self.cardexpiry)


class SecureCardAdditionalSetting(Base):
    __tablename__ = 'secure_card_additional_setting'

    id = Column(Integer, primary_key=True)
    address2 = Column(String(length=64))
    phone = Column(String(length=20))
    routing_number = Column(String(length=9))
    account_type = Column(Integer())
    dl_state = Column(String(length=2))
    dl_number = Column(String(length=30))
    card_entry_mode = Column(Integer())
    verification_txn_id = Column(String(length=64))
    stored_credential_use = Column(Integer())


class Terminal(Base):
    __tablename__ = 'terminal'

    id = Column(Integer, primary_key=True)
    terminal_number = Column(String(length=24))
    merchant_id = Column(Integer())


class FDRCTransaction(Base):
    __tablename__ = 'fdrc_transaction'

    id = Column(Integer, primary_key=True)
    tpp_id = Column(String(length=6))
    orig_term_cat_code = Column(String(length=2))
    pos_device_id = Column(Integer())

    def __repr__(self):
        return "<FDRCTransaction(id='%s, tpp_id=%s')>" % (self.id, self.tpp_id)


class DaoStatistic(Base):
    __tablename__ = 'dao_statistic'

    id = Column(Integer, primary_key=True)
    nodename = Column(String(length=128))
    date = Column(DateTime)
    eliminate = Column(Integer)
    notes = Column(String(length=2048))

    def __repr__(self):
        return "<DaoStatistic(id='%s, date=%s, notes=%s')>" % (self.id, self.date, self.notes)


class DaoStatisticDetails(Base):

    __tablename__ = 'dao_statistic_details'

    id = Column(Integer, primary_key=True)
    methodname = Column(String(length=512))
    executionscount = Column(Integer)
    minexecutiontime = Column(Integer)
    maxexecutiontime = Column(Integer)
    totalexecutiontime = Column(Integer)
    daostatisticid = Column(Integer)

    def __repr__(self):
        return "<DaoStatistic(id='%s, date=%s, notes=%s')>" % (self.id, self.date, self.notes)


class TsysSaratogaConversionRate(Base):

    __tablename__ = 'tsys_saratoga_conversion_rate'

    id = Column(Integer, primary_key=True)
    terminal_base_currency_code = Column(String(length=3))
    date = Column(DateTime)
    currency_code = Column(String(length=3))
    rate_issued_date_time = Column(DateTime)
    rate = Column(Float)
    rate_update_date_time = Column(DateTime)

    def __repr__(self):
        return "<TsysSaratogaConversionRate(id='%s, currency_code=%s, rate=%s')>" % \
               (self.id, self.currency_code, self.rate)
