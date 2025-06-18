from domain.ports.dynamo_port import DynamoPort
from typing import List, Dict
from .format_partition_items import format_partition_item


class ReadPartitionUseCase:
    """
    Application layer use case for reading a partition from the database.
    Depends only on the DynamoPort interface.
    """

    def __init__(self, dynamo_repo: DynamoPort):
        self._dynamo_repo = dynamo_repo

    def execute(self, partition_key: str) -> List[Dict]:
        """
        Retrieves and returns all items for the given partition key.
        """
        raw_items = self._dynamo_repo.get_items_by_partition_key(partition_key)

        formatted_items = [format_partition_item(item) for item in raw_items]
        return formatted_items
