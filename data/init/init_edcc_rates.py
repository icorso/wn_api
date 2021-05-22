"""delete from tsys_saratoga_conversion_rate;
set @tc=840;
INSERT INTO tsys_saratoga_conversion_rate SET terminal_base_currency_code=@tc, currency_code=840, rate='1', date=CURRENT_DATE(), rate_issued_date_time=DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL -1 DAY), rate_update_date_time=NOW();
# EUE 2 m.unit
INSERT INTO tsys_saratoga_conversion_rate SET terminal_base_currency_code=@tc, currency_code=978, rate='0.831400', date=CURRENT_DATE(), rate_issued_date_time=DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL -1 DAY), rate_update_date_time=NOW();
# JPY 0 m.unit
INSERT INTO tsys_saratoga_conversion_rate SET terminal_base_currency_code=@tc, currency_code=392, rate='0.009469', date=CURRENT_DATE(), rate_issued_date_time=DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL -1 DAY), rate_update_date_time=NOW();
# GBP
INSERT INTO tsys_saratoga_conversion_rate SET terminal_base_currency_code=@tc, currency_code=826, rate='0.729518', date=CURRENT_DATE(), rate_issued_date_time=DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL -1 DAY), rate_update_date_time=NOW();
# KWD 3 units
INSERT INTO tsys_saratoga_conversion_rate SET terminal_base_currency_code=@tc, currency_code=414, rate='0.302832', date=CURRENT_DATE(), rate_issued_date_time=DATE_ADD(CURRENT_TIMESTAMP(), INTERVAL -1 DAY), rate_update_date_time=NOW();
"""

from constants import EdccRates, Currency
from db.db_models import TsysSaratogaConversionRate
from db.mysql_client import DbSession
from utils import today

db = DbSession()


def add_tsys_saratoga_edcc_rates():
    db.delete_all(TsysSaratogaConversionRate)
    for r in list(EdccRates):
        model = TsysSaratogaConversionRate()
        model.rate = r.rate
        model.currency_code = r.currency_code
        model.date = today(format='%Y-%m-%d')
        model.rate_update_date_time = today(format='%Y-%m-%d')
        model.rate_issued_date_time = today(format='%Y-%m-%d', days=-1)
        model.terminal_base_currency_code = Currency.USD.code
        db.add(model)


def add_tsys_saratoga_gbp_cad_rate():
        model = TsysSaratogaConversionRate()
        model.rate = EdccRates.CAD.rate
        model.currency_code = Currency.GBP.code
        model.date = today(format='%Y-%m-%d')
        model.rate_update_date_time = today(format='%Y-%m-%d')
        model.rate_issued_date_time = today(format='%Y-%m-%d', days=-1)
        model.terminal_base_currency_code = Currency.CAD.code
        db.add(model)
