from observers.base import Observer

class S3FileProcessor(Observer):
    def update(self, event_data: dict) -> None:
        """
        Process the S3 file ingestion event data.
        
        :param event_data: A message or data that the observer needs to process.
        """
        file_path = event_data["s3_path"]
        print(f"[FileProcessor] Processing file from: {file_path}")