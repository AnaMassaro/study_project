from src.context.execution_timer import ExecutionTimer
from src.services.dynamodb_service import simulate_dynamodb_put_item
import json

def lambda_handler(event, context):
    item = {
        "id": event.get("id", "default_id"),
        "name": event.get("name", "default_name"),
    }

    with ExecutionTimer("DynamoDB PutItem"):
        response = simulate_dynamodb_put_item(item)

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Item processed successfully",
            "response": response
        })
    }