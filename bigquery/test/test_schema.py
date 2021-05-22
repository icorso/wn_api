from hamcrest import assert_that, equal_to, is_

from bigquery.bigquery_client import BigQueryClient
from bigquery.constants import SCHEMA_FIELDS, SCHEMA_CUSTOM_FIELD, SCHEMA_ACH_JH_TRASACTION, SCHEMA_CUP_TRANSACTION, \
    SCHEMA_LEVEL_CARD_DATA, SCHEMA_THREAT_METRIX, SCHEMA_EXTRA_PARAM

bq = BigQueryClient()

dataset = 'qa_dataset'


def test_schema_fields():
    table_name = 'closed_transaction_2017'  # TODO should check all closed txn tables
    table_schema = bq.get_table_schema(table_name)
    custom_field_schema = list(filter(lambda field: field.name == 'custom_field', table_schema))[0]
    ach_jh_transaction_schema = list(filter(lambda field: field.name == 'ach_jh_transaction', table_schema))[0]
    cup_transaction_schema = list(filter(lambda field: field.name == 'cup_transaction', table_schema))[0]
    level_card_data_schema = list(filter(lambda field: field.name == 'level_card_data', table_schema))[0]
    threat_metrix_schema = list(filter(lambda field: field.name == 'threat_metrix', table_schema))[0]
    extra_param_schema = list(filter(lambda field: field.name == 'extra_param', table_schema))[0]

    field_names = [field.name for field in table_schema]
    custom_field_names = [field.name for field in custom_field_schema.fields]
    ach_jh_transaction_names = [field.name for field in ach_jh_transaction_schema.fields]
    cup_transaction_names = [field.name for field in cup_transaction_schema.fields]
    level_card_data_names = [field.name for field in level_card_data_schema.fields]
    threat_metrix_names = [field.name for field in threat_metrix_schema.fields]
    extra_param_names = [field.name for field in extra_param_schema.fields]

    # verifying the top level fields
    assert_that(set(SCHEMA_FIELDS).difference(set(field_names)), is_(set()),
                'Expected fields don\'t exist in \'%s\' table' % table_name)
    assert_that(set(field_names).difference(set(SCHEMA_FIELDS)), is_(set()),
                '\'%s\' table fields do not exist in expected fields' % table_name)

    # verifying the second level fields
    assert_that(custom_field_names, equal_to(SCHEMA_CUSTOM_FIELD), 'custom_field fields don\'t correspond to expected')
    assert_that(ach_jh_transaction_names, equal_to(SCHEMA_ACH_JH_TRASACTION), 'ach_jh_trasaction fields don\'t correspond to expected')
    assert_that(cup_transaction_names, equal_to(SCHEMA_CUP_TRANSACTION), 'cup_trasaction fields don\'t correspond to expected')
    assert_that(level_card_data_names, equal_to(SCHEMA_LEVEL_CARD_DATA), 'level_card_data fields don\'t correspond to expected')
    assert_that(threat_metrix_names, equal_to(SCHEMA_THREAT_METRIX), 'threat_metrix fields don\'t correspond to expected')
    assert_that(extra_param_names, equal_to(SCHEMA_EXTRA_PARAM), 'extra_param fields don\'t correspond to expected')
