import random

def forca():
  '''
  Jogo de forca. Usa a função 'banco_de_palavras' para selecionar a palavra secreta.
  '''
  print("***************")
  print("*Jogo da forca*")
  print("***************")


  palavra_secreta = banco_palavras()
  letras_acertadas = ["_" for letra in palavra_secreta]
  
  enforcou = 6
  acertou = False

  while (enforcou > 0 and not acertou):
    chute = input("Digite uma letra\n").lower().strip()
    posicao = 0
    if (chute in palavra_secreta):
      for letra in palavra_secreta:
        if (chute == letra):
          letras_acertadas[posicao] = chute
        posicao += 1
    else:
      enforcou -= 1
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
  '''
  Le o arquivo texto com as palavras, separa em uma lista e retorna uma palavra escolhida aleatoriamente
  '''
  banco_de_palavras = []
  with open("palavras.txt") as arquivo:  
    for linha in arquivo:
      banco_de_palavras.append(linha.strip())
  palavra_escolhida = banco_de_palavras[random.randrange(0,len(banco_de_palavras))]
  return palavra_escolhida