import time
print('Bem-Vindo ao Sistema, carregando dados...')
time.sleep(2)
compra = float(input('--> Insira o valor da compra: '))
quantidade = float(input('--> Insira a quantidade comprada: '))
if compra < 100:
    print('O valor da compra foi de:', compra, 'com a quantidade de:', quantidade)
    
elif compra >= 100 and compra <= 199:
    desconto = compra * 0.9
    total = compra - desconto
    print('Um desconto de 10% sera dado ao valor')
    print('Desconto:', total, '%')
    print('Total:', desconto * quantidade)

elif compra >= 200 and compra <= 299:
    desconto = compra * 0.8
    total = compra - desconto
    print('Um desconto de 20% sera dado ao valor')
    print('Desconto:', total, '%')
    print('Total:', desconto * quantidade)

elif compra >= 300 and compra <= 399:
    desconto = compra * 0.7
    total = compra - desconto
    print('Um desconto de 30% sera dado ao valor')
    print('Desconto:', total, '%')
    print('Total:', desconto * quantidade)

elif compra >= 400 and compra <= 499:
    desconto = compra * 0.6
    total = compra - desconto
    print('Um desconto de 40% sera dado ao valor')
    print('Desconto:', total, '%')
    print('Total:', desconto * quantidade)

else:
    print('Um brinde será dado ao passar no caixa')
