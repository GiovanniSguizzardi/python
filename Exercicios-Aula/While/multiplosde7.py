print('Multiplos de 7 até 200:\n')

resultado = 0
multiplos = 0
print('Usando {While}')
while multiplos < 200:
    resultado+=7
    multiplos+=1
    print(f'{multiplos}: [{resultado}]')
    if resultado == 196:
        break

print('\n')
print('Usando {For}')
multiplo=0
for i in range(7, 200, 7):
    multiplo+=1
    print(f'{multiplo}: {i}')
