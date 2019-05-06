# Exercício 2.1
# lista_de_numeros = [ 1, 2, 3, 4, 5, 6, 7, ]

# def somar_lista_de_numeros(*args):
#     resultado_da_soma = 0
#     for numero in args:
#         resultado_da_soma += numero
#     return resultado_da_soma

# l = [ 1, 2, 3 ]
# resultado = somar_lista_de_numeros(*l)
# print(resultado)

# resultado = somar_lista_de_numeros(1, 2, 3)
# print(resultado)

# Exercício 2.2
# Escreva uma função que receba um número
# variável de nomes e retorne uma lista
# que contém L

# def extrair_usuarios_que_contem_ele(*args):
#     lista_de_nomes = []
#     for nome in args:
#         if 'l' in nome.lower():
#             lista_de_nomes.append(nome)
#     return lista_de_nomes

# lista = extrair_usuarios_que_contem_ele(
#     'Daniel',
#     'Marcos',
#     'Adriano',
#     'Miguel'
# )
# print(lista)

# Exercício 2.3
# 

# def criar_moto(tempo_do_motor, numero_marchas, *args):
#     return{
#         'tempo': tempo_do_motor,
#         'marcas': numero_marchas,
#         'marcas': list(args)
#     }

# criar_moto(2, 5, 'Honda')
# criar_moto(2, 5, 'Honda')
# criar_moto()
# criar_moto(2, 5, 'Honda', 'Yamaha', 'BMW')

# Exercício 2.4
# Um * abre listas, dois * abrem dicionarios

def calcular_media(*args):
    soma, quantidade = 0, 0
    for nota in args:
        soma, quantidade = soma + nota, quantidade + 1
    return soma / quantidade if quantidade > 0 else 0

def calcular_nota(**kwargs):
    for key in kwargs.keys():
        kwargs[key] = calcular_media(*kwargs[key])
    return kwargs

alunos = {
    'lucas': [10, 10, 10 ],
    'alex': [5, 3, 20]
}

medias = calcular_nota(**alunos)
print(medias)

