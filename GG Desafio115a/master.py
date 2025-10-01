from uteis import formatacao
from uteis.bd import *

#BD Final
arq = 'teste2.txt'
verificacao = exist_arq(arq) 
if verificacao == False:
   criar_arquivo(arq)

#Visual do menu
while True:
    formatacao.titulo('MENU PRINCIPAL')
    formatacao.menu('Ver pessoas cadastradas', 'Cadastrar novo usuário', 'Sair do Sistema')
    opcao = formatacao.escolha_opcao_menu('Sua Opção: ', 3)

    if opcao == 1:
        formatacao.titulo('PESSOAS CADASTRADAS')
        exibir_arquivo(arq)
        linha()
        input('tecle "ENTER" para continuar...')
    elif opcao == 2:    
        formatacao.titulo('CADASTRO DE USUÁRIO')
        cadastro_user(arq)
        linha()
        input('tecle "ENTER" para continuar...')
    elif opcao == 3:
        formatacao.titulo('Volte Sempre!!!')
        break

