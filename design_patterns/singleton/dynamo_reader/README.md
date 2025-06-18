# DynamoDB Reader Lambda 📦

Este projeto é uma função Lambda construída com arquitetura limpa, padrão Singleton e estrutura profissional, que simula a leitura de dados de uma partição em uma tabela DynamoDB. O objetivo é mostrar como construir uma Lambda **limpa, testável, desacoplada e fácil de manter**, aplicando práticas como **POO, arquitetura hexagonal e injeção de dependências**.

---

## ✅ Visão Geral da Arquitetura

A arquitetura segue os princípios da **Arquitetura Hexagonal (Ports and Adapters)**, combinada com separação de responsabilidades clara inspirada no **DDD (Domain-Driven Design)**.

![Arquitetura Lambda DynamoDB](./A_flowchart_diagram_depicts_the_architecture_of_a_.png)

---

## 📁 Estrutura de Pastas

```
.
├── lambda_function.py                  # Entry point da AWS Lambda
├── application/
│   ├── get_partition_items.py          # Caso de uso (use case) para leitura de partição
│   └── format_partition_item.py        # Formatação e normalização dos dados lidos
├── domain/
│   └── ports/
│       └── dynamo_port.py              # Interface que define o contrato de leitura no Dynamo
├── infrastructure/
│   └── dynamo_client.py                # Implementação real (simulada) do acesso ao Dynamo
├── shared/
│   ├── singleton.py                    # Metaclasse Singleton reutilizável e thread-safe
│   └── exceptions.py                   # Exceções personalizadas
```

---

## 🧩 Detalhamento das Camadas

### `lambda_function.py` (Driving Adapter)
Ponto de entrada da Lambda. Recebe o evento com o `partition_key`, instancia os objetos, executa o caso de uso e retorna os dados formatados.

### `application/` (Application Layer)
Responsável por orquestrar as ações da aplicação. Contém o caso de uso (`get_partition_items`) e o formatador (`format_partition_item`) dos dados retornados.

### `domain/` (Domain Layer)
Contém os contratos da aplicação — neste caso, a interface `DynamoPort`, que define o que a infraestrutura precisa cumprir.

### `infrastructure/` (Driven Adapter)
Implementa a lógica real de acesso ao banco DynamoDB. O `DynamoClient` é um singleton e simula uma leitura real.

### `shared/` (Utilitários comuns)
Contém ferramentas reutilizáveis como:
- `singleton.py`: Metaclasse Singleton thread-safe
- `exceptions.py`: Exceção específica para ausência de partition_key

---

## ♻️ Uso do Singleton

O `DynamoClient` foi implementado como um Singleton utilizando uma **metaclasse (`SingletonMeta`)**.

### ✨ Benefícios dessa escolha:
- Garante que apenas **uma instância** de client Dynamo seja criada (ótimo para reuso e performance)
- Evita recriação em cada chamada da Lambda
- Pronto para uso thread-safe em ambientes concorrentes

---

## 🧪 Como testar localmente

```bash
python lambda_function.py
```

A função simula a execução da Lambda com um `event` de exemplo e imprime os dados no console.

---

## 🚀 Conclusão

Este projeto serve como base para funções Lambda organizadas, desacopladas e escaláveis. Ele demonstra:
- Boas práticas de design e organização de código
- Arquitetura hexagonal aplicada em um cenário real
- Uso de Singleton com metaclasses
- Aplicação clara dos princípios de POO em Python

Você pode expandir para usar Dynamo real (`boto3`), adicionar SQS, observabilidade, testes automatizados, etc.

---

**Construa código profissional. Não scripts.** 😎