'''
Crie um programa que receba como entrada 4 salarios,
calcule a media salarial e exiba os salarios abaixo da media
(sem sequencias)
'''

print('-==-==-==-==-==-==-==-==-==-==-==-==-==-==-')
print('[1] Versao usando variaveis condicionais')
print('[2] Versao usando list=[x, x, x, x]')
print('[3] Versao usando match case & list')
print('-==-==-==-==-==-==-==-==-==-==-==-==-==-==-')
v = int(input('[?] Versao que quer escolher: '))

if v == 1:
    soma = 0
    salario_0 = float(input('\nSálario: '))
    soma+=salario_0
    salario_1 = float(input('Sálario: '))
    soma+=salario_1
    salario_2 = float(input('Sálario: '))
    soma+=salario_2
    salario_3 = float(input('Sálario: '))
    soma+=salario_3
    media = soma/4
    print(f'Media dos salarios: {media:.2f}')
    if salario_0 < media:
        print(f'Salario(0) abaixo da média: R${salario_0}')
    if salario_1 < media:
        print(f'Salario(1) abaixo da média: R${salario_1}')
    if salario_2 < media:
        print(f'Salario(2) abaixo da média: R${salario_2}')
    if salario_3 < media:
        print(f'Salario(3) abaixo da média: R${salario_3}')

#versão melhorada do exemplo acima

if v == 2:
    salarios = [0, 0, 0, 0]
    soma = 0
    salarios[0] = float(input('\nSalario: '))
    soma+=salarios[0]
    salarios[1] = float(input('Salario: '))
    soma+=salarios[1]
    salarios[2] = float(input('Salario: '))
    soma+=salarios[2]
    salarios[3] = float(input('Salario: '))
    soma+=salarios[3]
    media = soma/4
    print('Media:', media)
    if salarios[0] < media:
        print(f'Salario(0) abaixo da média: R${salarios[0]}')
    if salarios[1] < media:
        print(f'Salario(1) abaixo da média: R${salarios[1]}')
    if salarios[2] < media:
        print(f'Salario(2) abaixo da média: R${salarios[2]}')
    if salarios[3] < media:
        print(f'Salario(3) abaixo da média: R${salarios[3]}')

#versão mais melhorada do exemplo acima
if v == 3:
    salarios = [0, 0, 0, 0]
    soma = 0
    i = 0 #variavel de controle, indice da lista
    #laço feito para achar a media
    while i<4:
        salarios[i] = float(input('Salario: '))
        soma += salarios[i]
        i+=1
    media = soma/4
    print(f'Media: {media:.2f}')
    
    i=0
    #laço feito para achar os abaixo da media
    while i<4:
        if salarios[i] < media:
            print(f'Abaixo da media: {salarios[i]:.2f}')
        i+=1
