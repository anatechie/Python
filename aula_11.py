'''Elabore um programa onde o usuário informará um número  inteiro, por exemplo 7.
O programa retornará:
1        7 
2        6
3        5 
BINGO BINGO 
5        3
6        2
7        1'''

print('-----------------')
print('       BINGO          ')
print('-----------------')

num = int(input('Informe um número: ')) #entrada de dados
#a = 1
#b = num
#while a <= num : #contar de 1 até o número informado
#    print(a) 
#    print(b)
 #   a += 1
   # b -= 1

#b = num # contar do número informado até 1 
#while b >= 1:
     #   print (b)
     #   b -= 1


a = 1
b = num
while a <= num : #contar de 1 até o número informado
     if a == b:
       print('BINGO')
     else: 
        print(a,b)
a += 1
b -= 1
   
 

    

#4º passo, apenas um while
#b = num # contar do número informado até 1 
#while b >= 1:
     #   print (b)
     #   b -= 1











 
