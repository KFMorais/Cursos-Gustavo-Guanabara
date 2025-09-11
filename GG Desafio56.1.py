lista_idadesm = []
lista_idadesf = []
nomem = []

soma_idades = 0
for i in range(4):
    nome = input(f'Digite o {i+1}º nome: ').strip().title()
    idade = int(input('Digite a idade dessa pessoa: ').strip())
    genero = input(f'Digite o gênero (M/F): ').strip().title()
    soma_idades = soma_idades + idade
    if genero == "M":
        lista_idadesm.append(idade)
        nomem.append(nome)        
    if genero == "F":
        lista_idadesf.append(idade)

media_idades = soma_idades/4
print(f'1º: A média de idade do grupo é de {media_idades:.1f} anos')   #1º respondido

mmaisvelho = lista_idadesm[0]
for i in range(len(lista_idadesm)):
    if lista_idadesm[i] > mmaisvelho:
        mmaisvelho = lista_idadesm[i]
print(f'2º: O nome do homem mais é velho é {nomem[i]} e ele tem {mmaisvelho} anos') #2º respondido

soma = 0
for idade in (lista_idadesf):
    if idade < 20:
        soma += 1
    
print(f'3º: Para os dados informados, {soma} mulheres tem menos de 20 anos') #3º respondido