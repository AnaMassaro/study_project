# 🔁 Lambda Retry Handler – Arquitetura Hexagonal em Python

Este projeto simula uma função **AWS Lambda** profissional com código limpo, separação clara de responsabilidades, arquitetura hexagonal e práticas avançadas de Python, como getter/setter, mixins, e tratamento de exceções.

---

## 📌 O que essa Lambda faz?

1. Recebe uma lista de contas AWS
2. Executa um `describe-functions` (simulado) via AWS CLI para cada conta
3. Agrupa e formata os dados obtidos
4. Publica os dados agrupados em uma fila SQS
5. Faz **retry automático** em caso de throttling

---

## 🧱 Estrutura de Pastas (Arquitetura Hexagonal)

```
project-root/
│
├── domain/
│   ├── entities.py            ← Entidades com regras e validações
│   ├── ports/
│   │   ├── aws_client_port.py ← Interface (port) para leitura de dados AWS
│   │   └── publisher_port.py  ← Interface (port) para envio dos dados
│   └── mixins.py              ← Comportamentos reutilizáveis (validação)
│
├── infrastructure/
│   ├── aws_cli_client.py      ← Adapter que simula chamadas AWS CLI com retry
│   └── sqs_publisher.py       ← Adapter que simula envio de mensagem SQS
│
├── services/
│   └── describe_functions_service.py ← Caso de uso principal
│
├── exceptions/
│   └── errors.py              ← Exceções específicas (ex: `ThrottleError`)
│
├── utils/
│   └── retry.py               ← Decorador de retry reutilizável
│
└── lambda_function.py         ← Entrypoint principal da função Lambda
```

---

## 🧠 Conceitos Aplicados

### ✅ Arquitetura Hexagonal (Ports and Adapters)

- **Entidade `AWSAccount`**: objeto rico em regras de validação (ex: `account_id`, `region`)
- **Ports (interfaces)**: `AwsClientPort` e `PublisherPort` definem contratos esperados
- **Adapters reais**: `AwsCliClient` e `SqsPublisher` implementam esses contratos
- **Caso de uso**: `DescribeFunctionsService` orquestra o fluxo, usando apenas os ports

**Benefício**: o domínio não depende de boto3, subprocess ou detalhes da AWS — isso garante testabilidade, flexibilidade e clareza.

---

### ✅ Programação Orientada a Objetos (POO)

- **Encapsulamento**: atributos protegidos (`_account_id`)
- **Getter/Setter**: com `@property` para aplicar regras em tempo de atribuição
- **Mixins**: comportamentos reutilizáveis desacoplados (ex: validação)
- **Composição**: o caso de uso recebe clientes via injeção de dependência
- **Interfaces com `Protocol`**: typing avançado sem acoplamento

---

### ✅ Mixins

O `AccountValidationMixin` define validações reaproveitáveis, como:

- Formato de `account_id`
- Nome válido de região AWS

**Por que usar mixins?**
- Código limpo e reutilizável
- Substitui superclasses com responsabilidades demais
- Permite combinar lógica reutilizável sem acoplamento

---

### ✅ Retry Automático

Decorador `@retry(...)` no `AwsCliClient`, que:

- Reexecuta chamadas com `subprocess` simuladas
- Captura a exceção `ThrottleError`
- Aplica tempo de espera exponencial (padrão de mercado)

---

### ✅ Exceções Específicas

- `ThrottleError` define um erro específico para ser tratado com retry
- Mesmo "vazia", é importante para diferenciar falhas por tipo

---

## ✅ Boas práticas adotadas

| Prática                          | Onde aplicamos                                  |
|----------------------------------|--------------------------------------------------|
| Separação por camadas            | Arquitetura hexagonal (`domain`, `infra`, etc.) |
| Tipagem forte                    | Uso de `Protocol`, `@property`, parâmetros       |
| Validação defensiva              | Mixins e setters                                 |
| Encapsulamento                   | `_atributo + getter/setter`                      |
| Retry reutilizável               | Decorador `@retry`                               |
---

## 💡 Objetivo do projeto

Este projeto foi desenvolvido com foco didático e profissional, para praticar:

- Arquitetura limpa e escalável para Lambdas AWS
- Python moderno, expressivo e seguro
- Boas práticas de código