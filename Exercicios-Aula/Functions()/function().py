#principal
def soma(n1, n2):
    s = n1 + n2
    return s

def subtracao(n1, n2):
    sub = n1 - n2
    return sub

def multiplicacao(n1, n2):
    mult = n1 * n2
    return mult

def divisao(n1, n2):
    div = n1 / n2
    return div

n1 = int(input('N1: '))
n2 = int(input('N2: '))
imprimir = print
imprimir('\nSoma:', soma(n1, n2))
imprimir('Subtração:', subtracao(n1, n2))
imprimir('Multiplicação:', multiplicacao(n1, n2))
imprimir('Divisão:', divisao(n1, n2))
