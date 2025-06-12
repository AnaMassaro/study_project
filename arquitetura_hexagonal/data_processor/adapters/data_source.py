from interfaces.data_fetcher import DataFetcher
from typing import List, Dict, Any


class InMemoryDataSource(DataFetcher):
    def fetch_raw_data(self) -> List[Dict[str, Any]]:
        """
        Simula a leitura de dados vindos de um banco.
        Em um cenário real, aqui faríamos uma consulta ao banco de dados
        Retorna uma lista de registros no formato:
        {"category": str, "value": int}
        """
        return [
            {"category": "finance", "value": 100},
            {"category": "finance", "value": 150},
            {"category": "hr", "value": 50},
            {"category": "engineering", "value": 200},
            {"category": "engineering", "value": 180},
            {"category": "hr", "value": 70}
        ]