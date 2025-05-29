from observers.base import Observer

class SQSNotifier(Observer):
    def update(self, event_data: dict) -> None:
        """
        Notify via SQS about the S3 file ingestion event.
        
        :param event_data: A message or data that the observer needs to process.
        """
        file_path = event_data["s3_path"]
        print(f"[SQSNotifier] Sending notification for file: {file_path} to SQS.")
