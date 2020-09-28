def ranking():
  ''' 
  Função que faz a leitura do arquivo de texto onde estão registrados as pontuações e 
  exibe a lista com os nomes e a pontuação.
  '''
  tabela = []
  with open("registro.txt") as ranking:
    for linha in ranking:
      tabela.append(linha.strip().partition(',')[::2])

  print("*"*40)
  for jogador in tabela:
    print(f"* Jogador: {jogador[0]}\t Pontos: {jogador[1]}\t*")
  print("*"*40)  
