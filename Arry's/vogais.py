texto = input("Digite uma frase: ")

vogais = "aeiouAEIOU"
contagem_vogais = 0
contagem_espacos = 0


for caractere in texto:
    if caractere in vogais:
        contagem_vogais += 1
    if caractere == " ":
        contagem_espacos += 1


print("Texto analisado:", texto)
print("Número de vogais:", contagem_vogais)
print("Número de espaços:", contagem_espacos)