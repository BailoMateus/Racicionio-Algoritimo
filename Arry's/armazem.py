

precos = []
quantidades = []


print("Digite os preços das 100 mercadorias:")
for i in range(100):
    preco = float(input(f"Preço da mercadoria {i+1}: "))
    precos.append(preco)


print("\nDigite a quantidade vendida de cada mercadoria:")
for i in range(100):
    qtd = int(input(f"Quantidade vendida da mercadoria {i+1}: "))
    quantidades.append(qtd)


faturamento = 0
for i in range(100):
    faturamento += precos[i] * quantidades[i]


print(f"\nFaturamento mensal do armazém: R$ {faturamento:.2f}")
