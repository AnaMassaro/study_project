from domain.ports.publisher_port import PublisherPort


class SqsPublisher(PublisherPort):
    def __init__(self, queue_name: str):
        self._queue_name = queue_name

    def publish(self, grouped_data: dict) -> None:
        print(f"[SQS:{self._queue_name}] Enviando dados para a fila...")
        for account_id, functions in grouped_data.items():
            print(f"  → {account_id}: {functions}")
