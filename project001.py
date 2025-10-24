'''
Projeto #001
Criar um programa que possibilite o usuário a jogar "JOKENPO" contra o computador.
'''

import random, emoji

# Regras do jogo
print("=-=" * 30)
print("JOKENPô")
print("---" * 30)
print(emoji.emojize("REGRAS "
      "\nO computador e o Jogador escolherão um símbolo entre PEDRA [:brick:], PAPEL [:scroll:] e TESOURA [:scissors:]"
      "\n:brick: vence :scissors:"
      "\n:scissors: vence :scroll:"
      "\n:scroll: vence :brick:"
      "\nSe ambos escolherem o mesmo símbolo, o jogo é empatado e deve ser jogado novamente."))
print("=-=" * 30)

symbol = [":brick: PEDRA", ":scissors: TESOURA", ":scroll: PAPEL"] # Opções de Símbolos

computerSymbol = random.choice(symbol) # Escolha do computador

# Escolha do jogador
playerSymbol = str(input(emoji.emojize("Escolha um dos símbolos abaixo: " 
                         "\n[0] :brick: PEDRA"
                         "\n[1] :scissors: TESOURA"
                         "\n[2] :scroll: PAPEL"
                         "\nQual foi o escolhido? ")))
if playerSymbol == "0":
    playerSymbol = ":brick: PEDRA"
elif playerSymbol == "1":
    playerSymbol = ":scissors: TESOURA"
elif playerSymbol == "2":
    playerSymbol = ":scroll: PAPEL"
else:
    print("VALOR INVÁLIDO, TENTE NOVAMENTE!")
print("=-=" * 30)

# Conferência entre escolhas e fim de Jogo
print(emoji.emojize("O Computador escolheu {}".format(computerSymbol)))
print(emoji.emojize("O Jogador escolheu {}".format(playerSymbol)))

if (computerSymbol == ":brick: PEDRA" and playerSymbol == ":scissors: TESOURA") or (computerSymbol == ":scissors: TESOURA" and playerSymbol == ":scroll: PAPEL") or (computerSymbol == ":scroll: PAPEL" and playerSymbol == ":brick: PEDRA"):
    print("VITÓRIA DO COMPUTADOR!!!")
elif (playerSymbol == ":brick: PEDRA" and computerSymbol == ":scissors: TESOURA") or (playerSymbol == ":scissors: TESOURA" and computerSymbol == ":scroll: PAPEL") or (playerSymbol == ":scroll: PAPEL" and computerSymbol == ":brick: PEDRA"):
    print("VITÓRIA DO JOGADOR!!!")
elif playerSymbol == computerSymbol:
    print("EMPATE!!!")

print("=-=" * 30)
print("FIM DE JOGO")
print("=-=" * 30)