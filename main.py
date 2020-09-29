"""Menu principal de jogos feitos como estudos iniciais de python
    Jogo 1 - Forca
    Jogo 2 - Advinhar um número entre 1 e 100
    Ranking com a pontuação """


from advinhacao import advinhacao
from ranking import ranking
from forca import forca

print("*"*20)
print("{0:*^20}".format(' Olá '))
print("*"*20)

jogando = True
nome = input("Digite seu nome\n").lower().strip()

while (jogando):

  escolha = int(input("1 - Forca 2- Advinhação 3-Ranking\n"))
  if (escolha == 1):
    forca()
  elif (escolha == 2):
    advinhacao(nome)
  elif (escolha == 3):
    ranking()
  else:
    print("Escolha invalida")
  if (input("Deseja continuar S ou N?\n").lower() != 's'):
    jogando = False

