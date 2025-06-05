class SqsService:
    def __init__(self, queue_name: str):
        self.queue_name = queue_name

    def send_message(self, message):
        return True
