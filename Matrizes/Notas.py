# Criando a matriz de notas: 3 alunos, 4 notas cada
notas = [
    [7.5, 8.0, 6.5, 9.0],  # Aluno 1
    [5.0, 6.0, 7.0, 8.0],  # Aluno 2
    [9.0, 8.5, 10.0, 7.5]  # Aluno 3
]


for i in range(3):  # Para cada aluno
    soma = sum(notas[i])
    media = soma / 4
    print(f"Média do Aluno {i+1}: {media:.2f}")