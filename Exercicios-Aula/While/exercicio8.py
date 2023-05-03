print('Media aritmetica dos numeros pares entre 13-73:\n')

soma = 0
multiplo = 0
for x in range(14, 73, 2):
    multiplo += 1
    print(f'{multiplo}: {x}')
    soma += x
media = soma/len(range(14, 73, 2))
print('\n-==-{}-==-')
print(f'M.A: {media}')
print('-==-{}-==-')
