from typing import Protocol

from domain.entities import AWSAccount


class AWSClientPort(Protocol):
    def describe_functions(self, account: AWSAccount) -> list[dict]:
        """
        Retrieves a list of Lambda functions from the given AWS account.
        Should raise ThrottleError on throttling or AWSClientError for other issues.
        """
        ...
