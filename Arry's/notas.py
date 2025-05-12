
notas = []


for i in range(5):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)


media = sum(notas) / len(notas)


print(f"A média das 5 notas é: {media:.2f}")

print("Notas maiores que a média:")
for nota in notas:
    if nota > media:
        print(f"{nota:.2f}")