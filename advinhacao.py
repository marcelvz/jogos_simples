import random

def advinhacao(nome):
  print("**********************")
  print("*Teste de advinhação *")
  print("**********************")

  numero_secreto = random.randrange(1,101)
  dificuldade = int(input("Escolha a dificuldade 1 - Facil, 2 - Medio, 3 - Dificil\n"))
  if (dificuldade == 1):
    tentativas = 20
  elif (dificuldade == 2 ):
    tentativas = 10
  else:
    tentativas = 5

  pontos = 100

  while (tentativas > 0):
    print("Total de tentativas {}".format(tentativas))
    chute = int(input("Digite seu chute entre 1 e 100 \n"))
    if (chute < 1 or chute > 100):
      print("Digite um numero válido")
      continue
    if (numero_secreto == chute):
      print("Acertou")
      break
    else:
      if (chute > numero_secreto):
        print("Errou! Seu chute foi maior")
      else:
        print("Errou! Seu chute foi menor")
    tentativas = tentativas - 1
    pontos = pontos - abs(chute - numero_secreto)
  print(f"Fim de jogo! \nO numero secreto é: {numero_secreto}\nSua pontuação: {pontos}")
 
  with open("registro.txt","a") as registro:
      registro.write(f"{nome},{pontos}\n")