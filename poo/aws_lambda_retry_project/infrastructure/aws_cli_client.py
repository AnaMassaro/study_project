import random
import time

from domain.entities import AWSAccount
from domain.ports.aws_client_port import AWSClientPort
from exceptions.errors import ThrottleError
from utils.retry import retry


class AwsCliClient(AWSClientPort):
    @retry(attempts=3, delay=1.5, exception_types=(ThrottleError,))
    def describe_functions(self, account: AWSAccount) -> list[dict]:
        print(f"[AWS CLI] Rodando describe-functions para {account.account_id} na região {account.region}")

        # Simulando 1 em cada 3 chamadas sendo bloqueada (throttle)
        if random.random() < 0.33:
            raise ThrottleError("ThrottlingException: Rate exceeded")

        # Retorno simulado
        return [
            {"FunctionName": "process-data", "Runtime": "python3.9"},
            {"FunctionName": "send-emails", "Runtime": "nodejs16.x"},
            {"FunctionName": "generate-report", "Runtime": "python3.9"},
        ]
