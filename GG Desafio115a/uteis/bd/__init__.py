from uteis.formatacao import *

def exibir_arquivo(nome_arq): 
    try:
        with open(nome_arq, 'r', encoding='utf-8') as arq_aberto:
            conteudo = arq_aberto.readlines()
            if conteudo == []:
                print('Nenhum cadastro existente!!!')
            else:
                print(f'{'|Nome|':<42} {'|Idade|'}')
                linha()
                for i in conteudo:
                    dados = i.split(';')
                    print(f'{dados[0]:<46}{dados[1].strip()}')
    except FileNotFoundError:
        print(f'Arquivo de nome "{nome_arq}" não localizado')
    except Exception as e:
        print(f'Ocorreu o seguinte Erro: {e}')

def cadastro_user(nome_arq): #revisado
    nome = leia_nome('Nome: ')
    idade = leia_idade('Idade: ')
    try:
        with open(nome_arq, 'a', encoding='utf-8') as arq_open:
            arq_open.write(f'{nome};{idade}\n')
            print(f'Usuário {nome} cadastrado com sucesso!')
    except FileNotFoundError:
        print(f'Arquivo de nome "{nome_arq}" não localizado')
    except Exception as e:
        print(f'Ocorreu o seguinte Erro: {e}')

def exist_arq(nome_arq):
    try:
        with open(nome_arq, 'r', encoding='utf-8') as nome_arq_ab:
            return True
    except FileNotFoundError:
        return False

def criar_arquivo(nome_arq):
    try:
        with open(nome_arq, 'w', encoding='utf-8') as arq_criado:
            pass   #o ... remete que no futuro deve ser colocado alguma ação aqui já o pass deixa claro que a intenção que realmente não aconteça nada...
    except Exception as e:
        print('Erro na criação do arquivo')



    

    











'''


def arq_existe(n_arq):
    try:
        res = open(n_arq, 'rt')
        res.close
    except FileNotFoundError:
        return False
    else:
        return True

def criar_arq(n_arq):
    try: 
        res = open(n_arq, 'wt+')
        res.close()
    except:
        print('Não foi possível gerar o arquivo!') 
    else:
        print(f'Arquivo {n_arq} criado com sucesso!')

def leia_arq(n_arq):
    try:
        a = open(n_arq, 'rt')
    except:
        print('Erro na leitura do arquivo')
    else:
        titulo('PESSOAS CADASTRADAS')
        print(a.read())

    

'''