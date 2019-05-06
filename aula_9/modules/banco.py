import time             # primeiro módulos do python
import pymongo          # depois módulos terceiros

# from pymongo import MongoClient, DESCENDING
# import time
# try:
#     client = MongoClient()
#     db = client['chat'] # se não existe cria, se existe usa
# except Exception as e:
#     print('ERRO: {}'.format(e))
#     exit()

try:
    client = pymongo.MongoClient()
    db = client.chat
except Exception as err:
    print('ERRO: {}'.format(err))
    exit()

def cadastrar(nome, mensagem):
    db.chat.insert({
        'nome': nome,
        'mensagem': mensagem,
        'hora': time.strftime('%d-%m-%Y %H:%M:%S')
    })

def select():
    ultimo = [ x for x in db.chat.find().sort('_id', pymongo.DESCENDING) ]

    # ultimo = []
    # for x in db.chat.find().sort('_id', pymongo.DESCENDING)
    #     ultimo.append(x)

    while True:
        atual = [ x for x in db.chat.find().sort('_id', pymongo.DESCENDING)]
        if atual != ultimo:
            print('[{}] {} : {} \n'.format(
                atual[0]['hora'], atual[0]['nome'], atual[0]['mensagem']
            ))
            ultimo = atual
        time.sleep(2.0)
