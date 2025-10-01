#não está mais sendo utilizado no projeto do GG Desafio 115A

from uteis import formatacao

def impr_bd(users):
    formatacao.titulo('PESSOAS CADASTRADAS')
    for k, v in users.items():
        print(f'{k:<23}{v} anos')
    print('-'*30)
    
def cadastro(new_user):
    formatacao.titulo('CADASTRANDO NOVOS USERS')
    while True: 
        nome = input('Nome: ').strip()
        if nome == '':                
            print('Eiii... tu não digitou o nome da pessoa')
            continue
        elif nome.isnumeric(): 
            print('Eiii... Essa pessoa é filha de Ellon Musk para ser um número?')
            continue
        elif nome.isalpha():
            break
        else: 
            print('Vixxx... ve direito o que tu está digitando...')
            
    while True:
        try:
            idade = int(input('Idade: '))
            if idade < 0:
                print('Ops!!! Não existe idade negativa')
                continue
            else: 
                print(f'Cadastro de "{nome}" realizado com sucesso!!!')
                return nome, idade
                #print('retorno')
        except ValueError:
            print('Digite um número inteiro positivo correspondente a idade')
