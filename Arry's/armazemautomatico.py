import random


precos = [round(random.uniform(1.0, 100.0), 2) for _ in range(100)]          # preços entre R$1,00 e R$100,00
quantidades = [random.randint(0, 50) for _ in range(100)]                   # quantidade entre 0 e 50 unidades


faturamento = 0
for i in range(100):
    faturamento += precos[i] * quantidades[i]


print("Resumo das 10 primeiras mercadorias:")
for i in range(10):
    print(f"Mercadoria {i+1}: Preço = R$ {precos[i]:.2f}, Vendidos = {quantidades[i]}")


print(f"\nFaturamento mensal total do armazém: R$ {faturamento:.2f}")
