'''num = int(input('Informe um número: ')) 
i = 1
j= num
while i <= num:
    if i == j:
       print(f'{i} \t {j} \t*BISTECA*')
    else:
     print(f'{i} \t {j}')
    i += 1
    j -= 1'''

i = 0 
j=0
k=0
while i<10:
    i+=1

    j=i
    j*=2 
    k+= 1 
    while k>0:
        for i in range(11):
            j-=1
            if i%2==0:
                j+=2
            else:
                k-=2
                j+=1
                k-=1
                print(f'i: {i}, j: {j}, k: {k}')
                
'''Inicialização: i = 0, j = 0, k = 0.
Primeira iteração do while externo: i é incrementado para 1, j é definido como i (1) e depois multiplicado por 2 (2), k é incrementado para 1.
Loop interno while e for:
Para cada valor de i de 0 a 10, j é decrementado em 1.
Se i é par, j é incrementado em 2.
Se i é ímpar, k é decrementado em 2 e j é incrementado em 1, e k é decrementado em 1 novamente.
O loop interno continua até que k seja menor ou igual a 0.
O loop externo continua até que i seja menor que 10, e o processo se repete.
'''