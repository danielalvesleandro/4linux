
# EXERCICIO 2:
# Dada uma lista de números
# escrever um algoritmo que calcula
# a média dos números nesta lista
# salvar em uma variável e imprimir

lista_de_numeros = [ 1, 2, 3, 4, 5, 6 ]
soma = 0
tamanho = 0
media = 0

for numero in lista_de_numeros:
    
    soma = soma + numero
    #soma += 1
    tamanho = tamanho + 1
    #tamanho += 1
    media = soma / 2

print(media)
    
# exit()
# qtde_numeros
# qtde_numeros = lista_de_numeros[]