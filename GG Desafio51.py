p_termo = int(input('informe o primeiro termo: ').strip())
razao = int(input('informe a razão da PA: ').strip())

pa = [p_termo]

for i in range(10):
    temp = pa[i] + razao
    pa.append(temp)
    print(pa[i], end=' ==> ')
print('Acabou!!!')
