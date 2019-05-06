
# import pymongo

# client = pymongo.MongoClient(host='localhost')

# print('Conectado ao banco com sucesso')

# db = client.estrela
# db.dono.insert({
#     'nome': 'Paulo'
# })

# for dono in db.dono.find():
#     print(dono)


import pymongo

client = pymongo.MongoClient(host='localhost')

print('Conectado ao banco com sucesso')

db = client.lyon

for usuario in db.usuarios.find():
    print(usuario)