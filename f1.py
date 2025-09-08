#def msg():
 #  print("Bem-vindo às funções")
 #  print("Em Python")*/

#2msg()#chamando a função

#def nome(name):
#    print(f"Bem-vindo {name}")
#    nome("Ana Caroline")#chamando a função com parâmetro

#nome(input("Digite o nome: "))#chamando a função com input

#def soma(n1, n2):
 #   return n1 + n2
#(" A soma é: ", soma(int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))))#chamando a função com return e input
#1 = int(input("Digite o primeiro número: "))
#v2 = int(input("Digite o segundo número: "))
#s = soma(v1, v2)
#print(s)
#print(soma(v1, v2))#chamando a função com return e variáveis


#EXERCICIO 1
#Cria uma função para calcular as quatro operações da matematica(soma, subtração, multiplicação 
#e divisão)sendo fornecidos 2 números e informando o resultado de cada operação.)

def op(n1, n2):
    print(f"A soma é: {n1 + n2}")
    print(f"A subtração é: {n1 - n2}")
    print(f"A multiplicação é: {n1 * n2}")
    print(f"A divisão é: {n1 / n2:.2f}")  # Mostra a divisão com 2 casas decimais

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
op(a, b)








