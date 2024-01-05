import random
#Bubble Sort
#Complexidade: 0(n2)

def bubbleSort(seq):
    tam = len(seq)

    for i in range(tam-1):
        troca = False
        for j in range(0, tam-i-1):
            if seq[j] > seq[j+1]:
                troca = True
                seq[j], seq[j+1] = seq[j+1], seq[j]
                
#Se não for necessario mais realizar trocas, então forçamos a saida do loop
        if not troca:
            return

#Programa Principal
lista = [39, 12, 18, 85, 72, 10, 2, 18]
print(f'Lista Original: {lista}')
bubbleSort(lista)
print(f'Lista ordenada: {lista}')
