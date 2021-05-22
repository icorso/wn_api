import random
from operator import attrgetter
from faker import Factory

from sqlalchemy import and_

from db.db_models import OpenTransaction, ClosedTransaction, AchjhTransaction, AchjhTransactionStateHistory, \
    AchIntegrapayTransactionStateHistory, Currency, Terminal, TransactionCofDetails, SecureCard, \
    SecureCardAdditionalSetting, TransactionSurcharge, ApiKey, TransactionTip, FDRCTransaction, DaoStatistic, \
    DaoStatisticDetails
from db.mysql_client import DbSession
from utils import logger, today

db = DbSession()

fake = Factory.create()


def test_insert_dao_statistic():
    for i in range(1000):
        dao_statistic = DaoStatistic(
            nodename=random.choice(['vkapp1/nettraxion/vkapp1', 'vcapp1/nettraxion/vcapp1']),
            date=today(days=-366 - i, format='%Y-%m-%d'),
            eliminate=0,
            notes=fake.text(20)
        )
        db.add(dao_statistic)


def test_insert_dao_statistic_details():
    dao_statistic_first_id = 76
    dao_statistic_last_id = 2000
    dao_statistic_details_per_item = 10
    dao_statistic_list = db.query_all(DaoStatistic, DaoStatistic.id >= dao_statistic_first_id)
    for d in dao_statistic_list:
        for i in range(dao_statistic_details_per_item):
            db.query_all(DaoStatistic, DaoStatistic.id == dao_statistic_first_id)
            dao_statistic_details = DaoStatisticDetails(
                methodname=random.choice(['JPAPurgingDAO::removeForeignKey', 'JPAUserDAO::findByUserName',
                                          'JPABatchDAO::create', 'JPASystemsettingsDAO::getIntValue',
                                          'JPASearchDAO::findSearchByName', 'JPAGenericDAO::create'
                                          'JPATransactionPerHourCountDAO::findTransactionPerHourBy']),
                executionscount=fake.random_number(2),
                minexecutiontime=fake.random_number(2),
                maxexecutiontime=fake.random_number(2),
                totalexecutiontime=fake.random_number(2),
                daostatisticid=d.id
            )
            db.add(dao_statistic_details)
        if d.id >= dao_statistic_last_id:
            break
