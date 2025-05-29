# 🧩 Observer Pattern em Lambda AWS - Estudo de Caso

Este projeto demonstra o uso do **padrão de projeto Observer** no contexto de uma função **AWS Lambda** que reage a um evento do **S3** (quando um arquivo é enviado).

---

## 🔍 O que é o padrão Observer?

O padrão **Observer** é um padrão comportamental que permite que objetos (chamados *observers*) sejam notificados automaticamente sempre que outro objeto (o *subject*) sofre alguma alteração ou evento.

É muito usado em arquiteturas **event-driven** (orientadas a eventos), como as que encontramos em ambientes **serverless** com AWS.

---

## 📦 Cenário simulado neste projeto

Quando um arquivo é enviado para o S3:

1. A Lambda é disparada.
2. A Lambda notifica vários *observers* que reagem ao evento de forma independente:
   - Processam o conteúdo do arquivo.
   - Gravam os dados em um banco de dados.
   - Enviam uma mensagem para uma fila SQS.
   - (Fácil de estender para: logs, Slack, e-mail, etc.)

---

## ✅ Benefícios do uso do Observer

- **Desacoplamento:** A Lambda não precisa saber o que cada ação faz.
- **Extensibilidade:** Novas ações são adicionadas sem alterar a lógica principal.
- **Organização:** Cada classe tem uma única responsabilidade (SRP).
- **Facilidade de testes:** Cada parte pode ser testada isoladamente.
- **Simulação de arquitetura event-driven:** Tudo dentro de uma única função Lambda.

---

## ✨ Exemplo realista de aplicação

Este padrão é ideal para situações como:

- Automatizações reativas baseadas em eventos (ex: novo arquivo, nova mensagem, nova entrada no banco).
- Pipelines de processamento modularizados.
- Lambdas que disparam múltiplas ações de forma desacoplada.

---

## 💡 Para estudar futuramente

Se quiser revisar o padrão Observer, lembre-se:

> "Eu disparo um evento genérico. Cada parte interessada escuta e reage do seu jeito."

Esse projeto mostra como esse princípio se aplica de forma limpa e prática em um cenário real de backend.
