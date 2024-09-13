#print('VERIFICAÇÃO DE NÚMEROS PARES')
#num = int(input('Entre com um número: '))
#if num % 2 == 0:
#    print('O número {} é par'.format(num))
#else:
 #   print('O número {} é impar'.format(num))

'''Elabore um programa para cadastro de até 6 times de futsal para um torneio, com até 10 jogadores para cada time.
Os três times serão automaticamente nomeados como Time 1, Time 2 ...
Para jogadores, serão atribuidos automaticamente apenas o número da camisa, caso o número seja múltiplo de 3 aparecerá
o número acrescido de um patrocinador BET, por exemplo o jogador 3 ficará 3-BET
print('teste', end="")
print('teste', end='\n')
print('teste', end="")'''

print('CADASTRO TIME DE FUTSAL')
qnt_time = int(input('Informe a quantidade de times: '))
qnt_jogadores = int(input('Informe a quantidade de jogadores por time: '))
for t in range(1,qnt_time+1): #t variavel de contexto para o bloco, usada somente para interaçãoS
    print(f'Time {t}')
    for j in range(1,qnt_jogadores+1):
        if j % 3 == 0:
            print(f'{j}-BET ', end="")# parametro que sinaliza para que a linha não seja quebrada
        else:
         print(f'{j} ', end="")
    print(' ')
    
        

