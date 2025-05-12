
sorteados = []
apostados = []


print("Digite os 6 números sorteados:")
for i in range(6):
    numero = int(input(f"Número sorteado {i+1}: "))
    sorteados.append(numero)


print("Digite os 6 números apostados:")
for i in range(6):
    numero = int(input(f"Número apostado {i+1}: "))
    apostados.append(numero)


acertos = 0
for i in range(6):
    if sorteados[i] == apostados[i]:
        acertos += 1

print("\nNúmeros sorteados: ", sorteados)
print("Números apostados: ", apostados)

print(f"Você acertou {acertos} número(s).")
