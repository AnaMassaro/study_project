from chain_builder import build_handler_chain

def lambda_handler(event, context):
    data = event['data']

    chain = build_handler_chain()
    
    try:
        result = chain.handle(data)
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
            'category_id': '001'
        }
    }
    print(lambda_handler(test_event, None))