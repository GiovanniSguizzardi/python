print("Classificador de Triangulo")
a = int(input("➤ Digite um número: "))
b = int(input("➤ Digite outro número: "))
c = int(input("➤ Digite um terceiro número: "))
print('\n')
isosceles = False
if isosceles == a == b != c or a != b == c or a == c != b:
    isosceles = True
    
if isosceles == True:
    print("[!] Triangulo isósceles")
    print("&")
else:
    print(".")

if a >= b+c:
    print("[✘] Não forma triângulo")

elif a**2 == b**2 + c**2:
    print("[!] Triangulo retângulo")

elif a == b == c:
    print("[!] Triangulo equilátero")

elif a**2 == b**2 + c**2:
    print("[!] Triangulo retângulo")

elif a**2 > b**2 + c**2:
    print("[!] Triangulo obtusângulo")

elif a**2 < b**2 + c**2:
    print("[!] Triangulo acutângulo")
