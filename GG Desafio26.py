frase = input('digite uma frase: ').strip().lower()

print(f'A frase em questão tem {frase.lower().count('a')} letras "a"')
print(f'{frase.find('a')}')
print(f'{frase.rfind('a')}')