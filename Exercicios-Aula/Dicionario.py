#lista_1 = ['primeiro', 'segundo', 'terceiro']
#lista_2 = [1,2,3]
#lista_3 = zip(lista_1, lista_2)
#dic_1 = dict(lista_3)
#print(dic_1)

dados_p = {'nome':'Pedro', 'altura':1.80, 'idade':18, 'peso':105.00}
dados_a = {'nome':'Angelo', 'altura':1.83, 'idade':18, 'peso':90.00}
dados_f = {'nome':'Felipe', 'altura':1.74, 'idade':20, 'peso':82.00}
pessoas = {'1':dados_p, '2':dados_a, '3':dados_f}

while True:
    escolha = input('[>>] Qual pessoa gostaria de consultar: ')
    print(pessoas[escolha])

