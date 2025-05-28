def calcular_comissao(valor_venda, percentual_comissao):
    comissao = valor_venda * (percentual_comissao / 100)
    return comissao

# Entrada de dados
valor_venda = float(input("Digite o valor da venda (em reais): "))
percentual_comissao = float(input("Digite o percentual da comissão (%): "))

# Cálculo da comissão
ganho = calcular_comissao(valor_venda, percentual_comissao)

# Saída do resultado
print(f"Ganho do vendedor: R$ {ganho:.2f}")
