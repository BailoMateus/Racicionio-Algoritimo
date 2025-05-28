def calcular_digito(cpf_parcial, pesos):
    soma = 0
    for i in range(len(cpf_parcial)):
        soma += int(cpf_parcial[i]) * pesos[i]
    resto = soma % 11
    digito = 11 - resto
    if digito > 9:
        digito = 0
    return digito

def validar_cpf(cpf):
    # Verifica se o CPF tem exatamente 11 dígitos numéricos
    if len(cpf) != 11 or not cpf.isdigit():
        return False

    # Cálculo dos dígitos verificadores
    pesos1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    d10 = calcular_digito(cpf[:9], pesos1)

    pesos2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    d11 = calcular_digito(cpf[:9] + str(d10), pesos2)

    return cpf[-2:] == f"{d10}{d11}"

# Entrada
cpf = input("Digite o CPF (apenas os 11 números, sem pontos ou traços): ")

# Verificação
if not cpf.isdigit() or len(cpf) != 11:
    print("ERRO: CPF deve conter exatamente 11 números, sem pontos ou traços!")
else:
    if validar_cpf(cpf):
        print("CPF VÁLIDO!")
    else:
        print("CPF INVÁLIDO!")

