from time import sleep  
def contador(i, f, p): 
    if p == 0: 
        p = 1 
    if p < 0: 
        p = -p 
    print('-='*20) 
    print(f'Contagem de {i} até {f} de {p} em {p}') 
        
    if i < f:            
        for w in range(i, f+1, p):   
            print(w, end= ' ', flush=True)   
            sleep(0.5)   
    elif i > f:   
        for x in range(i, f-1, -p):   
            print(x, end= ' ', flush=True)   
            sleep(0.5)   

    print('Fim!')   

contador(1, 10, 1)  
contador(0, 100, 10) 
contador(10, 0, 2) 

print('-='*20) 
print('Agora é sua vez de personalizar a contagem') 
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))  



