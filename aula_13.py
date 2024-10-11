'''
Elabore uma lista de frutas que receba x elementos inseridospelo usuário e retorne a lista  informada
na ordem  inversa
'''
frutas = [] #É comum que as listas se iniciem sem nenhum valor. Como se fosse um papel em branco que
           #gradualmente você adiciona informações.
x = int(input('Informe a quantidade de frutas a serem inseridas: \t')) 
 #É comum que as listas se iniciem sem nenhum valor. Como se fosse um papel em branco que gradualmente
 #  você adiciona informações.                         
for i in range(x):
    fruta = input('Especifique a fruta a ser inserida: \t')
    frutas.append(fruta) #append adiciona uma item na lista
print(' ')
print(frutas)
print(' ')
print('--------------------------------------------------------')
print(' ')
print('--LISTA NA ORDEM REVERSA--')
print(' ')
for i in range(len(frutas)-1, -1, -1):
    print(frutas[i])


    '''
    
    '''