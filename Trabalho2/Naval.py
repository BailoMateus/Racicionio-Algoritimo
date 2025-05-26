#---------------------------------------------------------------------------------------------------------------------------------
# Batalha Naval - PjBL2
# Alunos: Mateus Luiz Bailo, Icaro Nunes, Bruno Hinz
#---------------------------------------------------------------------------------------------------------------------------------


# Cria uma matriz 20x20 preenchida com "~" (representa água)
def criar_tabuleiro():
    return [["~" for _ in range(20)] for _ in range(20)]

# Exibe o tabuleiro com cabeçalho numérico e letras A-T para facilitar visualização
def exibir_tabuleiro(tabuleiro):
    cabecalho = "   " + " ".join([str(i + 1).rjust(2) for i in range(20)])
    print(cabecalho)
    for linha_index in range(20):
        letra_linha = chr(65 + linha_index)  # A, B, C, ..., T
        conteudo_linha = ""
        for coluna_index in range(20):
            conteudo_linha += tabuleiro[linha_index][coluna_index].rjust(2) + " "
        print(f"{letra_linha}  {conteudo_linha.strip()}")

# Converte uma letra (ex: "B") em índice de linha (ex: 1)
def letra_para_indice(letra):
    return ord(letra.upper()) - 65

# Verifica se o navio cabe na posição desejada e se não há sobreposição
def posicao_valida(tabuleiro, linha, coluna_inicial, tamanho_navio):
    if coluna_inicial + tamanho_navio > 20:
        return False  # O navio ultrapassaria o limite da linha
    for i in range(tamanho_navio):
        if tabuleiro[linha][coluna_inicial + i] != "~":
            return False  # Já há outro navio ocupando a posição
    return True

# Permite que o jogador posicione os navios manualmente
def posicionar_navio(tabuleiro, nome, quantidade, tamanho, simbolo):
    print(f"\n== Posicionamento de {nome} ({quantidade} navios de {tamanho} células) ==")
    for numero_navio in range(quantidade):
        while True:
            print(f"\nTabuleiro atual:")
            exibir_tabuleiro(tabuleiro)  # Mostra o tabuleiro atualizado a cada inserção

            print(f"\nPosicione o {nome} #{numero_navio + 1}")
            entrada = input("Digite a posição inicial (ex: A5): ").strip().upper()

            # Verifica se a entrada está no formato válido
            if len(entrada) < 2 or not entrada[0].isalpha() or not entrada[1:].isdigit():
                print("Formato inválido. Use letra + número. Ex: B10")
                continue

            linha = letra_para_indice(entrada[0])
            coluna = int(entrada[1:]) - 1

            # Verifica se a posição está dentro dos limites
            if not (0 <= linha < 20 and 0 <= coluna < 20):
                print("Posição fora do tabuleiro!")
                continue

            # Verifica se o navio pode ser posicionado ali
            if not posicao_valida(tabuleiro, linha, coluna, tamanho):
                print("Navio não cabe aqui ou sobrepõe outro.")
                continue

            # Posiciona o navio horizontalmente
            for deslocamento in range(tamanho):
                tabuleiro[linha][coluna + deslocamento] = simbolo
            break

# Valida coordenadas de entrada do jogador (ex: A10, D3)
def eh_coordenada_valida(coordenada):
    if len(coordenada) < 2:
        return False
    letra = coordenada[0].upper()
    numero = coordenada[1:]
    return letra.isalpha() and numero.isdigit() and 'A' <= letra <= 'T' and 1 <= int(numero) <= 20

# Associa o símbolo do navio ao seu índice nas listas
def simbolo_para_indice(simbolo):
    if simbolo == "P":
        return 0  # Porta-Aviões
    elif simbolo == "C":
        return 1  # Cruzador
    elif simbolo == "F":
        return 2  # Fragata
    return -1  # Água ou posição vazia

