from domain.entities import AWSAccount
from infrastructure.aws_cli_client import AwsCliClient
from infrastructure.sqs_publisher import SqsPublisher
from services.describe_functions_service import DescribeFunctionsService


def lambda_handler(event=None, context=None):
    print("[START] Lambda handler iniciado")

    # Simulando contas
    accounts = [
        AWSAccount(account_id="123456789012", region="us-east-1"),
        AWSAccount(account_id="210987654321", region="us-west-2"),
    ]

    # Injeção de dependências
    aws_client = AwsCliClient()
    publisher = SqsPublisher(queue_name="functions-data-queue")
    service = DescribeFunctionsService(aws_client=aws_client, publisher=publisher)

    # Execução do caso de uso
    service.execute(accounts)

    print("[END] Lambda handler finalizado")


if __name__ == "__main__":
    lambda_handler()
