from domain.entities import AWSAccount
from domain.ports.aws_client_port import AWSClientPort
from domain.ports.publisher_port import PublisherPort


class DescribeFunctionsService:
    def __init__(self, aws_client: AWSClientPort, publisher: PublisherPort):
        self.aws_client = aws_client
        self.publisher = publisher

    def execute(self, accounts: list[AWSAccount]) -> None:
        for account in accounts:
            print(f"[INFO] Coletando funções da conta: {account.account_id}")
            functions = self.aws_client.describe_functions(account)

            grouped = self._group_by_runtime(functions)

            for runtime, funcs in grouped.items():
                payload = {
                    "account_id": account.account_id,
                    "region": account.region,
                    "runtime": runtime,
                    "functions": funcs,
                }
                self.publisher.publish(payload)

    def _group_by_runtime(self, functions: list[dict]) -> dict:
        grouped = {}
        for f in functions:
            runtime = f.get("Runtime", "unknown")
            grouped.setdefault(runtime, []).append(f["FunctionName"])
        return grouped
