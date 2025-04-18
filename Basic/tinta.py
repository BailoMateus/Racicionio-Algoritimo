print('Insira os dados nescassarios para podermos fazer o calculo')
altura_cilindro = float(input('Digite a altura do seu Cilindro em metros: '))
raio_cilindro = float(input('Digite o raio do seu Cilindro em metros:'))

base_cilindro = (3.14 * raio_cilindro**2)
area_lateral_cilindro = (2 * 3.14 * raio_cilindro * altura_cilindro)
area_total_cilindro = base_cilindro + area_lateral_cilindro

lata_tinta = 50.00
quantidade_tinta_lata = 5.00
quantidade_tinta = 3.00

quantidade_litros = area_total_cilindro/quantidade_tinta

lata_total = quantidade_litros/quantidade_tinta_lata

custo_total = lata_total * lata_tinta

#print('O talta de latas nescassarias para pintar o cilindro é de:', lata_total, 'Latas. Com um custo de R$: ', custo_total)
print('O total de latas necessárias para pintar o cilindro é de: {:.2f} Latas. Com um custo de R$: {:.2f}'.format(lata_total, custo_total))