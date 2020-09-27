import random

def forca():
  
  print("***************")
  print("*Jogo da forca*")
  print("***************")


  palavra_secreta = banco_palavras()
  letras_acertadas = letras_certas(palavra_secreta)
  
  enforcou = 6
  acertou = False

  while (enforcou > 0 and not acertou):
    chute = input("Digite uma letra\n").lower().strip()
    posicao = 0
    if (chute in palavra_secreta):
      for letra in palavra_secreta:
        if (chute == letra):
          letras_acertadas[posicao] = chute
        posicao = posicao + 1
    else:
      enforcou = enforcou - 1
    print("************")
    print(letras_acertadas)
    print(f"Chances restantantes:{enforcou}")
    print("************")
    acertou = "_" not in letras_acertadas
  if (acertou):
    print("***Ganhou***")
  else:
    print("***Perdeu***")


def banco_palavras():
  banco_de_palavras = []
  with open("palavras.txt") as arquivo:  
    for linha in arquivo:
      banco_de_palavras.append(linha.strip())
  return banco_de_palavras[random.randrange(0,len(banco_de_palavras))]
  
def letras_certas(palavra_secreta):
  return ["_" for letra in palavra_secreta]