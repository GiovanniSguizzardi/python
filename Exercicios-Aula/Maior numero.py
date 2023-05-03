print('Maior número de uma sequencia [Digitar 0 para acabar sequencia]')
n = int(input('[!] Número: '))
maior = 0
while n != 0:
    if n > maior:
        maior = n
    n = int(input('[!] Número: '))
print('[>>] Maior:', maior)
