import psycopg2
import psycopg2.extras

conn = psycopg2.connect(
    host='localhost',
    user='admin',
    password='4linux',
    database='projeto'
)
cursor = conn.cursor(
    cursor_factory=psycopg2.extras.RealDictCursor   # trabalha como dicionário, sem ele como tupla
)

def cadastrar_usuario(nome, email):
    query = '''
        INSERT INTO usuarios (nome, email)
        VALUES ('{}', '{}');
    '''.format(nome, email)
    cursor.execute(query)
    conn.commit()

nome = input('Digite seu nome: ')
email = input('Digite seu email: ')

cadastrar_usuario(nome, email)

print('Usuário {} cadastrado com sucesso'.format(nome))