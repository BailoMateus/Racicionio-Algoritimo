#---------------------------------------------------------------------------------------------------------------------------------
# Batalha Naval - PjBL2
# Alunos: Mateus Luiz Bailo, Icaro Nunes, Bruno Hinz
#---------------------------------------------------------------------------------------------------------------------------------

def criar_tabuleiro():
    return [["~" for _ in range(20)] for _ in range(20)]

def exibir_tabuleiro(tabuleiro):
    cabecalho = "   " + " ".join([str(i + 1).rjust(2) for i in range(20)])
    print(cabecalho)
    for linha_index in range(20):
        letra = chr(65 + linha_index)
        conteudo = " ".join(tabuleiro[linha_index][coluna_index].rjust(2) for coluna_index in range(20))
        print(f"{letra}  {conteudo}")

def simbolo_para_indice(simbolo):
    if simbolo == "P":
        return 0
    elif simbolo == "C":
        return 1
    elif simbolo == "F":
        return 2
    return -1

def posicionar_navio(tabuleiro, nome, quantidade, tamanho, simbolo):
    print(f"\n== Posicionamento de {nome} ({quantidade} navios de {tamanho} células) ==")
    for numero_navio in range(quantidade):
        exibir_tabuleiro(tabuleiro)
        entrada = input(f"Posicione o {nome} #{numero_navio + 1} (ex: B10): ").strip().upper()
        linha = ord(entrada[0]) - 65
        coluna = int(entrada[1:]) - 1
        for deslocamento in range(tamanho):
            tabuleiro[linha][coluna + deslocamento] = simbolo


def atacar(tabuleiro_real, tabuleiro_ataque, pontuacao, partes_restantes, tamanhos_navios, nomes_navios, pontuacoes_navios):
    while True:
        print("\n======= ATAQUE =======")
        exibir_tabuleiro(tabuleiro_ataque)
        coordenada = input("Digite a coordenada para atacar (ex: D7): ").strip().upper()

        letra = coordenada[0]
        numero_str = coordenada[1:]
        linha = ord(letra) - 65
        coluna = int(numero_str) - 1

        # Verificação leve: dentro dos limites do tabuleiro
        if not (0 <= linha < 20 and 0 <= coluna < 20):
            print(" Posição fora do tabuleiro!")
            continue

        if tabuleiro_ataque[linha][coluna] in ["X", "O"]:
            print("Você já atacou essa posição.")
            continue

        alvo = tabuleiro_real[linha][coluna]
        indice = simbolo_para_indice(alvo)

        if indice != -1:
            tabuleiro_ataque[linha][coluna] = "X"
            tabuleiro_real[linha][coluna] = "X"
            print(" ACERTOU!")
            partes_restantes[indice] -= 1
            if partes_restantes[indice] % tamanhos_navios[indice] == 0:
                pontuacao[0] += pontuacoes_navios[indice]
                print(f" Você afundou um {nomes_navios[indice]}! (+{pontuacoes_navios[indice]} pontos)")
        else:
            tabuleiro_ataque[linha][coluna] = "O"
            print(" Errou...")

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

def main():
    print(" Bem-vindo ao Batalha Naval (Versão Simples)\n")

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

    print("Escolha o modo:")
    print("1 - Posicionar navios manualmente")
    print("2 - Usar tabuleiro pronto para teste")
    escolha = input("Sua escolha: ").strip()

    tabuleiro_ataque = criar_tabuleiro()

    if escolha == "2":
        tabuleiro_real = gerar_tabuleiro_teste()
        print(" Tabuleiro de teste gerado automaticamente!")
        exibir_tabuleiro(tabuleiro_real)
    else:
        tabuleiro_real = criar_tabuleiro()
        for i in range(3):
            posicionar_navio(tabuleiro_real, nomes_navios[i], quantidades_navios[i], tamanhos_navios[i], simbolos_navios[i])

    pontuacao = [0]
    atacar(tabuleiro_real, tabuleiro_ataque, pontuacao, partes_restantes, tamanhos_navios, nomes_navios, pontuacoes_navios)

if __name__ == "__main__":
    main()
