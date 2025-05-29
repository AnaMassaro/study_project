from file_processor import process_file
from decorators.logging_decorator import logging_decorator
from decorators.exception_decorator import exception_decorator

@logging_decorator
@exception_decorator
def lambda_handler(event, context):
    """
    AWS Lambda function handler that processes a file content.
    
    :param event: The event data passed to the Lambda function.
    :param context: The context object provided by AWS Lambda.
    :return: The processed file content.
    """
    print("Lambda function started.")
    
    file_content = event.get('file_content', 'default content')
    processed_content = process_file(file_content)
    
    print(f"Processed content: {processed_content}")
    
    return {
        'statusCode': 200,
        'body': processed_content
    }

if __name__ == "__main__":
    # Example event for local testing
    test_event = {
        'file_content': 'Hello, World!'
    }
    test_context = None  # Context is not used in this example
    
    response = lambda_handler(test_event, test_context)
    print(f"Response: {response}")