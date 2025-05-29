from observers.base import Observer

class DatabaseWriter(Observer):
    def update(self, event_data: dict) -> None:
        """
        Write the S3 file ingestion event data to the database.
        
        :param event_data: A message or data that the observer needs to process.
        """
        file_path = event_data["s3_path"]
        print(f"[DBWriter] Writing extracted data from {file_path} to database.")