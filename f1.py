#def msg():
 #  print("Bem-vindo às funções")
 #  print("Em Python")*/

#2msg()#chamando a função

def nome(name):
    print(f"Bem-vindo {name}")
    nome("Ana Caroline")#chamando a função com parâmetro

#nome(input("Digite o nome: "))#chamando a função com input

def soma(n1, n2):
    return n1 + n2
#(" A soma é: ", soma(int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: "))))#chamando a função com return e input
v1 = int(input("Digite o primeiro número: "))
v2 = int(input("Digite o segundo número: "))
s = soma(v1, v2)
print(s)
#print(soma(v1, v2))#chamando a função com return e variáveis