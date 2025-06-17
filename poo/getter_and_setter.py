class Payment:
    def __init__(self, amount):
        # Nós usamos dois nomes diferentes (com e sem underline) para evitar loop infinito:
        # se o setter usasse `self.amount = value` dentro dele mesmo, ele se chamaria de novo.
        self._amount = None      # atributo interno (armazenado diretamente)
        self.amount = amount     # chama o setter, que faz validação antes de definir o valor

    @property
    def amount(self):
        # Esse método é chamado automaticamente quando fazemos: p.amount
        return self._amount

    @amount.setter
    def amount(self, value):
        # Esse método é chamado automaticamente quando fazemos: p.amount = 200
        # Aqui podemos validar o valor antes de aceitar
        if value < 0:
            raise ValueError("Valor não pode ser negativo.")
        self._amount = value

# Exemplo de uso
p = Payment(100)
print(p.amount)       # ✅ Chama o getter → imprime: 100

p.amount = 200        # ✅ Chama o setter → valor atualizado para 200
print(p.amount)       # ✅ Chama o getter → imprime: 200

p.amount = -2         # ❌ Chama o setter → ValueError: Valor não pode ser negativo.
print(p.amount)       # Esta linha não será executada por causa do erro acima
