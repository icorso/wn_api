import csv
import hashlib
from csv import *
from datetime import datetime, timedelta
from enum import Enum


def today(days=0, hours=0, format='%d-%m-%Y:%H:%M:%S:000'):
    return (datetime.now() + timedelta(days=days, hours=hours)).strftime(format)


class DialectEnum(Enum):
    delimiter = (',', ';', '    ')
    quotechar = ('"', '\'')
    escapechar = None
    doublequote = True
    skipinitialspace = False
    lineterminator = ('\r\n', '\n')
    quoting = (QUOTE_MINIMAL, QUOTE_ALL, QUOTE_NONE, QUOTE_NONNUMERIC)


class DefaultDialect(Dialect):
    delimiter = DialectEnum.delimiter.value[1]
    quotechar = '"'
    escapechar = None
    doublequote = True
    skipinitialspace = False
    lineterminator = '\r\n'
    quoting = DialectEnum.quoting.value[3]


class BulkPayment:
    def __init__(self, terminal_id, secret_phrase, **kwargs):
        self.columns = ['ORDERID', 'CURRENCY', 'AMOUNT', 'CARDNUMBER', 'CARDTYPE', 'CARDEXPIRY', 'CARDHOLDERNAME',
                        'ADDRESS1', 'ADDRESS2', 'POSTCODE', 'DATETIME', 'HASH', 'AUTOREADY', 'DESCRIPTION', 'EMAIL',
                        'ORIGINALBRANDTXIDENTIFIER', 'STOREDCREDENTIALTXTYPE', 'STOREDCREDENTIALUSE']
        self.hash_fields = ['ORDERID', 'AMOUNT', 'DATETIME']
        self.dialect = DefaultDialect
        self.data = dict()
        self._is_header = False
        self.with_field(**kwargs)
        self.terminal_id = terminal_id
        self.secret_phrase = secret_phrase

    def set_dialect(self, dialect_class):
        self.dialect = dialect_class

    def with_field(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.columns:
                self.data.update(kwargs)
            else:
                raise Exception(f'Column {k} does not exist')
        return self

    def with_header(self):
        self._is_header = True
        return self

    def write_csv(self):
        self.generate_hash()
        index_map = {v: i for i, v in enumerate(self.columns)}
        a = dict(sorted(self.data.items(), key=lambda pair: index_map[pair[0]]))
        with open('mycsvfile.csv', 'w') as f:
            w = csv.DictWriter(f, a.keys(), dialect=self.dialect)
            if self._is_header:
                w.writeheader()
            w.writerow(a)

    def encode_string(self, input_string: str, is_old_hash=False):
        m = hashlib.sha256()
        if is_old_hash:  # the string should be w/o a separator
            m = hashlib.md5()
        m.update(str.encode(input_string))
        return m.hexdigest()

    def generate_hash(self):
        hash_string = [str(self.data[k]) for k in self.hash_fields]
        self.data['HASH'] = self.encode_string(':'.join(hash_string))


d = {'AMOUNT': 3.11, 'DATETIME': today()}

bulk_payment = BulkPayment(terminal_id='21001', secret_phrase='someSecretPhrase', **d)
bulk_payment.with_field(CURRENCY='USD')
bulk_payment.with_field(ORDERID='239892843')
bulk_payment.with_header()
print(bulk_payment.write_csv())
