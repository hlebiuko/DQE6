import great_expectations as gx
from great_expectations.checkpoint import Checkpoint

DATASOURCE_NAME = "MySQL"
HOST = "localhost"
PORT = "3306"
USERNAME = "root"
PASSWORD = "Password"
DATABASE = "AdventureWorks2012"
ADDRESS_TABLE_NAME = "Address"

context = gx.get_context()

CONNECTION_STRING = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
# context.delete_datasource(
#     datasource_name="mysql_datasource9"
# )
mysql_datasource = context.sources.add_sql(
    name="mysql_datasource9", connection_string=CONNECTION_STRING
)

mysql_datasource.add_table_asset(
    name="mysql_address_data", table_name=ADDRESS_TABLE_NAME
)

batch_request_address = mysql_datasource.get_asset("mysql_address_data").build_batch_request()

expectation_suite_name = "expectation_name"

context.add_or_update_expectation_suite(expectation_suite_name=expectation_suite_name)

validator_address = context.get_validator(
    batch_request=batch_request_address,
    expectation_suite_name=expectation_suite_name,
)

validator_address.expect_column_values_to_not_be_null(column="AddressID")
validator_address.expect_column_values_to_not_be_null(column="Address")
validator_address.expect_column_values_to_not_be_null(column="City")
validator_address.expect_column_values_to_not_be_null(column="PostalCode")
validator_address.expect_column_values_to_be_between(
    column="PostalCode", min_value=0, max_value=99999
)
validator_address.expect_column_values_to_be_in_set(
    column="CountryRegion", value_set=["Country1", "Country2", "Country3"]
)
validator_address.expect_column_values_to_match_regex(
    column="PostalCode", regex="^\\d{5}$"
)

validator_address.save_expectation_suite(discard_failed_expectations=False)

my_checkpoint_name = "my_sql_checkpoint"

checkpoint = Checkpoint(
    name=my_checkpoint_name,
    run_name_template="%Y%m%d-%H%M%S-my-run-name-template",
    data_context=context,
    batch_request=batch_request_address,
    expectation_suite_name=expectation_suite_name,
    action_list=[
        {
            "name": "store_validation_result",
            "action": {"class_name": "StoreValidationResultAction"},
        },
        {"name": "update_data_docs", "action": {"class_name": "UpdateDataDocsAction"}},
    ],
)

context.add_or_update_checkpoint(checkpoint=checkpoint)

checkpoint_result = checkpoint.run()

context.open_data_docs()

# context.delete_datasource(
#     datasource_name="mysql_datasource9"
# )

