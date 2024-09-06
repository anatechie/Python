#codigo fonte: onde é colocado a estrutura que será apresentada o programa
#Extensão: .py
#IDE? Vs Code
# Terminal -Editor de código
#Hello > saída de dados
# Variavel: alocação de espaço e memoria
#Elementos: nome, tipo, valor
#Principal regra: Não começar com número, começar com letra maiuscula, palavras reservadas 
#Saída formatada: print(f'teste {minha_var}')
#Estrutura de decisão: if 
#if > condição <:
#if >condição <:
#else
#if > condição <:
#     teste 
#elif > condição <:
#else:
#Operadores aritmeticos: + - * / %
#Operadores de atribuição: = += -= 
#Operadores lógicos: > < >=(maior) <=(menor) ==(igual) !=(diferente) and or not 

#limpar tela: import os 
#Para limpar tela: comando os.system('cls')
'''
print('-------------------')
print('|Exemplo incrimento|')
print('-------------------')
i = 2
while i <= 10:
    #print(i)
    print(f'{i} - teste ')
    i += 2
    '''

print('-------------------')
print('|Exemplo incrimento|')
print('-------------------')
i = 1
while i <= 50:
    if i <= 25:
       print(f'{i} - teste Parte I  ')
       print('-------------------')
    else:
        print (f'{i} - teste Parte II ')
        print('-------------------')
    i += 1


for i in range(1,11,13):
    print(i)