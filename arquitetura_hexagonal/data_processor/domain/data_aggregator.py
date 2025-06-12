from collections import defaultdict
from typing import List, Dict, Any

class DataAggregator:
    def aggregate_by_category(self, raw_data: List[Dict[str, Any]]) -> Dict[str, List[Any]]:
        """
        Agrupa os dados por categoria.

        Exemplo de entrada:
        [
            {"category": "finance", "value": 10},
            {"category": "finance", "value": 20},
            {"category": "hr", "value": 5}
        ]

        Saída:
        {
            "finance": [10, 20],
            "hr": [5]
        }
        """
        grouped = defaultdict(list)
        for record in raw_data:
            try:
                category = record["category"]
                value = record["value"]
                grouped[category].append(value)
            except KeyError as e:
                # Se um campo obrigatório estiver ausente, ignora o registros
                continue
        return dict(grouped)
