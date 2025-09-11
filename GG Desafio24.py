cidade = input('digite o nome da cidade: ').strip().split()
analise = "SANTO" in cidade[0].upper()
if (analise == True):
   print(f'A cidade indicada inicia com a palavra "SANTO"')
else:
   print(f'A cidade indicada NÃO inicia com a palavra "SANTO"')