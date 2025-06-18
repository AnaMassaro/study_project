from typing import Protocol, List, Dict


class DynamoPort(Protocol):
    """
    Port that defines the contract for accessing data from DynamoDB.
    The application layer will depend on this interface, not on concrete implementations.
    """

    def get_items_by_partition_key(self, partition_key: str) -> List[Dict]: ...
