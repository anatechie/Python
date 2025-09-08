#3. Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com 
#valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(*num):
    maior_numero = (lambda nums: max(nums))(*num)
    return maior_numero

num =[12, 5,9,80]
maior_numero = maior(num)

print(f"O maior número é: {maior_numero}")