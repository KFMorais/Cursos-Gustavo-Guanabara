def linha():  #revisado
    print('-'*50)

def titulo(txt): #revisado
    linha()
    print(f'{txt:^50}')
    linha()

def menu(*opcoes): #revisado
    for e, i in enumerate(opcoes):
        print(f'{e+1} - {i}')
    linha()

def escolha_opcao_menu(txt, q_itens): #revisado
    while True:
        try:
            ni = int(input(txt))
            if ni > q_itens or ni < 1:
                print('Ops, Digite um número que tenha correspondencia no menu')
                continue
            else:
                return ni
        except ValueError:
            print('Erro, Digite um número inteiro válido')

def leia_idade(txt): #revisado
    while True:
        try:
            idade = int(input(txt))
            if idade < 0:
                print('Ops!!! Não existe idade negativa')
                continue
            else:
                return idade
        except ValueError:
            print('Erro: Digite um número inteiro positivo') 
        except Exception as e:
            print(f'Vixx: rolou um erro do tipo: {e}')

def leia_nome(txt): #revisado
    while True:
        try:
            nome = input(txt).title().strip()
            if nome == '':
                print('Ops: Digite um nome válido')
                continue
            elif nome.isnumeric() == True:
                print('Eita... e é filho de Elon Musk???')
                continue
            res = 0
            for i in nome:
                if i.isdigit() == True:
                    res = True
                    break
            if res == True:
                print('Ops: Digite um nome válido')
                continue
            else:
                return nome
        except Exception as e:
            print(f'Vixx... deu um ERRO do tipo {e}')
