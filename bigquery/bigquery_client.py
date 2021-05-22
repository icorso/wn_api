import json
import os

from google.cloud import bigquery
from google.oauth2 import service_account


class BigQueryClient:
    def __init__(self, project=None, account_file=None, dataset=None):
        try:
            root_dir = os.path.dirname(os.path.abspath(__file__))
            access_file_path = os.path.join(root_dir, "credentials.json")

            with open(access_file_path, "r") as json_file:
                data = json.load(json_file)
            self.__project = data['project']
            self.__credentials = service_account.Credentials.from_service_account_file(data['account_file_path'])
            self.__client = bigquery.Client(project=self.__project, credentials=self.__credentials)
            json_file.close()
        except FileNotFoundError:
            if project is None or account_file is None:
                raise Exception('Empty project or account_file property')
            self.__project = project
            self.__credentials = service_account.Credentials.from_service_account_file(account_file)
            self.__client = bigquery.Client(project=self.__project, credentials=self.__credentials)
        self.dataset = dataset if dataset else 'qa_dataset'

    def with_dataset(self, dataset_name):
        self.dataset = dataset_name
        return self

    def get_client(self):
        return self.__client

    def get_table_schema(self, table_name):
        return self.__client.get_table('%s.%s' % (self.dataset, table_name)).schema
