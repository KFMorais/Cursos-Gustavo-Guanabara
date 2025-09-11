#Estratégia 1
'''

def voto(an):
    from datetime import date
    idade = 2018 - an #date.today().year - an
    if idade >=18 and idade < 65:
        return idade, 'Voto Obrigatório'
    elif idade >=16 and idade < 18 or  idade >= 65:
        return idade, 'Voto Opcional'
    else:
        return idade, 'Não Vota'

print('-'*30)
ano = int(input('Em que ano você nasceu: '))
print(f'Com {voto(ano)[0]} anos: {voto(ano)[1]}.')
'''
#Estratégia 2
'''

def voto(an):  
    from datetime import date  
    idade = 2018 - an #date.today().year - an  
    if idade >=18 and idade < 65: 
        return f'Com {idade} anos: Voto Obrigatório.' 
    elif idade >=16 and idade < 18 or  idade >= 65: 
        return f'Com {idade} anos: Voto Opcional.' 
    else:
        return f'Com {idade} anos: Não Vota.' 

print(voto(1990)) 
'''         

### Conhecimentos extras: 
#1- Coloquei o "from datetime import date" para rodas apenas no local (não no global)... pois 
# para este programa só precisa dessa library lá. Assim gasta menos memória...
#2- Lembrar de quando for fazer If's, colocar primeiro as excessões depois no Else coloca a "regra geral"
