import pymongo

client = pymongo.MongoClient(host='localhost')
db = client.cadastro

def cadastrar_usuario():
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    idade = int(input('Digite sua idade: '))

def listar_usuarios():
    for u in db.usuarios.find():
        print(u)

def salvar_csv():
    arquivo = open('relatorio.csv', 'w')
    for u in db.usuarios.find():
        arquivo.write('{};{};{}:'.format(
            u['nome'],
            u['email'],
            u['idade']
        ) + '\n')
    arquivo.close

done = False
while not done:

    print('1 - Criar usuário')
    print('2 - Listar usuários')
    print('3 - Salvar CSV')

    option = int(input('Selecione uma das opções acima: '))

    if option == 1:
        cadastrar_usuario()
    elif option == 2:
        listar_usuarios()
    elif option == 3:
        salvar_csv()
    else:
        done = True

print('Xau :)')