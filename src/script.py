import time
import functools

# Decorator para medir tempo
def medir_tempo(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fim = time.time()
        print(f"⏱ Tempo de execução: {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

# Lista de produtos (nome, preço)
produtos = [
    ("Celular", 1500),
    ("Carregador", 80),
    ("Notebook", 3500),
    ("Capa", 30),
    ("Mouse", 120),
]

# 1️⃣ map: deixar os nomes dos produtos em minúsculas
# onde p[0] é o nome e p[1] é o preço
produtos_formatados = list(map(lambda p: (p[0].lower(), p[1]), produtos))

# 2️⃣ filter: pegar só os produtos mais caros (preço > 100)
produtos_caros = list(filter(lambda p: p[1] > 100, produtos_formatados))

# 3️⃣ sorted: ordenar por preço (do menor para o maior)
# se quiser do maior para o menor, basta inverter a ordem, adicionando o reverse=True, assim:
# sorted(produtos_caros, key=lambda p: p[1], reverse=True)
ordenados_por_preco = sorted(produtos_caros, key=lambda p: p[1])

# 4️⃣ partial: criar uma função que aplica 10% de desconto
def aplicar_desconto(produto, percentual):
    nome, preco = produto
    novo_preco = round(preco * (1 - percentual / 100), 2)
    return (nome, novo_preco)

# Criando uma função com 10% de desconto fixo
aplicar_10_porcento = functools.partial(aplicar_desconto, percentual=10)

# 5️⃣ decorator em ação: medindo tempo para aplicar desconto
@medir_tempo
def processar_produtos(lista):
    return list(map(aplicar_10_porcento, lista))

# Execução
print("\n🛍 Produtos formatados e caros (ordenados):")
for nome, preco in ordenados_por_preco:
    print(f"- {nome} → R$ {preco:.2f}")

print("\n💸 Aplicando desconto de 10%:")
com_desconto = processar_produtos(ordenados_por_preco)

for nome, preco in com_desconto:
    print(f"- {nome} → R$ {preco:.2f}")
