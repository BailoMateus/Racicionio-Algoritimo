
# Criação do tabuleiro 20x20
def criar_tabuleiro():
    return [["~" for _ in range(20)] for _ in range(20)]

def exibir_tabuleiro(tabuleiro):
    
    cabecalho = "   " + " ".join([str(i + 1).rjust(2) for i in range(20)])
    print(cabecalho)

    for linha_index in range(20):
        letra_linha = chr(65 + linha_index)
        conteudo_linha = ""
        for coluna_index in range(20):
            conteudo_linha += tabuleiro[linha_index][coluna_index].rjust(2) + " "
        print(f"{letra_linha}  {conteudo_linha.strip()}")

# Teste inicial
#tabuleiro = criar_tabuleiro()
#exibir_tabuleiro(tabuleiro)

def letra_para_indice(letra):
    return ord(letra.upper()) - 65

def posicao_valida(tabuleiro, linha, coluna_inicial, tamanho_navio):
    if coluna_inicial + tamanho_navio > 20:
        return False
    for i in range(tamanho_navio):
        if tabuleiro[linha][coluna_inicial + i] != "~":
            return False
    return True

