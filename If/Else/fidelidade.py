valor_entrada = 30.00


quantidade_ingressos = int(input("Quantos ingressos deseja comprar? "))


desconto_fidelidade = float(input("Informe o seu desconto de fidelidade (0 a 100%): "))


if 0 <= desconto_fidelidade <= 100:

        valor_desconto_fidelidade = (desconto_fidelidade / 100) * valor_entrada
else:
            print("Desconto inválido. O valor deve estar entre 0 e 100%.")
            valor_desconto_fidelidade = 0


tem_estacionamento = int(input("Você tem ticket de estacionamento para descontar? (sim = 1/não = 2): "))

desconto_estacionamento = 0

if tem_estacionamento == 1:

    desconto_estacionamento = float(input("Qual o valor do ticket de estacionamento? R$ "))


    total_ingressos = quantidade_ingressos * valor_entrada
    total_desconto = (valor_desconto_fidelidade * quantidade_ingressos) + desconto_estacionamento
    total_a_pagar = total_ingressos - total_desconto
    print(f"O valor total a ser pago é: R$ {total_a_pagar:.2f}")

else:
    total_ingressos = quantidade_ingressos * valor_entrada
    total_desconto = valor_desconto_fidelidade * quantidade_ingressos
    total_a_pagar = total_ingressos - total_desconto
    print(f"O valor total a ser pago é: R$ {total_a_pagar:.2f}")