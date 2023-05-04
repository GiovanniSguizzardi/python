'''
-==-==-==-==-==-==-==-==-==-==-==-==-
{*} Calculadora Simples
- Adição
- Subtração
- Divisão
- Multiplicação

{*} Funções
- menu()
- entrada_de_dados()
- adicao()
- subtracao()
- divisao()
- multiplicacao()
- imprimir()
- controlador()
-==-==-==-==-==-==-==-==-==-==-==-==-
'''

#Função Menu()
def menu():
    print('**- Menu-Calculadora -**')
    print('[1] Adição')
    print('[2] Subtração')
    print('[3] Multiplicação')
    print('[4] Divisão')
    op = int(input('Escolha: '))
    return op

#Função entrada_de_dados()
def entrada_dados():
    print('**- Entrada de Dados -**')
    num = int(input('Número: '))
    return num

#Função adicao()
def adicao(n1, n2):
    print('**- Adição -**')
    result = n1+n2
    return result

#Função subtracao()
def subtracao(n1, n2):
    print('**- Subtração -**')
    result = n1-n2
    return result

#Função multiplicacao()
def multiplicacao(n1, n2):
    print('**- Multiplicação -**')
    result = n1*n2
    return result

#Função divisao()
def divisao(n1, n2):
    print('**- Divisão -**')
    result = n1/n2
    return result

#Função imprime()
def imprime(result):
    print('**- Imprimir -**')
    print('Resultado: ', result)

#Função controlador()
def controlador(n1, n2, op):
    print('**- Controlador -**')
    if(op == 1):
        result = adicao(n1, n2)
    elif(op == 2):
        result = subtracao(n1, n2)
    elif(op == 3):
        result = multiplicacao(n1, n2)
    elif(op == 4):
        result = divisao(n1, n2)
    else:
        result = 'Opção invalida'
    return result

#Principal
print('**- Principal -**')
op = menu()
n1 = entrada_dados()
n2 = entrada_dados()
result = controlador(n1, n2, op)
imprime(result)
