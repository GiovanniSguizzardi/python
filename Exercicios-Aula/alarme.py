#when h-m-s gets 23:58:59 --> print('Alarme!')
alarme_h = int(input('Hora para alarme: '))
alarme_m = int(input('Minuto para alarme: '))
alarme_s = int(input('Segundo para alarme: '))
h = 0
while h < 24:
    m = 0
    while m < 60:
        s = 0
        while s < 60:
            print(f'{h:02}:{m:02}:{s:02}')
            if h == alarme_h and m == alarme_m and s == alarme_s:
                print('+------------------+')
                print('|     Alarme!      |')
                print('| Hora de acordar! |')
                print('+------------------+')
                print('Fim da Operação...')
                break 
            s+=1
        if h == alarme_h and m == alarme_m:
            break
        m+=1
    if h == alarme_h:
        break
    h+=1