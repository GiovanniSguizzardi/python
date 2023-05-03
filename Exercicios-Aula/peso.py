print('Sistema de GDO')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
massa = peso / (altura)**2

if massa < 26:
    print('Resultado: Normal')
    
elif massa >= 26 and massa < 30:
    print('Resultado: Obeso')
    
else:
    print('Resultado: Obeso Morbido')            
