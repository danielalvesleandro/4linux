
lista_de_usuarios = []

arquivo = open('relatorio.csv', 'r')
for linha in arquivo.readlines():
    registro = linha.split(';')
    usuario = {
            'nome': registro[0],
            'idade': registro[1],
            'email': registro[2],
            'sexo': registro[3],
            'endereco': registro[4],
    }

    lista_de_usuarios.append(usuario)

    arquivo = open('relatorio_2.csv', 'w')
    for usuario in lista_de_usuarios:
        arquivo.write(str(usuario) + '\n')



exit()

arquivo = open('relatorio.csv','r')
for linha in arquivo.readlines():
    print(linha)
arquivo.close()

# arquivo = open('usuarios.txt', 'r')
# for linha in arquivo.readlines():
#     print(linha)
# arquivo.close()

# arquivo = open('usuarios.txt', 'w')
# arquivo.write('Hello, world 2')

# arquivo = open('usuarios.txt', 'a')
# for i in range(100):
#     arquivo.write(str(i) + '\n')
#     print(str(i))

# arquivo = open('usuarios.txt', 'r')
# for linha in arquivo.readlines():
#     print(linha)
# arquivo.close()

