RED = "\033[1;31m"  
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
print('[-------------------]')
print('Calculo de Empréstimo')
print('[-------------------]')

nome = input('[*] Seu nome: ')
valor_emprestimo = float(input('[$] Valor do Empréstimo: '))
numero_parcelas = int(input('[&] Número de parcelas: '))
print(nome, ', a dívida será de: ', valor_emprestimo * numero_parcelas)
