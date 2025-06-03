from lambda_function import lambda_handler


def test_lambda_handler():
    event = {
        "id": "123",
        "name": "test_name"
    }

    response = lambda_handler(event, None)
    print(response)
    

if __name__ == "__main__":
    test_lambda_handler()