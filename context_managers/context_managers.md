# Gerenciadores de Contexto (Context Managers) em Python

## O que é um Gerenciador de Contexto?

Um **Gerenciador de Contexto** em Python é uma construção que permite configurar um recurso, utilizá-lo e depois garantir que ele seja liberado ou finalizado corretamente, mesmo que ocorram erros.

Normalmente usamos o `with` para isso:

```python
with contexto():
    # usar o recurso com segurança aqui
```

Quando entramos no bloco, o método `__enter__` é chamado, e ao sair do bloco (normalmente ou por uma exceção), o método `__exit__` é executado.

---

## Por que usar Gerenciadores de Contexto?

- **Gerenciamento automático de recursos:** arquivos, conexões de rede, sessões de banco, locks, etc., são abertos e fechados corretamente.  
- **Código mais limpo e seguro:** evita repetição de blocos try/finally.  
- **Segurança contra exceções:** recursos são liberados mesmo se houver erro dentro do bloco `with`.  
- **Melhor leitura e manutenção do código.**

---

## Como funciona?

Um gerenciador é uma classe (ou função) que implementa dois métodos:

- `__enter__(self)`: configura o recurso e retorna ele, se necessário.  
- `__exit__(self, exc_type, exc_val, exc_tb)`: realiza a limpeza e recebe informações sobre exceções, se ocorreram.

O valor retornado por `__exit__` controla o comportamento em caso de exceção:  
- Retornar `False` ou `None` (padrão) propaga a exceção para fora do `with`.  
- Retornar `True` suprime a exceção (ela não será levantada).

---

## Gerenciadores de Contexto vs Decorators

- **Gerenciadores de contexto** controlam a preparação e limpeza de recursos envolvendo um bloco de código (`with`).  
- **Decorators** envolvem uma função para modificar seu comportamento antes e depois da execução.

Ambos podem ser usados para setup/teardown, mas:

- Use **context managers** para controle flexível sobre blocos de código com múltiplas linhas.  
- Use **decorators** para modificar o comportamento de uma única função.

Exemplo:

```python
with open('arquivo.txt') as f:  
    dados = f.read()  # context manager  
```

versus

```python
@log_execucao  
def processar_dados():  
    pass  # decorator  
```

---

## Exemplo prático: gerenciando mensagens SQS em Lambda

Imagine que você quer garantir que uma mensagem da fila SQS só seja deletada se o processamento for concluído com sucesso. Usar um context manager facilita isso:

```python
class SQSMessageHandler:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        print("Starting to process message:", self.message['MessageId'])
        return self.message

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("Processing succeeded, deleting message:", self.message['MessageId'])
            # Simule a deleção da mensagem, ex: sqs_client.delete_message(...)
        else:
            print("Processing failed, message NOT deleted:", self.message['MessageId'])
        return False  # Propaga exceção se ocorreu

# Uso simulado dentro da lambda handler
def lambda_handler(event, context):
    for msg in event['Records']:
        with SQSMessageHandler(msg) as message:
            # Processa a mensagem aqui
            print("Processing message body:", message['Body'])
            # Se der erro aqui, a mensagem não será deletada
```
