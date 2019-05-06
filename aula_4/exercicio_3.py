# Exercício 3.1
# Decorator (função retornando função)

# def funcao_que_retorna_funcao():
#     def f():
#         return 10
#     return f

# funcao = funcao_que_retorna_funcao()
# valor = funcao()
# print(valor) # printa 10

# def soma(a, b):
#     return a + b

# apelido_da_soma = soma
# print(apelido_da_soma(2, 2))

# Exercício 3.2
# 

# def funcao (lista, callback):
#     for x in lista:
#         print(x)
#     callback()

# def avisar_que_terminou():
#     print('Opa.. terminou a lista...')

# def explodir_brasilia():
#     print('BUMMM')

# LISTA = [ 1, 2, 3, 4, 5 ]
# funcao(LISTA, avisar_que_terminou)
# funcao(LISTA, explodir_brasilia)

# Exercício 3.3
# Decorator (função retornando função)

def avisar_que_terminou():
    print('Opa.. terminou a lista...')

def funcao (lista, callback):
    for x in lista:
        print(x)
    callback()

def explodir_brasilia(fn):
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs)
        print('BUMM')
    return wrapper

@explodir_brasilia
def funcao(lista):
    for x in lista:
        print(x)

@explodir_brasilia
def qualquer_nome():
    print('qualquer coisa')

def tratar_excecao(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except:
            print('Opa.. deu ruim')
    return wrapper

funcao([ 1, 2, 3, 4, 5 ])
qualquer_nome()