from operator import attrgetter

from sqlalchemy import and_

from db.db_models import OpenTransaction, ClosedTransaction, AchjhTransaction, AchjhTransactionStateHistory, \
    AchIntegrapayTransactionStateHistory, Currency, Terminal, TransactionCofDetails, SecureCard, \
    SecureCardAdditionalSetting, TransactionSurcharge, ApiKey, TransactionTip, FDRCTransaction
from db.mysql_client import DbSession
from utils import logger

db = DbSession()


class UtilityHelper(object):
    def get_currency_by_id(self, id):
        return db.query_first(Currency, Currency.id == id)

    def get_api_key(self, key_alias: str):
        return db.query_first(ApiKey, ApiKey.key_alias == key_alias)


class TransactionsHelper(object):
    def __init__(self, terminal_number=None):
        self._terminal_id = None
        self._terminal_number = terminal_number
        if terminal_number:
            t = db.query_first(Terminal, Terminal.terminal_number == terminal_number)
            self._terminal_id = t.id if t else None

    @property
    def terminal_id(self):
        return self._terminal_id

    @property
    def terminal_number(self):
        return self._terminal_number

    def find_no_events_transactions(self):
        tx_list = []
        txs_filter = [OpenTransaction.responsecode != 'D', OpenTransaction.cardtype == 26]
        if self._terminal_id:
            txs_filter.append(OpenTransaction.terminalid == self._terminal_id)

        for tx in db.query_all(OpenTransaction, and_(*txs_filter)):
            if len(self.find_transaction_events(tx.id)) == 0:
                tx_list.append(tx)

        for t in tx_list:  # exclude parent refund tx_list
            opened_tx = list(filter(lambda OpenTransaction: OpenTransaction.id == t.originaltransactionid, tx_list))
            if t.originaltransactionid and len(opened_tx) > 0:
                tx_list.remove(opened_tx[0])

        logger.warning("Collected '" + str(len(tx_list)) + "' transactions without events.")
        return tx_list

    def find_transaction(self, tx_id):
        tx = db.query_first(OpenTransaction, OpenTransaction.id == tx_id)
        if tx is None:
            tx = db.query_first(ClosedTransaction, ClosedTransaction.id == tx_id)
        return tx

    def get_transaction(self, **kwargs):
        for c in [OpenTransaction, ClosedTransaction]:
            for k, v in kwargs.items():
                tx = db.query_first(c, and_(getattr(c, k) == v, getattr(c, 'terminalid') == self.terminal_id))
                if tx:
                    return tx
        return None

    def get_transaction_cof_details(self, transaction_id):
        return db.query_first(TransactionCofDetails, TransactionCofDetails.id == transaction_id)

    def get_transaction_surcharge(self, transaction_id):
        return db.query_first(TransactionSurcharge, TransactionSurcharge.id == transaction_id)

    def get_transaction_tip(self, transaction_id):
        return db.query_first(TransactionTip, TransactionTip.id == transaction_id)

    def find_gray_area_transactions(self):
        txs = []
        for t in db.query_all(ClosedTransaction, ClosedTransaction.amount.contains('.90')):
            if db.query_first(AchjhTransaction, and_(AchjhTransaction.gray_area == 0, AchjhTransaction.id == t.id)):
                txs.append(t)
        return txs

    def find_refunded_originals(self):
        txs = []
        for t in db.query_all(OpenTransaction, OpenTransaction.originaltransactionid != None):
            if self.is_ach_transaction(t.id):
                txs.append(self.find_transaction(t.originaltransactionid))
        return txs

    def is_transaction_closed(self, tx_id):
        return db.query_first(ClosedTransaction, ClosedTransaction.id == tx_id)

    def is_ach_transaction(self, tx_id):
        return db.query_first(AchjhTransaction, AchjhTransaction.id == tx_id)

    def find_transaction_events(self, tx_id):
        return db.query_all(AchjhTransactionStateHistory, AchjhTransactionStateHistory.transaction_id == tx_id)

    def get_fdrc_transaction(self, tx_id):
        tx = db.query_first(FDRCTransaction, FDRCTransaction.id == tx_id)
        return tx


class SecureCardHelper(TransactionsHelper):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_secure_card(self, merchantref):
        criteria = and_(SecureCard.merchantref == merchantref)
        if self.terminal_id:
            criteria = and_(SecureCard.merchantref == merchantref, SecureCard.terminalid == self.terminal_id)

        return db.query_first(SecureCard, criteria)

    def get_secure_card_additional_settings(self, merchantref):
        sc = self.get_secure_card(merchantref)
        if sc:
            return db.query_first(SecureCardAdditionalSetting, SecureCardAdditionalSetting.id == sc.additional_setting_id)
        return None


class DirectDebitHelper(object):

    def direct_debit_open_transactions_list(self):
        return db.query_all(OpenTransaction, and_(OpenTransaction.bank_id == 66, OpenTransaction.cardtype == 30))

    def direct_debit_transaction_history(self, tx_id):
        return db.query_all(AchIntegrapayTransactionStateHistory,
                            AchIntegrapayTransactionStateHistory.original_transaction_id == tx_id)

    def get_direct_debit_transaction_last_event(self, tx_id):
        events = self.direct_debit_transaction_history(tx_id)

        try:
            return sorted(events, key=attrgetter('id'), reverse=True)[0]
        except IndexError:
            return None
