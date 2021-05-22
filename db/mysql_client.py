# coding=utf-8
import json
import os

from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker


class DbSession(object):
    """
    MySQL connector
    Win platform: https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient
    *nix: sudo apt-get install python-mysqldb
    """
    def __init__(self):
        root_dir = os.path.dirname(os.path.abspath(__file__))
        access_file_path = os.path.join(root_dir, "../credentials.json")

        with open(access_file_path, "r") as json_file:
            data = json.load(json_file)

        self.host = data['db_host']
        self.port = '3306'
        self.user = data['db_user']
        self.password = data['db_password']
        self.db = data['db_scheme']
        self.engine = create_engine('mysql+mysqlconnector://' + self.user + ':' + self.password + '@' + self.host
                                    + ':' + self.port + '/' + self.db + '?charset=utf8')

    def query_first(self, table, filter_):
        """Выборка первой записи по указанному фильтру из таблицы

        Args:
            table: представление таблицы БД
            (см. http://docs.sqlalchemy.org/en/latest/core/metadata.html#sqlalchemy.schema.Table)
            filter_: фильтр данных из таблицы
        Returns:
            Первый результат запроса (заполненный 'table' инстанс) или None если резутат не содержит записей.
            Example: user.query_first(History, History.mobile_phone == '3456774')
        """
        s = sessionmaker(bind=self.engine, expire_on_commit=False)()
        result = s.query(table).filter(filter_).first()
        s.close()
        return result

    def query_all(self, table, filter_=text('')):
        """Выборка всех записей по указанному фильтру из таблицы
        Example: user.query_all(Advance, Advance.advance_time.like('2015-10-08%'))
        Args:
            table: представление таблицы БД
            (см. http://docs.sqlalchemy.org/en/latest/core/metadata.html#sqlalchemy.schema.Table)
            filter_: фильтр данных из таблицы
        Returns:
              список всех найденных записей
        """
        s = sessionmaker(bind=self.engine, expire_on_commit=False)()
        results = s.query(table).filter(filter_).all()
        s.close()
        return results

    def add(self, params):
        """Добавление данных в таблицу
        Example: user.add(users.OPERATOR.customers_data)
        Args:
            params: представление таблицы БД
            (см. http://docs.sqlalchemy.org/en/latest/core/metadata.html#sqlalchemy.schema.Table)
        """
        s = sessionmaker(bind=self.engine, expire_on_commit=False)()
        s.add(params)
        s.commit()
        s.close()

    def update(self, table, filter_, params):
        """Обновление данных в таблице базы данных
        Args:
            table: представление таблицы БД
            (см. http://docs.sqlalchemy.org/en/latest/core/metadata.html#sqlalchemy.schema.Table)
            filter_: фильтр данных из таблицы
            params: параметры с новыми данными, например {"name": 'new_name'}
        Returns: количество строк которые были обновлены
        """
        s = sessionmaker(bind=self.engine, expire_on_commit=False)()
        result = s.query(table).filter(filter_).update(params)
        s.commit()
        s.close()
        return result

    def delete(self, table, filter_):
        """Удаление записи(ей) из таблицы
        Example: user.delete(Customers, Customers.id == 3)
        Args:
            table: представление таблицы БД
            (см. http://docs.sqlalchemy.org/en/latest/core/metadata.html#sqlalchemy.schema.Table)
            filter_: фильтр данных из таблицы
        """
        s = sessionmaker(bind=self.engine)()
        s.delete(self.query_first(table, filter_))
        s.commit()
        s.close()

    def delete_all(self, table):
        """Удаление всех записи(ей) из таблицы
        Example: user.delete(Customers)
        Args:
            table: представление таблицы БД
            (см. http://docs.sqlalchemy.org/en/latest/core/metadata.html#sqlalchemy.schema.Table)
        """
        s = sessionmaker(bind=self.engine)()
        s.query(table).delete()
        s.commit()
        s.close()
