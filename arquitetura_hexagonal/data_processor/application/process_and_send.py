from domain.data_aggregator import DataAggregator
from interfaces.data_fetcher import DataFetcher
from interfaces.queue_sender import QueueSender


def process_and_send(data_fetcher: DataFetcher, queue_sender: QueueSender) -> None:
    """
    Use case que orquestra a operação:
    - Busca os dados
    - Processa (agrega por categoria)
    - Envia para a fila
    """
    raw_data = data_fetcher.fetch_raw_data()
    
    aggregator = DataAggregator()
    grouped_data = aggregator.aggregate_by_category(raw_data)
    
    queue_sender.send(grouped_data)
