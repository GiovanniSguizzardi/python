import time
print('Ordenador de Numeros')
time.sleep(1)
n1 = float(input('Insira um numero: '))
n2 = float(input('Insira outro numero: '))
n3 = float(input('Insira mais um numero: '))
numeros = n1, n2, n3

print('Qual ordem será usada?')
print('[1] Crescente')
print('[2] Decrescente')
ordem = int(input('Insira sua opção: '))

match ordem:
    case 1:
        numeros = sorted(numeros, reverse=True)
        print('Ordem Crescente', numeros)
    case 2:
        numeros = sorted(numeros, reverse=False)
        print('Ordem Decrescente', numeros)
        
