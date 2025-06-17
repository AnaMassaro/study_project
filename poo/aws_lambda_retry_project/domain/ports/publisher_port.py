from typing import Protocol


class PublisherPort(Protocol):
    def publish(self, message: dict) -> None:
        """
        Sends the given message to an external queue or system.
        """
        ...
