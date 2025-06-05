from core.chain import Handler

class SendToSQSHandler(Handler):
    def __init__(self, sqs_service):
        super().__init__()
        self.sqs_service = sqs_service

    def handle(self, data):
        print("Sending data to SQS...")
        
        self.sqs_service.send_message(data)

        return data