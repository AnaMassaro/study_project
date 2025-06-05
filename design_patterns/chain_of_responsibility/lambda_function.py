from chain_builder import ChainBuilder

from services.cache_service import CacheService
from services.sqs_service import SqsService

def lambda_handler(event, context):
    data = event['data']

    cache_service = CacheService()
    sqs_service = SqsService(queue_name="MinhaFila")

    builder = ChainBuilder(sqs_service, cache_service)
    handler_chain = builder.build_chain(data)
    
    try:
        result = handler_chain.handle(data)
        return {"statusCode": 200, "body": result}
    except Exception as e:
        return {"statusCode": 400, "body": str(e)}

if __name__ == '__main__':
    # Example event for local testing
    test_event = {
        'data': {
            'name': '  John Doe  ',
            'date': '01/02/2023',
            'amount': '100.50',
            'category_id': '001',
            'type': 'simple'
        }
    }
    print(lambda_handler(test_event, None))