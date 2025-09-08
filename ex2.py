#def op(n1, n2):
#    print(f"A soma é: {n1 + n2}")
 #   print(f"A subtração é: {n1 - n2}")
#    print(f"A multiplicação é: {n1 * n2}")
#    print(f"A divisão é: {n1 / n2:.2f}")  # Mostra a divisão com 2 casas decimais

#a = int(input("Digite o primeiro número: "))
#b = int(input("Digite o segundo número: "))
#op(a, b)

#2. Criar uma função para retornar se um número se é par ou ímpar]

def verifica_num():
    num = int(input("Digite um número: "))

    if num % 2 == 0:
        print(f"O número {num} é par.")
    else:
        print(f"O número {num} é ímpar.")
verifica_num()