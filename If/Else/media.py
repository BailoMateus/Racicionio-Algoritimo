nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a terceira nota: '))
print("As suas notas são:", nota1, nota2, nota3, nota4)

tempo_materia = float(input("Digite quantas horas aula tem a sua materia:"))
tempo_presença = float(input("Digite qual a sua presença nessa materias em horas:"))

minimo_presença = tempo_materia * 0.75
media = (nota1 + nota2 + nota3 + nota4)/4

if media >= 7 and tempo_presença >= minimo_presença:
    print("Você esta Aprovado")
elif media >= 5 and tempo_presença >= minimo_presença:
    print("Você esta de Recuperação")
elif media < 5 and tempo_presença < minimo_presença:
    print("Você esta Reprovado por Nota e Faltas")
elif tempo_presença < minimo_presença:
    print("Você esta Reprovado por Faltas")
elif media < 5:
    print("Você esta Reprovado por Nota")