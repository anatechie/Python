#Se os dados forem mensagens eles tem delimitadores especiais. Por exemplo, "Olá Mundo!" é composto
#por letras números, acentos etc. Tudo que for aparecer, é uma mensagem que vai aparecer na tela. O
#delimitador padrão do Python para isso são as aspas (""). No caso do Python, pode ser utilizado aspas
#duplas ou aspas comuns. A comunidade Python utiliza das aspas simples aspas simples.
#Para o Python3, todos os comandos são funções, então toda função tem que ter parenteses. Os parenteses
#podem ser utilizados com qualquer função. Ex.: Print(''). Nessa função pede-se ao interpretador
#Python para que seja escrito na tela o que está dentro das aspas. 

#Caso seja apresentado número, eles não serão colocados entre aspas, pois não são mensagens; são números

#Qual a diferença entre mensagem e número? 
#As mensagens são usadas para serem exibidas na tela, já os números são usados para fazer calculos. 
#Ex.: 7 + 4. Para que esses números sejam escritos na tela, a função Print() precisa estar presente!
#Print(7 + 4) -> nesse exemplo seria mostrado o resultado
#Print('7 + 4') -> nesse exemplo mostraria o sete seguido do 4, ou seja, 74.
#O operador + está agindo como concatenador, ou seja, ele junta duas frases para formar uma.
#
'''print('Olá mundo')'''

'''print(7 + 4)'''
'''print('7 + 4')'''
'''print('7' + '4')'''

'''print('Olá', 11)''' # Há exeções em que o + funciona melhor que a virgula,ou vice-versa

from email.errors import InvalidDateDefect

#VARIAVEIS ''' são espaços na memória onde se é possível guardar dados '''
'''NO PYTHON TODA VARIAVEL É UM OBJETO'''
#Toda variavel pode receber valores, o sinal para demonstrar isso é atravez do operador de igualdade =
nome = 'Fulanildes'
idade = 999
peso = 100.

'''print(nome, idade, peso)
print('---------------')
print(nome + idade + peso)'''
nome = input ('Qual é seu nome?')
idade = input ('Quantos anos você tem?')
peso = input ('Informe seu peso: ')
'''Input é a função que lê o que vai ser escrito pelo print'''
print(nome, idade, peso)
