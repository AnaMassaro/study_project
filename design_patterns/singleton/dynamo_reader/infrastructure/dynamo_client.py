from domain.ports.dynamo_port import DynamoPort
from shared.singleton import SingletonMeta
from typing import List, Dict


class DynamoClient(metaclass=SingletonMeta):
    """
    Simulates a DynamoDB client. In production, you'd use boto3 here.
    This class is a Singleton — only one instance will be created.
    """

    def get_items_by_partition_key(self, partition_key: str) -> List[Dict]:
        # Simulated data (as if it came from DynamoDB)
        data = [
            {"partition_key": "user#123", "name": "Ana", "age": 30},
            {"partition_key": "user#123", "name": "Ana", "purchase": "Book"},
            {"partition_key": "user#456", "name": "Carlos", "age": 25},
        ]

        # Filters only the items for the requested partition key
        return [item for item in data if item["partition_key"] == partition_key]
