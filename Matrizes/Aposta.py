
apostas = []


for i in range(1, 6):
    print(f"\nJogador {i}:")
    jogador_aposta = []

   
    for j in range(1, 4):
        placar = input(f"Digite o placar do Jogo {j} (formato 'X x Y'): ")
        jogador_aposta.append(placar)

   
    apostas.append(jogador_aposta)


print("\n Apostas dos Jogadores:")
for i in range(5):
    print(f"Jogador {i+1}:")
    for j in range(3):
        print(f"  Jogo {j+1}: {apostas[i][j]}")