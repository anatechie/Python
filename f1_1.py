def fun():
    print("---------------------------"*1)
    print("|    Funções em Python      |")
    print("---------------------------"*1)

fun()#chamando a função

def far(temp):
    return ((temp - 32) *(5/9))
print(f"A temperatura é {far(float(input('Digite a temperatura em Fahrenheit: '))):.2f}")