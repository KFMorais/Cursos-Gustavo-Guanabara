letraa = letrab = menor = ciclo = letrac = 0
while True:
    ciclo += 1
    nome_produto = str(input('Nome do Produto: ').strip().title())
    preco = float(input('Preço: R$ ').strip())

    letraa += preco

    if preco > 1000:
        letrab += 1

    if ciclo == 1 or preco < menor:
        menor = preco
        letrac = nome_produto 
    
    opcao = str(input('Deseja informar mais produtos? [S] ou [N] ').upper().strip()[0])
    while opcao not in 'SN':
        print('Opção inválida!')
        opcao = str(input('Deseja informar mais produtos? [S] ou [N] ').upper().strip()[0])
    if opcao == 'N':
        break

print(f'O total da compra foi R$ {letraa:.2f}')
print(f'Temos {letrab} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi a {letrac} que custou R$ {menor:.2f}')
