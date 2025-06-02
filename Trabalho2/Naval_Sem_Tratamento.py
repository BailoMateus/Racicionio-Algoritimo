#---------------------------------------------------------------------------------------------------------------------------------
# Batalha Naval - PjBL2 - Raciocínio Algorítmico
# Alunos: Mateus Luiz Bailo, Icaro Nunes, Bruno Hinz
#---------------------------------------------------------------------------------------------------------------------------------

# Cria um tabuleiro 20x20 preenchido com "~", representando o mar (água)
def criar_tabuleiro():
    return [["~" for linha_tabuleiro in range(20)] for coluna_tabuleiro in range(20)]

# Exibe o tabuleiro formatado com letras (A-T) nas linhas e números (1-20) nas colunas
def exibir_tabuleiro(tabuleiro):
    cabecalho = "   " + " ".join([str(i + 1).rjust(2) for i in range(20)])
    print(cabecalho)
    for linha_index in range(20):
        letra = chr(65 + linha_index)  # Converte 0 → A, 1 → B, ..., 19 → T
        conteudo = " ".join(tabuleiro[linha_index][coluna_index].rjust(2) for coluna_index in range(20))
        print(f"{letra}  {conteudo}")

# Converte símbolo do navio em índice para uso nas listas de pontuação e controle
def simbolo_para_indice(simbolo):
    if simbolo == "P":
        return 0  # Porta-Aviõess
    elif simbolo == "C":
        return 1  # Cruzador
    elif simbolo == "F":
        return 2  # Fragatas
    return -1    # Água ou espaço vazio

# Permite ao jogador posicionar os navios manualmente no tabuleiro
def posicionar_navio(tabuleiro, nome, quantidade, tamanho, simbolo):
    print(f"\n== Posicionamento de {nome} ({quantidade} navios de {tamanho} células) ==")
    for numero_navio in range(quantidade):
        while True:
            exibir_tabuleiro(tabuleiro)
            entrada = input(f"Posicione o {nome} #{numero_navio + 1} (ex: B10): ").strip().upper()

            # Converte coordenada em índice de linha e coluna
            linha = ord(entrada[0]) - 65
            coluna = int(entrada[1:]) - 1

            if coluna + tamanho > 20:
                print("Navio não cabe na linha, tente outra posição")
                continue

            sobreposicao = False
            for deslocamento in range(tamanho):
                if tabuleiro[linha][coluna + deslocamento] != "~":
                    sobreposicao = True
                    break1

            if sobreposicao:
                print("Ja existe um navio nessa posição!!")

            # Posiciona o navio na horizontal a partir da coordenada informada
            for deslocamento in range(tamanho):
                tabuleiro[linha][coluna + deslocamento] = simbolo
            break

# Controla a fase de ataque, onde o jogador tenta acertar os navios
def atacar(tabuleiro_real, tabuleiro_ataque, pontuacao, partes_restantes, tamanhos_navios, nomes_navios, pontuacoes_navios):
    while True:
        print("\n======= ATAQUE =======")
        exibir_tabuleiro(tabuleiro_ataque)
        coordenada = input("Digite a coordenada para atacar (ex: D7): ").strip().upper()

        letra = coordenada[0]
        numero_str = coordenada[1:]
        linha = ord(letra) - 65
        coluna = int(numero_str) - 1

        #  Verificação leve: evita acesso fora da matriz
        if not (0 <= linha < 20 and 0 <= coluna < 20):
            print(" Posição fora do tabuleiro!")
            continue

        if tabuleiro_ataque[linha][coluna] in ["X", "O"]:
            print(" Você já atacou essa posição.")
            continue

        # Verifica se há um navio naquela posição
        alvo = tabuleiro_real[linha][coluna]
        indice = simbolo_para_indice(alvo)

        if indice != -1:
            tabuleiro_ataque[linha][coluna] = "X"
            tabuleiro_real[linha][coluna] = "X"
            print(" ACERTOU!")
            partes_restantes[indice] -= 1

            # Verifica se o navio foi totalmente destruído
            if partes_restantes[indice] % tamanhos_navios[indice] == 0:
                pontuacao[0] += pontuacoes_navios[indice]
                print(f" Você afundou um {nomes_navios[indice]}! (+{pontuacoes_navios[indice]} pontos)")
        else:
            tabuleiro_ataque[linha][coluna] = "O"
            print(" Errou...")

        # Verifica se todos os navios foram afundados
        if all(restantes == 0 for restantes in partes_restantes):
            print("\n Todos os navios foram afundados!")
            print(f" Pontuação final: {pontuacao[0]} pontos")
            break

        continuar = input("Deseja continuar jogando ? (S/N)").strip().upper()
        if continuar == "N":
            print(f"\n Jogo Encerrado pelo jogador")
            print(f" Pontuação Final: {pontuacao[0]} pontos")

