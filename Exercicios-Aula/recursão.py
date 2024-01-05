# Recursão

#Somatoria na matematica
# f(4)= 1 + 2 + 3 + 4 =10
# f(5) = 1 + 2 + 3 + 4 + 5 = 15

# f(X) = f(x - 1) + x
# (1, 3, 5, 7, 9)

# Exemplo 1 - somar uma lista de numeros (Sem Recursao)
def somaNumeros(lista):
    soma = 0
    for i in lista:
        soma += i
    return soma

#Programa Principal
lista = [1, 3, 5, 7, 9]
print(f'soma: {somaNumeros(lista)}')

# Função Recursiva
# Somar o primeiro elemento da lista - lista[0]
# e somo com o restante da lista - lista[1:]

# [1, 3, 5, 7, 9]
# (1 (3 + ( 5+ (7 + 9))))
# (1 + (3 + (5 + 16)))
# (1 + (3 + 21))
# (1 + 24)
# 25

def somarRecursivo(lista):
    if len(lista)==1 :
        return lista[0]
    else: 
        return lista[0]+somarRecursivo(lista[1:])
    
# Teste
print(f'Soma: {somarRecursivo(lista)}')


def somatorio(n):
    if n == 1:
        return 1
    else:
        return n + somatorio(n-1)
    
# Teste
n = 6
print(f'Soma: {somatorio(n)}')

