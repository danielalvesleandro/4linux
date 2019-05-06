import pymongo

client = pymongo.MongoClient(host='localhost')
db = client.chocolate

def cadastrar_usuario(nome, email):
    '''
        Esta função cadastra um usuário no banco
    '''
    return db.usuarios.insert({
        'nome': nome,
        'email':  email
    })

def cadastrar_time(time):
    '''
        Esta função cadastra um time no banco
    '''
    return db.times.insert({
        'nome': time,
    })

def cadastrar_torcedor(nome, email, time):
    '''
        Esta função cadastra um torcedor
    '''
    torcedor = dict(db.usuarios.find_one({'email': email}))
    if not torcedor:
        db.usuarios.insert({
            'nome': nome,
            'email': email,
            'time': time
        })
    else:
        torcedor['time'] = time
    db.usuarios.update({ 'email': email }, torcedor)

nome = input('Digite seu nome: ')
email = input('Digite seu email: ')
time = input('Digite seu time de coração: ')

cadastrar_usuario(nome, email)
cadastrar_torcedor(nome, email, time)


print('Usuário {} cadastrado com sucesso'.format(nome))