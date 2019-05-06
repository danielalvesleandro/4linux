#!/usr/bin/python3




###24.04.2019###

#######################################################################
# Interpolação de strings (.format)
#######################################################################

lista_de_usuarios = [
  {
    "nome": "qMHHOwoAaYECgB",
    "idade": 49,
    "email": "yMEpqGsegWXw@4linux.com",
    "sexo": "?",
    "endereco": "Rua NIbCtFYJpZtRJg"
  },
  {
    "nome": "GJBxVjGYtVEqmRasx",
    "idade": 23,
    "email": "mBZWAcaUDCVioOQEdIu@4linux.com",
    "sexo": "?",
    "endereco": "Rua VFJGPBuNRnz"
  },
  {
    "nome": "TFeiNzjMuAfyYHksx",
    "idade": 39,
    "email": "BEjDyrdxPJoniHIDFgZ@4linux.com",
    "sexo": "?",
    "endereco": "Rua AEhMBiFAuGgSAiuIyx"
  },
  {
    "nome": "EguHnoFTrUAuUUoery",
    "idade": 37,
    "email": "QzqgJRboorIzKjKp@4linux.com",
    "sexo": "?",
    "endereco": "Rua LgktJSYDjo"
  },
  {
    "nome": "zDjQIfYyTwtzetXMJvDs",
    "idade": 25,
    "email": "CZBArUyyMa@4linux.com",
    "sexo": "F",
    "endereco": "Rua DEPwqBeLgyylX"
  },
  {
    "nome": "FDLtOesbqzdqzGe",
    "idade": 47,
    "email": "MakWfrgesmuBb@4linux.com",
    "sexo": "F",
    "endereco": "Rua qVLKGbVYOPRNTdrRYA"
  },
  {
    "nome": "xrffFndgNldHhb",
    "idade": 20,
    "email": "MUvdkHayaYULCTkSDH@4linux.com",
    "sexo": "F",
    "endereco": "Rua ZwkeJCYdeZgEcX"
  },
  {
    "nome": "RyfOocoNhyuEDSN",
    "idade": 50,
    "email": "ggQNSQvIOmDqZj@4linux.com",
    "sexo": "M",
    "endereco": "Rua kvvnDojQEMsHMXzc"
  },
  {
    "nome": "GAXCbICkOjzNZxU",
    "idade": 31,
    "email": "ClNJyJMhNfmTvyQxxYvQ@4linux.com",
    "sexo": "?",
    "endereco": "Rua yIParNvhlayIcGup"
  },
  {
    "nome": "wvaTNhfqPOlnt",
    "idade": 29,
    "email": "EwTJHbRTCrfYF@4linux.com",
    "sexo": "F",
    "endereco": "Rua bGCVdBFXSzcVBeLvKYUZ"
  },
  {
    "nome": "qhDBAYlbwaSMar",
    "idade": 27,
    "email": "AwDWEkwtZcGgaHlsaW@4linux.com",
    "sexo": "M",
    "endereco": "Rua hVYSkEHTmaBIJG"
  },
  {
    "nome": "fAZzfzvEySnSei",
    "idade": 44,
    "email": "wrzgKwORTAnliywEq@4linux.com",
    "sexo": "M",
    "endereco": "Rua cSdMqmMvebnTd"
  },
  {
    "nome": "HJBLhUuMHeAogrtbeq",
    "idade": 47,
    "email": "akKkICosKJbUdVcLTCnQ@4linux.com",
    "sexo": "F",
    "endereco": "Rua IhyoOwKTUCQlBvDuVVYS"
  },
  {
    "nome": "vEeSluRuOmIJTFrgNA",
    "idade": 35,
    "email": "wrCGKAsQRlWLKUSH@4linux.com",
    "sexo": "?",
    "endereco": "Rua ZRfcRxPsJPO"
  },
  {
    "nome": "OyehQbxCsnSGPBLcviBs",
    "idade": 23,
    "email": "fnndYbeFLPmhB@4linux.com",
    "sexo": "?",
    "endereco": "Rua cnquXCCUji"
  },
  {
    "nome": "JDZdCgzulyGWW",
    "idade": 30,
    "email": "brPbOrQBWfIBikDA@4linux.com",
    "sexo": "M",
    "endereco": "Rua HgtuwqKeMin"
  },
  {
    "nome": "MoinSGxEySEgrb",
    "idade": 36,
    "email": "qolygpBXCKEeur@4linux.com",
    "sexo": "?",
    "endereco": "Rua xoVGMdTrFKHboQRzFd"
  },
  {
    "nome": "XStrcVVPyieJJznYZ",
    "idade": 49,
    "email": "doKMuRYdKwolzgkq@4linux.com",
    "sexo": "M",
    "endereco": "Rua jeTpYoJAHnSeWAUWG"
  },
  {
    "nome": "uWVZbFSfdE",
    "idade": 30,
    "email": "WpRAukMAAygh@4linux.com",
    "sexo": "?",
    "endereco": "Rua QQvsljaHXnhqjHlg"
  },
  {
    "nome": "jgVjBVFVVKui",
    "idade": 43,
    "email": "SCUVGmVBRpREfAMIleo@4linux.com",
    "sexo": "?",
    "endereco": "Rua ioMdZJPBgdMUzWsDg"
  }
]

