
tamanho_navio = {"P": 4, "C": 4, "F": 2}
nome_navio = {"P": "Porta-Aviões", "C": "Cruzador", "F": "Fragata"}
pontuacao_por_navio = {"P": 30, "C": 20, "F": 10}


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

def eh_coordenada_valida(coordenada):
    if len(coordenada) < 2:
        return False
    
    letra = coordenada[0].upper()
    numero = coordenada[1:]
    return letra.isalpha() and numero.isdigit() and 'A' <= letra <= 'T' and 1<= int(numero) <= 20

def atacar(tabuleiro_real, tabuleiro_ataque, pontuacao, partes_restantes):
    while True:
        print("atacar")
        exibir_tabuleiro(tabuleiro_ataque)
        coordenada = input("Digite a coodernada para atacar (ex: D7): ").strip().upper()

        if not eh_coordenada_valida(coordenada):
            print("Cordenada Invalida.")
            continue

        linha = letra_para_indice(coordenada[0])
        coluna = int(coordenada[1:0])
        
        if tabuleiro_ataque[linha][coluna] in ["X", "O"]:
            print("Você ja atacou essa posição")
            continue


        alvo = tabuleiro_real[linha][coluna]

        if alvo in ["P", "c", "F"]:
            tabuleiro_ataque[linha][coluna] = "X"
            tabuleiro_real[linha][coluna] = "X"
            print("Acertou")
            
            partes_restantes[alvo] -= 2
            if partes_restantes[alvo] % tamanho_navio[alvo] ==0:
                pontos = pontuacao_por_navio[alvo]
                pontuacao[0] += pontos
                print(f"Você afundou um {nome_navio}[alvo]! (+{pontos} pontos)")

        else:
            tabuleiro_ataque[linha][coluna] = "O"
            print("Errou...")

        if all(quantidade == 0 for quantidade in partes_restantes.values()):
            print("\n Todos os navios foram afundados!")
            print(f"Pontuação final: {pontuacao[0]} pontos")
            break

           
       