# Gera um tabuleiro com os navios já posicionados para testes (sem necessidade de input)
def gerar_tabuleiro_teste():
    tabuleiro = criar_tabuleiro()

    # Porta-Aviões (3 unidades de 4 células)
    tabuleiro[0][0:4] = ["P"] * 4
    tabuleiro[2][5:9] = ["P"] * 4
    tabuleiro[4][10:14] = ["P"] * 4

    # Cruzadores (4 unidades de 3 células)
    tabuleiro[6][0:3] = ["C"] * 3
    tabuleiro[7][5:8] = ["C"] * 3
    tabuleiro[8][10:13] = ["C"] * 3
    tabuleiro[9][15:18] = ["C"] * 3

    # Fragatas (5 unidades de 2 células)
    tabuleiro[11][0:2] = ["F"] * 2
    tabuleiro[12][3:5] = ["F"] * 2
    tabuleiro[13][6:8] = ["F"] * 2
    tabuleiro[14][9:11] = ["F"] * 2
    tabuleiro[15][12:14] = ["F"] * 2

    return tabuleiro        

# Função principal que executa o jogo
def main():
    print(" Bem-vindo ao Batalha Naval (Versão Simples)\n")

    # Informações dos navios
    tamanhos_navios = [4, 3, 2]
    quantidades_navios = [3, 4, 5]
    simbolos_navios = ["P", "C", "F"]
    nomes_navios = ["Porta-Aviões", "Cruzador", "Fragata"]
    pontuacoes_navios = [30, 20, 10]

    # Cálculo das partes de navios restantes (usado para verificar fim de jogo)
    partes_restantes = [
        quantidades_navios[0] * tamanhos_navios[0],
        quantidades_navios[1] * tamanhos_navios[1],
        quantidades_navios[2] * tamanhos_navios[2]
    ]

    while True:
        print("Escolha o modo:")
        print("1 - Posicionar navios manualmente")
        print("2 - Usar tabuleiro pronto para teste")
        print("0 - Sair do Jogo")
        escolha = input("Sua escolha: ").strip()

        tabuleiro_ataque = criar_tabuleiro()

        if escolha == "0":
            print("Saindo do Jogo")
            break
        elif escolha =="1":
            tabuleiro_real = criar_tabuleiro()
            for i in range(3):
                posicionar_navio(tabuleiro_real, nomes_navios[i], quantidades_navios[i], tamanhos_navios[i], simbolos_navios[i])
            break
        elif escolha =="2":
            tabuleiro_real = gerar_tabuleiro_teste()
            print("\n Tabuleiro para testes gerado automaticamente!")
            exibir_tabuleiro(tabuleiro_real)
            break
        else:
            print("Opção Invalida, Escolha 1, 2 ou 0")



    pontuacao = [0]  # Usamos uma lista para manter mutabilidade da pontuação
    atacar(tabuleiro_real, tabuleiro_ataque, pontuacao, partes_restantes, tamanhos_navios, nomes_navios, pontuacoes_navios)

# Inicia o programa
if __name__ == "__main__":
    main()

