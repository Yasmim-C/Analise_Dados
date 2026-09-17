import numpy as np

# Mapa 5 x 5 

mapa = np.random.randint(1, 10, size=(5, 5))

print(mapa)

# Posionando o tesouro em uma posição aleatória

while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0,5, size=2)
    if (tesouro_linha, tesouro_coluna) != (0, 0):
        break

posicao_jogador = (0, 0)
pontuacao = 0

def mostrar_mapa(mapa, posicao_jogador):
    mapa_com_jogador = mapa.copy()
    linha, coluna = posicao_jogador
    mapa_com_jogador[linha, coluna] = -1

    print('\n Mapa Atual:')
    for linha in mapa_com_jogador:
        print(" ".join(linha.astype(str)))

# Fluxo principal

while True:
    mostrar_mapa(mapa, posicao_jogador)

    direcao = input("Informe para qual direção deseja se mover: (Cima, baixo, direita e esquerda): ").strip().lower() # O ".strip" retira os espaços e o ".lower" deixa as letras minusculas.

# Dicionario dos movimentos do jogador

    movimentos = {
        "cima": (-1, 0),
        "baixo": (1, 0),
        "direita": (0, 1),
        "esquerda": (0, -1),
        "c": (-1, 0),
        "b": (1, 0),
        "d": (0, 1),
        "e": (0, -1),
    }
    if direcao in movimentos:
        nova_posicao = (posicao_jogador[0] + movimentos[direcao][0], posicao_jogador[1] + movimentos[direcao][1])
    else:
        print("Direção inválida! Tente outra ves")

# Verifica se a nova posição é válida

    if not (0 <= nova_posicao[0] < mapa.shape[0] and 0<= nova_posicao[1] < mapa.shape[1]):
        print("Movimento fora dos limites! Tente outra vez")
        continue

    posicao_jogador = nova_posicao
    pontuacao +=1

    if posicao_jogador == (tesouro_linha, tesouro_coluna):
        mostrar_mapa(mapa, posicao_jogador)
        print("\n\n====== Parabéns!! Você chegou ao tesouro ======")
        print(f"Pontuação Final: {pontuacao}")
        print(f"O tesouro estava na posição:{(tesouro_linha, tesouro_coluna)}")