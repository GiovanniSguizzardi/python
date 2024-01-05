import time
#Algoritmo de ordenação - Merge Sort (Recursivo)
#Ordenação por intercalação/mistura

def merge_sort(lista):
    if len(lista) > 1: #caso base

        #encontrando o meio da lista
        meio = len(lista) // 2 #divisão inteira

        #dividindo a lista em 2 sublistas (L e R)
        L = lista[:meio]
        R = lista[meio:]

        #chamada recursiva
        merge_sort(L)
        
        merge_sort(R)

        #variaveis de controle:
        #i - fará o controle da lista L
        #j - fará o controle da lista R
        #k - fará o controle da lista anterior a recursão
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                lista[k] = L[i]
                i+=1
            else:
                lista[k] = R[j]
                j+=1
            k+=1

        #verificação dos elementos da lista L
        while i < len(L):
            lista[k] = L[i]
            i+=1
            k+=1

        #verificação dos elementos da lista R
        while j < len(R):
            lista[k] = R[j]
            j+=1
            k+=1

#Programa principal
lista = [12, 11, 13, 5, 6 , 7]
inicio = time.time()
print(f'Lista Original: {lista}')
merge_sort(lista)
print(f'Lista Ordenada: {lista}')
fim = time.time()
print(f'Tempo de execução: {fim - inicio}')
