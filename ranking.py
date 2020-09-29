def ranking():
  ''' 
  Função que faz a leitura do arquivo de texto onde estão registrados as pontuações e 
  exibe a lista com os nomes e a pontuação.
  '''
  tabela = []
  with open("registro.txt") as ranking:
    for linha in ranking:
      tabela.append(linha.strip().partition(',')[::2])

  print("*"*37)
  for jogador in tabela:
    print('* Jogador: {0:<10} Pontos: {1:<5} *'.format(jogador[0],jogador[1]))    
  print("*"*37)
  