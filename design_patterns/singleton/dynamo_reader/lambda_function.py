from application.get_partition_items import ReadPartitionUseCase
from infrastructure.dynamo_client import DynamoClient
from shared.exceptions import MissingPartitionKeyError


def lambda_handler(event: dict, context=None):
    """
    Simulates an AWS Lambda handler.
    Receives a partition key and retrieves matching items from DynamoDB.
    """

    partition_key = event.get("partition_key")

    if not partition_key:
        raise MissingPartitionKeyError()

    client = DynamoClient()
    use_case = ReadPartitionUseCase(dynamo_repo=client)

    items = use_case.execute(partition_key=partition_key)

    print(f"✅ Retrieved {len(items)} item(s) from DynamoDB:")

    return {"statusCode": 200, "body": items}


if __name__ == "__main__":
    event = {"partition_key": "user#123"}
    # event = {}
    response = lambda_handler(event)
    print(response)
