'''print('---------------------------------')
print('MASTER CALC 2024 - TURBO EDITION')
print('---------------------------------')
n1 = int(input('Informe o primeiro número: '))
op = input('Informe a opção: (+, -,* , /, %): ')
n2 = int(input('Informe o segundo número: '))
print('---------------------------------')


if op == '+':
    print(f'O resultado da adição é: {n1 + n2}')
    print('---------------------------------')
elif op == '-':
    print(f'O resultado da subtração: {n1 - n2}')
    print('---------------------------------')
elif op == '*':
    print(f'O resultado da multiplicação:  {n1 * n2}')
    print('---------------------------------')
elif op == '/':
    print(f'O resultado da divisão: {n1 / n2}')
    print('---------------------------------')
else:
    print(f'O resto da divisão é: {n1  % n2}')
'''

print('---------------------------------')
print('MASTER CALC 2024 - TURBO EDITION')
print('---------------------------------')
n1 = int(input('Informe o primeiro número: '))
op = input('Informe a opção: (+, -,* , /, %): ')
n2 = int(input('Informe o segundo número: '))
print('---------------------------------')

if op =='+':
    resultado = n1 + n2
elif op == '-':
    resultado = n1 - n2
elif op == '*':
    resultado = n1 * n2
elif op == '/':
    resultado = n1 / n2
else: 
    resultado = False
    if resultado:
        print(f'O resultado é: {resultado}')
    else: 
        print('Operação Inválida') 

        #import os
        ''' os.system('cls') 
        print(teste)'''