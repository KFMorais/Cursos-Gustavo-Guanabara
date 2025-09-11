from utilidadesCeV import dado,moeda

p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p, 10, 20)


'''
p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 80, 35)



print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p)}')
print(f'Aumentando 10% de {moeda.moeda(p)}, temos {moeda.aumentar(p,10, False)}')
print(f'Reduzindo 13% de {moeda.moeda(p)}, temos {moeda.diminuir(p,13, False)}')
'''
