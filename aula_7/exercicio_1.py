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

print('Conectado ao banco de dados')

cursor.execute('SELECT * FROM usuarios ORDER BY id;')

for usuario in cursor.fetchall():
    print(usuario)

inserir_caracter_em_string = 'Mensagem: {} ||||'.format('Eu vou no lugar das chaves')

query_de_insercao = '''
    INSERT INTO usuarios (nome, email)
    VALUES ( 'Marcos Alves Leandro', 'marcos@gmail.com' );
    '''

#cursor.execute(query_de_insercao)
#conn.commit()
















