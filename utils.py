import hashlib
import logging
import os
import random
import sys
from collections import namedtuple
from datetime import datetime, timedelta
from logging.handlers import RotatingFileHandler
from urllib.parse import urlunparse

from faker import Factory

from constants import Currency

LOGFILE = str(os.path.dirname(os.path.abspath(__file__))) + "/wnapi.log"
LOGGER_FORMAT = '%(asctime)s - %(message)s'
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler(sys.stdout)
f_handler = RotatingFileHandler(LOGFILE, maxBytes=(1048576 * 3), backupCount=2)
# f_handler = logging.FileHandler(LOGFILE)
c_handler.setLevel(logging.WARN)
f_handler.setLevel(logging.WARN)

# Create formatters and add it to handlers
c_format = logging.Formatter(LOGGER_FORMAT)
f_format = logging.Formatter(LOGGER_FORMAT)
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)


fake = Factory.create()


def today(days=0, hours=0, format='%d-%m-%Y:%H:%M:%S:000'):
    return (datetime.now() + timedelta(days=days, hours=hours)).strftime(format)


def build_url(scheme=None, netloc=None, path=None):
    scheme = scheme if scheme else 'http'
    netloc = netloc if netloc else 'wn:8080'
    path = path if path else ''
    return urlunparse((scheme, netloc, path, '', '', ''))


def random_text(length=10, upper=True, lower=False):
    return fake.password(length=length, upper_case=upper, lower_case=lower, special_chars=False)


def random_card(cardtype=None):
    if not cardtype:
        creditcard = str(fake.credit_card_full()).split('\n')
    else:
        creditcard = str(fake.credit_card_full(cardtype.lower())).split('\n')
    cardnumber = creditcard[2].split(' ')

    ccard = namedtuple('CreditCard', 'cardtype, cardholder, cardnumber, cardexpiry, cvv')
    cardtype = creditcard[0] if 'VISA' not in creditcard[0] else creditcard[0].split(' ')[0]
    cardtype = 'AMEX' if 'American' in creditcard[0] else creditcard[0].split(' ')[0]

    return ccard(cardtype.upper(),
                 creditcard[1],
                 cardnumber[0],
                 cardnumber[1].replace('/', ''),
                 creditcard[3].replace('CVC: ', '').replace('CVV: ', ''))


def masked_pan(pan: str) -> str:
    return pan[0:6] + '*' * (len(pan) - 10) + pan[-4:len(pan)]


def random_amount(digits=1, minorunits=None, currency=Currency.USD, positive=True):
    """
    Generates random amount
    :param digits: integer part of amount
    :param minorunits: fractional part of amount (cents)
    :param currency: constants.Currency enum
    :param positive: True/False
    :return: float amount
    """
    amount = float(fake.pydecimal(left_digits=digits, right_digits=currency.minorunits, positive=positive))
    if minorunits:
        amount = float(int(amount) + minorunits/10**currency.minorunits)
    if amount == 0.00:
        amount += float(0.01)
    return amount


def random_surcharge_percent(minorunits=5):
    left_digits = str(random.choice(range(0, 4)))
    right_digits = str(fake.pyfloat(left_digits=0, right_digits=minorunits, positive=True))\
                       .split('.')[1]\
                       .ljust(minorunits, '1')
    return float(left_digits + '.' + right_digits)


class SurchargeAmount(object):
    # for a new formula see ticket #31231
    def __init__(self, amount: float, percentage: float, currency=Currency.USD):
        self._percentage = round(percentage, 5)
        self._amount = amount
        self._surcharge = round(float(self._amount) * (self._percentage / 100), currency.minorunits)
        self._total_amount = round(float(self._amount) + self._surcharge, currency.minorunits)

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        self._percentage = value

    @property
    def surcharge(self):
        return self._surcharge

    @surcharge.setter
    def surcharge(self, value):
        self._surcharge = value

    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value

    def __repr__(self):
        return '<%s.%s object at %s\namount=%s,\npercentage=%s,\nsurcharge=%s,\ntotal_amount=%s' % (
            self.__class__.__module__,
            self.__class__.__name__,
            hex(id(self)),
            self._amount, self._percentage, self._surcharge, self._total_amount
        )


def split_string(string, divider='-', position=4):
    return divider.join(string[i:i + position] for i in range(0, len(string), position)) if position != 0 else string


def generate_hash(string, algorithm='sha512'):
    if algorithm in {'MD5', 'md5'}:
        m = hashlib.md5()
    elif algorithm in {'SHA256', 'sha256'}:
        m = hashlib.sha256()
    else:
        m = hashlib.sha512()

    m.update(str.encode(string))
    return m.hexdigest()
