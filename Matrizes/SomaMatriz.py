# Inicializando as matrizes
matriz1 = []
matriz2 = []
matriz_soma = []

# Leitura da primeira matriz
print("Digite os elementos da Matriz 1 (2x2):")
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Matriz1[{i}][{j}]: "))
        linha.append(valor)
    matriz1.append(linha)

# Leitura da segunda matriz
print("\nDigite os elementos da Matriz 2 (2x2):")
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Matriz2[{i}][{j}]: "))
        linha.append(valor)
    matriz2.append(linha)

# Soma das matrizes
for i in range(2):
    linha_soma = []
    for j in range(2):
        soma = matriz1[i][j] + matriz2[i][j]
        linha_soma.append(soma)
    matriz_soma.append(linha_soma)

# Exibindo a matriz resultante
print("\nMatriz Soma (Matriz1 + Matriz2):")
for i in range(2):
    for j in range(2):
        print(matriz_soma[i][j], end=' ')
    print()