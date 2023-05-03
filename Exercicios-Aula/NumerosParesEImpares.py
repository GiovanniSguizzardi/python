import time

n1 = int(input('[>>] Insira um numero: '))
time.sleep(1)
n2 = int(input('[>>] Insira outro numero: '))
print('\n')

if n1 > n2:
    print('[+] n1 maior que n2, e o primeiro numero é:')
    condicao = 2

else:
    print('[?] n2 maior/igual que n1, pois:')
    condicao = 1

match condicao:
    case 1:
        if n1 == n2:
            print('[!] Os numeros são iguais')
        else:
            print('[!] O n2 é maior que o n1')
        
    case 2:
        if n1 % 2 == 0:
            print('[+] n1 é PAR')
        else:
            print('[-] n1 é IMPAR')
    
            
