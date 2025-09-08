#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno 
#retangular (largura e comprimento) e mostre a área do terreno. 

def area():
    largura = 70.5
    comprimento = 50

    #funcao lambda para calculo 
    calcArea = lambda largura, comprimento : largura * comprimento

    area = calcArea(largura, comprimento)

    #.2f formata para 2 casas decimais
    print(f"A area do terrehno é: {area:.2f}m².")