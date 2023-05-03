print('Somatorio de uma sequencia [Digitar 0 para acabar sequencia]')
n = int(input('Número: '))
somatoria = 0

while n > 0:
    n = int(input('Número: '))
    somatoria += n
print(f'Resultado: {somatoria}')


