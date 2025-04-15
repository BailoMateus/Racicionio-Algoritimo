valor_diaria = 100.00


alugar_carro = int(input("Você deseja alugar o carro? Digite 1 para 'sim' ou 2 para 'não': ")) == 1


if alugar_carro:
    dias_locados = int(input("Digite o número de dias você deseja ficar com o carro: "))
    valor_total = dias_locados * valor_diaria
    print("O valor a ser pago pela locação é: R$:", valor_total)
else:
    print("Você escolheu não alugar o carro.")