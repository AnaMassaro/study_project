from event_dispatcher import EventDispatcher
from observers.file_processor import S3FileProcessor
from observers.db_writer import DatabaseWriter
from observers.sqs_notifier import SQSNotifier

def lambda_handler(event, context):
    s3_path = event.get("s3_path")
    if not s3_path:
        return {
            "statusCode": 400,
            "body": "Missing 's3_path' in event data."
        }
    
    dispatcher = EventDispatcher()
    dispatcher.register(S3FileProcessor())
    dispatcher.register(DatabaseWriter())
    dispatcher.register(SQSNotifier())

    dispatcher.notify({"s3_path": s3_path})
    return {
        "statusCode": 200,
        "body": f"Event processed for S3 path: {s3_path}"
    }

if __name__ == "__main__":
    # Example event for local testing
    test_event = {
        "s3_path": "s3://my-bucket/my-file.txt"
    }
    response = lambda_handler(test_event, None)
    print(response)