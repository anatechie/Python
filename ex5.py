#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado 
#pelo usuário


def qntDigito ():
    numero = input("Digite um número inteiro: ")

# Verifica se o número é composto apenas por dígitos
    if numero.isdigit():
        quantidade = len(numero)
        print(f"O número possui {quantidade} dígito(s).")
    else:
        print("Entrada inválida. Por favor, digite um número inteiro.")

qntDigito()