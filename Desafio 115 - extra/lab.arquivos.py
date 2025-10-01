#Orientações passadas pelo Gemini Cli

'''
#Versão 1.0 basicão

arquivo = open('teste.txt', 'w', encoding='utf-8')
arquivo.write('Esse é o jeito mais simples de escrever.\n')
arquivo.close()
print('ok, o comando foi executado. Verifique se o arquivo "teste.txt" apareceu na pasta')

#Versão 2.0 criação de arquivo e escrita

with open('teste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Agora usando o bloco with.\n')
    arquivo.write('É mais seguro e mais limpo!\n')
print("Arquivo 'teste.txt' sobrescrito com o método 'with'.")

#Versão 3.0 leitura de arquivo

print("---Lendo o conteúdo do arquivo 'teste.txt' ---")
with open('teste.txt', 'r', encoding='utf-8') as arquivo:
    conteudo = arquivo.read()
print(conteudo)
print('--- Leitura terminada ---')

#Versão 4.0 acrescentanto conteudo

print("--- Adicionando novo conteúdo ao arquivo ---")

with open('teste.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Esta é uma nova linha, adicionada depois.\n')
    arquivo.write('O modo "a" é muito útil.\n')
print("Conteúdo adicionado. Agora, vamos ler o arquivo completo para ver:\n")

with open('teste.txt', 'r', encoding='utf-8') as arq_estudo:
    print(arq_estudo.read())

#Versão 5.0 Tratamento de erros

try:
    with open('teste.txt', 'r', encoding='utf-8') as arq_erro:
        print(arq_erro.read())

except FileNotFoundError:
    print('é para entrar nessa parte')
'''

