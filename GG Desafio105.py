def notas(*dados, sit=False):  
    '''
    Programa para identificar maior nota, menor nota, média e situação (opcional)
    '''
    
    levantamento = {}  
    for e, i in enumerate(dados):
        if e == 0:
            maior = i
            menor = i
            soma = 0
        if i < menor: 
            menor = i
        elif i > maior:
            maior = i
        soma += i
    levantamento['qtda'] = len(dados)  
    levantamento['maior'] = maior  
    levantamento['menor'] = menor  
    levantamento['media'] = soma/len(dados)  
    
    if sit == True: 
        if levantamento['media'] < 5:
            levantamento['situação'] = 'Ruim'
        elif 5 <= levantamento['media'] < 7:    
            levantamento['situação'] = 'Razoável'
        elif 7 <= levantamento['media'] < 8:
            levantamento['situação'] = 'Boa'
        elif 8 <= levantamento['media'] <= 10:
            levantamento['situação'] = 'Ótima'
        else:
            levantamento['situação'] = 'Algo errado não está certo!!!'
    
    return levantamento



#Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)  
print(resp)  
help(notas)
