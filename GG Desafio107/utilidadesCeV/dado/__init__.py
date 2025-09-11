def leiaDinheiro(txt):
    valor = input(txt).strip().replace(',', '.')
    if valor == '':
        temp = True
    else: 
        temp = valor.isalpha()

    while temp == True:
        print(f'Erro: "{valor}" é um preço inválido!')
        valor = input(txt).strip().replace(',', '.')
        if valor == '':
            temp = True
        else: 
            temp = valor.isalpha()

    return float(valor)


#Trabalhar com isalpha()
