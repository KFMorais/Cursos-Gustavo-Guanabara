import requests

#url = 'https://pudim.com.br/'

try:
    #requests.get(url)
    requests.get('https://pudim.com.br/')

except:
    print('Erro...')
else:
    print('Deu certo')
    