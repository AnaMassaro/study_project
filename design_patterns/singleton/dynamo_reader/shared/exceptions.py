class MissingPartitionKeyError(Exception):
    """Raised when the partition_key is missing from the event input."""

    def __init__(self):
        super().__init__("partition_key is required in the event.")
