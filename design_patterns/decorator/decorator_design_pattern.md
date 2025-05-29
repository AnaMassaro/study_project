# Decorator Pattern – Projeto Lambda com Logging e Exception Handling

Este projeto demonstra a aplicação do **Decorator Pattern** no contexto de uma função AWS Lambda, adicionando funcionalidades de **log** e **tratamento de exceções** sem modificar a lógica principal da função.

## 🧩 O que é o Decorator Pattern?

O **Decorator Pattern** é um padrão estrutural que permite adicionar responsabilidades a objetos de forma dinâmica. Em Python, usamos funções que "embrulham" outras funções, adicionando comportamentos antes e/ou depois da execução da função original.

## 🚀 O que foi implementado aqui?

Neste exemplo, temos uma função `lambda_handler` que simula o processamento de um arquivo. Decorators foram aplicados a ela para:

- **Logging**: indicar quando a função começou e terminou.
- **Tratamento de Exceções**: capturar qualquer erro que ocorra durante a execução e evitar que ele quebre a aplicação.

Isso foi feito sem alterar a lógica central de negócio, que é o processamento do arquivo.

## ✅ Benefícios do uso do padrão

- **Separação de responsabilidades**: a lógica de negócio fica limpa, enquanto logging e exception handling são isolados.
- **Reutilização**: os decorators podem ser aplicados em qualquer outra função da aplicação.
- **Flexibilidade**: é fácil adicionar, remover ou reorganizar comportamentos extras.
- **Leitura clara**: o uso de `@decorator_name` mostra explicitamente quais responsabilidades adicionais estão associadas à função.

## 📌 Exemplo de uso

```python
@logging_decorator
@exception_decorator
def lambda_handler(event, context):
    ...
```

> ⚠️ **A ordem dos decorators é importante**: o mais próximo da função é aplicado primeiro.

---

Este padrão é extremamente útil em projetos reais para lidar com:

- 📋 *Log*
- 🔒 *Autenticação*
- 🚀 *Cache*
- ✅ *Validação*
- 📊 *Métricas*
- 🔁 *Retries*

Entre outros cenários comuns do dia a dia de desenvolvimento.