#def definir função ou declarar
#função subprograma, objetivo reuso
def hello():
    print('Olá')
# chamada de função
hello()
# basta definir uma vez para que possa ser reutilizado

def ola ( nome, idade):
    print(f'Olá{nome} - idade: {idade}')

var_nome = input('nome: ')
var_idade = int(input('idade: '))

ola(var_nome, var_idade)
