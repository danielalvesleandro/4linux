# EXERCICIO 1:
# Imprima somente os usuários cujos emails contenham as letras:
# 'a' ou 'k' ou 'm' ou 'l'
# e cujas idades sejam maior que 30 e menor que 40

# Dica do exercicio

#Condicoes OU
#if 2 < 4 or 5 < 10:
#    print('Condição OU')

#Condicoes #
#if 2 < 4 and 5 < 10:
#    print('Condição AND')

# Testar se uma letra está e muma string
#if 'c' in 'LuCaS'.lower():
#    print('Lucas tem C')

# Obs: A funcao lower() converte uma string
# para letra minuscula
#print('LUCAS'.lower()) # Imprime 'lucas' tudo minusculo

#condicao_1 = 'c' in 'Lucas'
#condicao_2 = 2- < 40

#if condicao_1 and condicao_2:
#        print('opaa')

# SOLUÇÃO 1
import banco

TEMPLATE = '{nome};{idade};{email};{sexo};{endereco};'

for usuario in banco.lista_de_usuarios:
    
    email = usuario['email'].lower()
    idade = usuario['idade']
    
    condicao_1 = 'a' in email
    condicao_1 = condicao_1 or 'k' in email
    condicao_1 = condicao_1 or 'm' in email
    condicao_1 = condicao_1 or 'l' in email

    condicao_2 = idade > 30 and idade < 40

    if condicao_1 and condicao_2:
        usuario_formatado = TEMPLATE.format(
            nome=usuario['nome'],
            idade=usuario['idade'],
            email=usuario['email'],
            sexo=usuario['sexo'],
            endereco=usuario['endereco'])
        print(usuario_formatado)

exit()
# SOLUÇÃO 2
# print(     )
for usuario in banco.lista_de_usuarios:
    
    email = usuario['email'].lower()
    idade = usuario['idade']

    condicao_1 = False
    letras = [ 'a', 'k', 'm', 'k']
    for letra in letras:
        condicao_1 = condicao_1 or letra in email
    
    condicao_2 = idade > 30 and idade < 40
    
    if condicao_1 and condicao_2:
        print(usuario)