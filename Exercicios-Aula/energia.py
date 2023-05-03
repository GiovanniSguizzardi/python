import time
print('-=++=-KWH Calculator -=++=-')
kwh = int(input('[>>] KWattsH consumido: '))

if kwh < 150:
    consumo = kwh * 0.20
    print('[r] Seu consumo foi de:', consumo, 'R$')

elif kwh >= 150 and kwh < 500:
    consumo = kwh * 0,25
    print('[r] Seu consumo foi de:', consumo, 'R$')

else:
    consumo = kwh * 0,30
    print('[r] Seu consumo foi de:', consumo, 'R$')
    
if consumo > 11.90:
    print('[!] Porfavor consulte os atendentes da ENEL, pois sua conta está errada...')
