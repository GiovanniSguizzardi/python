#Manipulação de Listas com Funções
'''
1) Função tamanho_lista() Feito
2) Função criar_lista() Feito
3) Função imprimir_lista() Feito
4) Função imprimir_pares() Feito
5) Função imprimir_impares() Feito
6) Função que adiciona os pares em uma lista() Feito
7) Função que adiciona os impares em uma lista() Feito
8) Função buscar um elemento na lista()
'''

def tamanho_lista():
    print('[DEF] Tamanho Lista')
    t = int(input('[?] Tamanho da lista: '))
    return t

def criar_lista(t):
    print('\n[DEF] Criar lista')
    lista = [] #cria lista vazia
    i = 0 #variavel de controle
    while i < t:
        #lista[i] = int(input('Numero: '))
        n = int(input('[?] Numero: '))
        lista.append(n)
        i+=1
    return lista

def imprimir_pares(lista):
    print('[DEF] Pares')
    lista_p = [] #cria lista vazia
    for i in lista:
        if i%2 == 0:
            print(i)
            lista_p.append(i)
    return lista_p

def imprimir_impares(lista):
    print('\n[DEF] Impares')
    lista_i = [] #cria lista vazia
    for i in lista:
        if i%2 != 0:
            print(i)
            lista_i.append(i)
    return lista_i

def imprimir_lista(lista):
    print('\n[DEF] Imprimir Lista')
    for i in lista:
        print(f'[!] Elemento: {i}')
    print(f'Lista: {lista}')

def buscar_na_lista(lista):
    print('\n[DEF] Buscar Elemento na Lista')
    numero = int(input('Numero na lista: '))
    #controlador de posição da lista
    if numero in lista:
        index = lista.index(numero)
        print(f'Numero, {numero} encontrado no Index, {index}')
    else:
        print(f'Número, {numero} não está na lista!')
        
def principal():
    print('[DEF] Função Principal')
    t = tamanho_lista()
    lista = criar_lista(t)
    pares = imprimir_pares(lista)
    impares = imprimir_impares(lista)
    imprimir = imprimir_lista(lista)
    busca = buscar_na_lista(lista)

#Programa Principal
principal()
