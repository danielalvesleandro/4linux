# EXERCICIO 3:
# Dar prompt solicitando a idade do usuário
# validando e removendo caracteres inválidos
# da impressão

idade = input('Digite sua idade: ')
string_vazia = ''

caracteres_validos = '0123456789'

for letra in idade:
    if letra in caracteres_validos:
        string_vazia += letra

print(string_vazia)




exit()
idade = input('Digite sua idade: ')
#idade = int(idade)

caracteres_validos = '0123456789'

for letra in idade:
    if letra not in caracteres_validos:
        print('Você digitou errado!')
        exit()

print('Você digitou corretamente')
    