# Fase de ataque: jogador tenta acertar navios
def atacar(tabuleiro_real, tabuleiro_ataque, pontuacao, partes_restantes, tamanhos_navios, nomes_navios, pontuacoes_navios):
    while True:
        print("\n======= ATAQUE =======")
        exibir_tabuleiro(tabuleiro_ataque)  # Mostra tabuleiro de ataques
        coordenada = input("Digite a coordenada para atacar (ex: D7): ").strip().upper()

        # Verifica se a coordenada é válida
        if not eh_coordenada_valida(coordenada):
            print("Coordenada inválida.")
            continue

        linha = letra_para_indice(coordenada[0])
        coluna = int(coordenada[1:]) - 1

        # Verifica se já foi atacado
        if tabuleiro_ataque[linha][coluna] in ["X", "O"]:
            print("Você já atacou essa posição.")
            continue

        alvo = tabuleiro_real[linha][coluna]
        indice = simbolo_para_indice(alvo)

        # Acerto
        if indice != -1:
            tabuleiro_ataque[linha][coluna] = "X"
            tabuleiro_real[linha][coluna] = "X"
            print("ACERTOU!")

            partes_restantes[indice] -= 1
            # Verifica se o navio foi afundado (todas as partes atingidas)
            if partes_restantes[indice] % tamanhos_navios[indice] == 0:
                pontuacao[0] += pontuacoes_navios[indice]
                print(f"Você afundou um {nomes_navios[indice]}! (+{pontuacoes_navios[indice]} pontos)")
        else:
            tabuleiro_ataque[linha][coluna] = "O"
            print("Errou...")

        # Fim do jogo: todos os navios afundados
        if all(restantes == 0 for restantes in partes_restantes):
            print("\n Todos os navios foram afundados!")
            print(f" Pontuação final: {pontuacao[0]} pontos")
            break

# Gera um tabuleiro com navios posicionados automaticamente para testes
def gerar_tabuleiro_teste():
    tabuleiro = criar_tabuleiro()

    # Porta-Aviões (3 de 4 células)
    tabuleiro[0][0:4] = ["P"] * 4
    tabuleiro[2][5:9] = ["P"] * 4
    tabuleiro[4][10:14] = ["P"] * 4

    # Cruzadores (4 de 3 células)
    tabuleiro[6][0:3] = ["C"] * 3
    tabuleiro[7][5:8] = ["C"] * 3
    tabuleiro[8][10:13] = ["C"] * 3
    tabuleiro[9][15:18] = ["C"] * 3

    # Fragatas (5 de 2 células)
    tabuleiro[11][0:2] = ["F"] * 2
    tabuleiro[12][3:5] = ["F"] * 2
    tabuleiro[13][6:8] = ["F"] * 2
    tabuleiro[14][9:11] = ["F"] * 2
    tabuleiro[15][12:14] = ["F"] * 2

    return tabuleiro

# Função principal do jogo
def main():
    print("Bem-vindo ao Batalha Naval (Versão Texto)\n")

    # Informações dos navios
    tamanhos_navios = [4, 3, 2]
    quantidades_navios = [3, 4, 5]
    simbolos_navios = ["P", "C", "F"]
    nomes_navios = ["Porta-Aviões", "Cruzador", "Fragata"]
    pontuacoes_navios = [30, 20, 10]
    partes_restantes = [
        quantidades_navios[0] * tamanhos_navios[0],
        quantidades_navios[1] * tamanhos_navios[1],
        quantidades_navios[2] * tamanhos_navios[2]
    ]

    # Menu de escolha do modo
    print("Escolha o modo de posicionamento dos navios:")
    print("1 - Posicionar manualmente")
    print("2 - Usar tabuleiro pronto para teste")
    escolha = input("Sua escolha: ").strip()

    tabuleiro_ataque = criar_tabuleiro()

    if escolha == "2":
        # Gera tabuleiro com navios posicionados automaticamente
        tabuleiro_real = gerar_tabuleiro_teste()
        print("Tabuleiro de teste gerado automaticamente!")
        exibir_tabuleiro(tabuleiro_real)  # Mostra navios no modo teste
    else:
        # Posicionamento manual
        tabuleiro_real = criar_tabuleiro()
        for i in range(3):
            posicionar_navio(tabuleiro_real, nomes_navios[i], quantidades_navios[i], tamanhos_navios[i], simbolos_navios[i])

    pontuacao = [0]  # Usamos lista para poder alterar dentro da função
    atacar(tabuleiro_real, tabuleiro_ataque, pontuacao, partes_restantes, tamanhos_navios, nomes_navios, pontuacoes_navios)

# Inicia o programa
if __name__ == "__main__":
    main()
