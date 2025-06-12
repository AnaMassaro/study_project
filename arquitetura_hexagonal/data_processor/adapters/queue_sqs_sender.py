from interfaces.queue_sender import QueueSender
from typing import Dict, Any


class QueueSqsSender(QueueSender):
    def send(self, payload: Dict[str, Any]) -> None:
        """
        Simula o envio de um payload para uma fila SQS.
        Em um cenário real, aqui usaríamos boto3 para enviar a mensagem.
        """
        print("📤 Enviando para fila SQS...")
        print(payload)
