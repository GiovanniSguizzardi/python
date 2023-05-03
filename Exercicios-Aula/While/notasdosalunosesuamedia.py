print('X Alunos e sua media aritmetica:\n')

alunos = 0
notas = 0
notas_totais = 0
continuar = int(input('Quantos alunos deseja cadastrar: '))

while alunos != continuar:
    alunos += 1
    notas = float(input('Nota: '))
    notas_totais += notas

media = notas_totais/continuar
print(f'MediaAritmetica: {media}')
    
    
