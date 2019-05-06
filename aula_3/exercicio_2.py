BANCO_DE_DADOS = []
BANCO_DE_DADOS.append = ({
    'email': 'daniel.leandro@outlook.com.br',
    'idade': 32,
    'senha': 'password'
})

# define uma subclasse chamada InvalidEmailError
# da classe Exception para tratar os erros individualmente
class InvalidEmailError(Exception):
    pass
class InvalidAgeError(Exception):
    pass
class ExistentUserError(Exception):
    pass
class InvalidPasswordError(Exception):
    pass

def cadastrar_usuario():
    usuario = {
        'email': input('Digite seu email: '),
        'idade': int(input('Digite sua idade: '))
    }
    # encontra possíveis erros na criação do usuário
    if '@' not in usuario['email']:
        raise InvalidEmailError
    if '.' not in usuario['email']:
        raise InvalidEmailError
    if usuario['idade'] <= 0:
        raise InvalidAgeError
    # retorna o usuário criado
    #return usuario
    return{
        'email' = email,
        'idade' = idade,
        'senha': input('Digite sua senha: ')
    }

def cadastrar_usuario(usuario):
    # verificar se usuário já existe no banco
    for usuario_cadastrado in BANCO_DE_DADOS:
        if usuario_cadastrado['email'] == usuario['email']:
            raise ExistentUserError
    BANCO_DE_DADOS.append(usuario)

def verificar_senha(usuario):
    senha = input('Digite sua senha:')
    if usuario['senha'] != senha:
        raise InvalidPasswordError

try:
    usuario = cadastrar_usuario()
    cadastrar_usuario(usuario)
    print('Usuário cadastrado com sucesso')
except InvalidEmailError:
    print('Email inválido')
except InvalidAgeError:
    print('Idade inválida')
except ExistentUserError:
    print('Idade inválida')
except InvalidPasswordError:
    print('Senha inválida')



exit(0)

#(Não funcionou / corrigir)

# def cadastrar_usuario():
#     email: input('Digite seu email: ')
      
#     # encontra possíveis erros na criação do usuário
#     if '@' not in usuario['email']:
#         raise Exception({
#             'status_code': 400,
#             'message': 'Email invalido'
#         })
#     if '.' not in usuario['email']:
#         raise Exception({
#             'status_code': 400,
#             'message': 'Email invalido'
#         })

#     idade: int(input('Digite sua idade: ')

#     if usuario['idade'] <= 0:
#         raise Exception({
#             'status_code': 400,
#             'message': 'Email invalido'
#         })
#     # retorna o usuário criado
#     return {
#         'email' = email,
#         'idade' = idade
#     }

# try:
#     usuario = cadastrar_usuario()
#     print('Usuário cadastrado com sucesso')
# except Exception as err:
#     err = err.args[0]
#     print(err)
#     print('Código do erro: {}'.format(err['status_code']))
#     print('Mensagem: {}'.format(err['message']))

exit()
# def cadastrar_usuario():
#     usuario = {
#         'email': input('Digite seu email: '),
#         'idade': int(input('Digite sua idade: '))
#     }
#     # encontra possíveis erros na criação do usuário
#     if '@' not in usuario['email']:
#         raise Exception({
#             'status_code': 400,
#             'message': 'Email invalido'
#         })
#     if '.' not in usuario['email']:
#         raise Exception({
#             'status_code': 400,
#             'message': 'Email invalido'
#         })
#     if usuario['idade'] <= 0:
#         raise Exception({
#             'status_code': 400,
#             'message': 'Email invalido'
#         })
#     # retorna o usuário criado
#     return usuario

# try:
#     usuario = cadastrar_usuario()
#     print('Usuário cadastrado com sucesso')
# except Exception as err:
#     err = err.args[0]
#     print(err)
#     print('Código do erro: {}'.format(err['status_code']))
#     print('Mensagem: {}'.format(err['message']))


exit()
# def cadastrar_usuario():
#     usuario = {
#         'email': input('Digite seu email: '),
#         'idade': int(input('Digite sua idade: '))
#     }
#     # encontra possíveis erros na criação do usuário
#     if '@' not in usuario['email']:
#         raise Exception('Email inválido')
#     if '.' not in usuario['email']:
#         raise Exception('Email inválido')
#     if usuario['idade'] <= 0:
#         raise Exception('Idade menor do que zero.') 
#     # retorna o usuário criado
#     return usuario

# try:
#     usuario = cadastrar_usuario()
#     print('Usuário cadastrado com sucesso')
# except Exception as err:
#     print(err)