from abc import ABC, abstractmethod
from typing import List, Dict, Any

class DataFetcher(ABC):
    @abstractmethod
    def fetch_raw_data(self) -> List[Dict[str, Any]]:
        """Busca os dados brutos que serão processados."""
        pass
