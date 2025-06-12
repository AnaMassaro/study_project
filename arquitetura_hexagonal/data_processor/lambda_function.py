from adapters.data_source import InMemoryDataSource
from adapters.queue_sqs_sender import QueueSqsSender
from application.process_and_send import process_and_send


def lambda_handler(event=None, context=None):
    """
    Ponto de entrada da aplicação.
    Simula o handler da AWS Lambda.
    """
    data_source = InMemoryDataSource()
    queue_sender = QueueSqsSender()
    
    process_and_send(data_source, queue_sender)
    
    return {
        "statusCode": 200,
        "body": "Dados processados e enviados com sucesso."
    }


# Executar localmente (útil para rodar sem AWS)
if __name__ == "__main__":
    print("⏳ Executando handler localmente...")
    response = lambda_handler()
    print("✅ Fim da execução:", response)
