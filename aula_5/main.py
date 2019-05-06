import usuario

USUARIOS = []

def cadastrar_usuario():

    nome = input('Digite seu nome')
    email = input('Digite seu email')
    idade = int(input('Digite sua idade'))

    u = usuario.Usuario(nome, email, idade)  # módulo.Classe
    USUARIOS.append(u)

def listar_usuarios():
    with open('relatorio.csv', 'w') as arquivo:
        for u in USUARIOS:
            arquivo.write(str(u) + '\n')
        # arquivo = open('relatorio.csv', 'w')
        # arquivo.write(str(u) + '\n')   # write precisa do /n para imprimir um em cada linha
        # arquivo.close
        # ou    

    done = False
    while not done:
        
        print('1 - Criar usuário')
        print('2 - Listar usuários')
        print('3 - Salvar usuários (CSV)')

    option = int(input('Selecione uma das opções acima: '))

    if option == 1:
        cadastrar_usuario()
    elif option == 2:
        listar_usuario()
    else:
        done = True
    
