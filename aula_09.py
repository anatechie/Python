#for i in range(1,10):
#1.for i in range(10):
#print(i)
#2.for i in range(1,11):
#print(f'valor de i {i}')
#3.for x in range(1,30,3):
#print(x)

'''Repetição'''
#99..1 utilizando estrutura for

'''for i in range(99, -1, -3):
    print(i)'''

#99..0 utilizando estrutura for

'''for i in range(1,10):
    print(i)
    i += 2'''

'''Elabora um programa  onde o usuário informará um valor e o programa deverá retornar
se o respectivo valor é múltiplo de 5 ou não

num=int(input('Entre com um número: '))
if num % 5 == 0:
    print('O número é múltiplo de 5')
else:
    print('O número não é múltiplo de 5')'''

'''Elabore um programa que realizará uma contagem de 1 até 100, nos múltiplos de 5 imprima M5
nos múltiplos de 10 imprima m10 e nos múltiplos de 15 imprima m15, para os demais valores imprima
o valor normalmente
Considere sempre o maior múltiplo:
ex.: Se o valor for 30'''

for cont in range(1,101):
    
    if cont % 15 == 0:
        print(f' - M15')
    elif  cont % 10 == 0:
        print(f' - m10')
    elif cont % 5 == 0:
        print(f' - m5')
    else:
        print(cont)


a = 20
b = 30
c = 2
d = 3
e = 37

for i in range(1,20):
    a += 1
    b -= 2
    c = a + b
    d = d + i 
    if i % 7 == 0:
       a -= 3
       d = a + b
    else: 
        e += 5

        '''teste de mesa'''
