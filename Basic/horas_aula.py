horas_aula = float(input('digite quantas horas aula tem sua materia: '))

numero_presença = horas_aula * 0.758

falta_max = horas_aula - numero_presença


print('seu numero maximo de faltas é:', falta_max, 'horas aula')