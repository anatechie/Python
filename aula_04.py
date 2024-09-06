'''print('Hello')
idade = 10 #int
nome = "Ana" #caractere
mensalidade = 789.87'''#float
#ctrl + alt + seta para baixo
'''print(idade)
print(nome)
print(mensalidade)
print(bloqueado)
print('---------------------------------')
print(idade)
print(idade)
idade = 20 * 3
print(nome)
print(mensalidade)
print(bloqueado)'''

#função sempre retorna algo
'''type(idade)#apresenta tipo 
print(type(idade))
print(type(nome))
print(type(mensalidade))
print(type(bloqueado))'''

#PRÓXIMO TÓPICO
'''idade = 10'''
#idade(type(idade))
#type() é uma função que retorna o tipo de uma variável
'''idade = int(input('Informe a idade: '))''' # imprime <class 'int'>
#A função int() é usada para converter uma string em um número 
# inteiro. Ela pega a string retornada por input() e tenta 
# convertê-la em um número inteiro.
'''idade = int(input('Informe a idade: '))
print(type(idade))'''

'''mensalidade = float(input('Informe a mensalidade: '))'''
#A função float() é usada para converter uma string em um número
'''print(type(mensalidade))
nome = str(input('Informe nome: '))
print(type(nome))'''
#A função str() é usada para converter uma string em uma string                                                                                                         
'''bloqueado = bool(input('Bloqueado?'))
print(type(bloqueado))'''
#A ausencia de valor é considerado false
'''print(idade)# tipo String
print('idade')
print('Informe a idade: ')

print('A idade informada foi: {idade}')
print(f'A idade informada foi: {idade}')

idade = idade + 18 #idade é String e 10 é inteiro 
print(f'Em 10 anos a pessoa terá {idade} anos de idade')'''
#input transforma as variaveis em String
#f-string é uma forma de concatenar strings e variáveis
#A variável idade é uma string e não pode ser somada com um número

#OPERADORES LOGICOS
'''print()
print()
print()
print()
print()'''

#ESTRUTURAS CONDICIONAIS
'''a = 20
if a > 10:
    print('A é maior que 10')

a = 9 
if True: 
    print('Palmeiras não tem mundial')'''

idade = int(input('Informe a idade: '))
if idade < 18: #if é um bloco, : marca a abertura dele
    print('Menor de idade')
else: #uma estrtura condicional retorna valor booleano
    print('Maior de idade')

#sempre usar => ou <= para evitar ter que fazer muitas comparações