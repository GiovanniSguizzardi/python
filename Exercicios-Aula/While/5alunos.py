print('5 alunos e qual é o mais velho?')
print('-==-==-==-==-==-==-==-==-==-==--==-')

alunos = 0
idade = 0
idade_maior = 0
nome_maior = 0
sexo_maior = 0

while True:
    nome = input('Nome do aluno: ')
    idade = int(input('Idade do aluno: '))
    sexo = input('Sexo do aluno: ')
    print('-==-==-==-==-==-==-==-==-==-==--==-\n')
    alunos = alunos + 1

    if idade > idade_maior:
        idade_maior = idade
        nome_maior = nome
        sexo_maior = sexo

    if alunos == 5:
        print('Dados do aluno mais velho cadastrado:')
        print('Nome:',nome_maior,'\nIdade:',idade_maior,'\nSexo:',sexo_maior,)
        break
            
        
        
        
        
    
