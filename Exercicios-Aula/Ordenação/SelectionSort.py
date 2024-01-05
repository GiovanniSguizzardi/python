#Selection Sort - busca pelo menor indice
#Complexidade: 0(n2)

def selectionSort(seq):
    for i in range(len(seq)):
        min_index = i
        for j in range(i+1, len(seq)):
            #seleciona o menor elemento em cada interação
            if seq[j] < seq[min_index]:
                min_index = j
        #troca os elementos - atribuição paralela
        seq[i], seq[min_index] = seq[min_index], seq[i]

#Programa principal
lista = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
print(f'Lista original: {lista}')
selectionSort(lista)
print(f'Lista ordenada: {lista}')
