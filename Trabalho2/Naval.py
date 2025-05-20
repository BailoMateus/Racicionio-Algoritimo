
# Cria uma matriz 20x20 preenchida com "~"
def criar_tabuleiro():
    return [["~" for _ in range(20)] for _ in range(20)]

def exibir_tabuleiro(tabuleiro):
    # Cabeçalho com os números das colunas
    cabecalho = "   " + " ".join([str(i + 1).rjust(2) for i in range(20)])
    print(cabecalho)
    # Cada linha com sua letra (A até T) e o conteúdo das células
    for linha_index in range(20):
        letra_linha = chr(65 + linha_index) # Converte 0 → A, 1 → B, ..., 19 → T
        conteudo_linha = ""
        for coluna_index in range(20):
            conteudo_linha += tabuleiro[linha_index][coluna_index].rjust(2) + " "
        print(f"{letra_linha}  {conteudo_linha.strip()}")

# Teste inicial
tabuleiro = criar_tabuleiro()
exibir_tabuleiro(tabuleiro)

# Converte letra (ex: "A") para índice (0 a 19)
def letra_para_indice(letra):
    return ord(letra.upper()) - 65

# Verifica se o navio pode ser colocado na posição escolhida
def posicao_valida(tabuleiro, linha, coluna_inicial, tamanho_navio):
    if coluna_inicial + tamanho_navio > 20:
        return False # Passaria do limite do tabuleiro
    for i in range(tamanho_navio):
        if tabuleiro[linha][coluna_inicial + i] != "~":
            return False # Já tem navio aqui
    return True



