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

def cadastrar_time(time):
    query1 = '''
        INSERT INTO times (nome)
        VALUES ('{}');
    '''.format(time)
    cursor.execute(query1)
    conn.commit()

def selecionar_torcedores(time):
    query2 = '''
        SELECT * from usuarios u 
        INNER JOIN rel_usuarios_times r
        ON u.id = r.usuario
        INNER JOIN times t
        ON r.time = t.id
        WHERE t.nome = '{}';
    '''.format(time)
    cursor.execute(query2)
    return list(cursor.fetchall())

time = input('Digite um time para cadastrar: ')
cadastrar_time(time)

time = input('Digite um time para selecionar torcedores: ')

for torcedores in selecionar_torcedores(time):
    print(torcedores)