TEMPLATE = '{nome};{idade};{email};{sexo};{endereco};'

for usuario in lista_de_usuarios:
    if usuario['idade'] > 30:
        usuario_formatado = TEMPLATE.format(
            nome=usuario['nome'],
            idade=usuario['idade'],
            email=usuario['email'],
            sexo=usuario['sexo'],
            endereco=usuario['endereco'])
        print(usuario_formatado)             


#######################################################################
# Interpolação de strings (.format)
#######################################################################
exit()
mensagem = 'Ola {}, {}'
mensagem = mensagem.format(
    'seja bem vindo ao mundo do Python',
    'Daniel Alves Leandro'
)
print(mensagem)

#ou

mensagem = 'Ola {nome}, {boasvindas}'
mensagem = mensagem.format(
    boasvindas='seja bem vindo ao mundo do Python',
    nome='Daniel Alves Leandro'
)
print(mensagem)

mensagem = 'Ola {nome}, seja bem vindo ao mundo do Python'
mensagem = mensagem.format(nome='Daniel Alves Leandro')
print(mensagem)

#ou

mensagem = 'Ola {}, seja bem vindo ao mundo do Python'
mensagem = mensagem.format('Daniel Alves Leandro')
print(mensagem)

#######################################################################
# Ficha / Itens
#######################################################################
exit(0)

lista = [0, 1, 2, 3, 'Daniel Alves Leandro']
lista[4] #Daniel Alves Leandro

ficha = {
    'nome': 'Daniel Alves Leandro',
    'idade': 32,
    'email': 'daniel.leandro@outlook.com.br',
    'parentes': [
        {
            'nome': 'Adriano Alves Leandro',
            'idade': 40,
            'email': 'adrianokgid@gmail.com',
        },

        {
            'nome': 'Marcos Alves Leandro',
            'idade': 37,
            'email': 'marcos@gmail.com',
        },
    ]
}

print (ficha['parentes'][1]['nome'])

#######################################################################
# Sequência de Fibonacci com laço FOR
#######################################################################
# Fibonacci
# 0 1 1 2 3 5 8 13 21 34
# f(n) = f(n-1) + f(n+-2), se n > 1
# 1 se n <= 1

exit()
n = 5
i = 0
j = 1
fib = 0

# obrigado a definir uma variável (X) para receber o valor atual da interação
for x in range(n):
    j, i = i + j, j
    print(j) #fib = j
    # identacao do print no escopo do conteudo do for, na linha do for printa soh o 8]

#ou

exit()
n = 5
i = 0
j = 1
fib = 0

for x in range(n):
    fib = i + j
    i = j
    j = fib
    print(fib)

#######################################################################
# Laço FOR  / Printa letras da frase / Printa números pares
#######################################################################
exit()
for letra in 'Daniel Alves Leandro':
        print(letra)


lista_de_numeros = [ 0, 1, 2, 3, 4, 5, 6, 7 ]
for numero in lista_de_numeros:
    if numero % 2 == 0:
        print(numero)

#######################################################################
# Print Texto / Condição com IF
#######################################################################
exit()
print('Hello, world')

nome = input('Qual é a melhor linguagem de programação? ')

if nome == 'python':
    print('Voce acertou')
    print('Parabens')
else:
    print('Errou :(')
    print('Burro')