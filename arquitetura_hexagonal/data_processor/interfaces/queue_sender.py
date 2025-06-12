from abc import ABC, abstractmethod
from typing import Dict, Any

class QueueSender(ABC):
    @abstractmethod
    def send(self, payload: Dict[str, Any]) -> None:
        """Envia um payload formatado para uma fila (ex: SQS)."""
        pass
