def gerar_lista_par(n):
    lista_de_numeros = []
    x = 1
    while x <= n:
        if x % 2 == 0:
            lista_de_numeros.append(x + 1)
        x = x + 1
    return lista_de_numeros

# teste para pegar erros de runtime error
lista = gerar_lista_par(5012)
for numero in lista:
    assert numero != 0, 'numero não pode ser 0'.format(numero)
    assert numero % 2 == 0, '{} não é par'.format(numero)

print(gerar_lista_par(12))
print(gerar_lista_par(20))



# # EXERCÍCIO DE AQUECIMENTO 2

# # ESCREVER UMA FUNÇÃO QUE RECEBE UM NÚMERO
# # INTEIRO (1, 2 ,3 ,4 ,5) E RETORNA UMA
# # LISTA COM OS NÚMEROS PARES MENORES QUE N

# def gerar_lista_par(n):
#     lista_de_numeros = []
#     x = 1
#     while x < n:
#         if x % 2 == 0:
#             lista_de_numeros.append(x)
#         x = x + 1
#     return lista_de_numeros

# print(gerar_lista_par(12))
# print(gerar_lista_par(20))



# EXERCÍCIO DE AQUECIMENTO 1

# ESCREVER UMA FUNÇÃO QUE RECEBE UM NÚMERO
# INTEIRO (1, 2 ,3 ,4 ,5) E RETORNA UMA
# LISTA COM ESSES NÚMEROS, EXERCÍCIO
# gerar_lista(5) -> [ 1, 2, 3, 4, 5 ]
# gerar_lista(9) -> [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]

# def gerar_lista(n):
#     lista_de_numeros = []
#     x = 0
#     while x < n:
#         lista_de_numeros.append(x + 1)
#         x = x +1
#     return lista_de_numeros

# print(gerar_lista(5))
# print(gerar_lista(9))
