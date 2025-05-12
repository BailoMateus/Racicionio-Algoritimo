
vetor = []


for i in range(10):
    numero = int(input(f"Digite o número na posição {i+1}: "))
    vetor.append(numero)


elemento = int(input("Digite o número que deseja localizar no vetor: "))


if elemento in vetor:
    posicao = vetor.index(elemento)  # Encontrando a posição do elemento
    print(f"O número {elemento} está na posição {posicao} do vetor.")
else:
    print("Não está no vetor.")