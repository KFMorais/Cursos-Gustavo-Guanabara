nota1 = int(input('Informe a primeira nota: '))
nota2 = int(input('Informe a segunda nota: '))
media = (nota1 + nota2)/2

cores = {
'limpa':'\033[m',
'fvermelho':'\033[1;41m',
'fverde':'\033[1;42m',
'famarelo':'\033[43m',
}

print(f'a média do aluno foi {media}')
if (media > 7):
    print(f'{cores["fverde"]}Aprovado{cores["limpa"]}')
elif (5 < media < 7):
    print(f'{cores["famarelo"]}Final{cores["limpa"]}')
else:
    print(f'{cores["fvermelho"]}Reprovado{cores["limpa"]}')

#print(f'a média do aluno foi {(nota1+nota2)/2}')
