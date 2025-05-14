# Criando uma matriz 5x5 com entrada do usuário
matriz = []

print("Digite os valores da matriz 5x5 (linha por linha):")
for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input(f"Elemento [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Imprimindo a matriz em ordem reversa (de trás para frente)
print("\nMatriz em ordem inversa:")
for i in range(4, -1, -1):       # Linhas de 4 a 0
    for j in range(4, -1, -1):   # Colunas de 4 a 0
        print(matriz[i][j], end=' ')
    print()  # Nova linha
