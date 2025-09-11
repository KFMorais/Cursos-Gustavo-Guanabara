nome = input('digite seu nome: ').strip()

analise = 'SILVA' in nome.upper()

if(analise == True):
    print('O nome digitado possui "SILVA" nele')
else:
    print('O nome indicado não possui "SILVA"')