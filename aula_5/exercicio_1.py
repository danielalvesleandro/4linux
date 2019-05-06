
# Criar uma classe chamada "Usuario" que 
# contém os atributos:
# - nome
# - email
# - idade
import datetime
class Usuario:
    def __init__( self, nome, email, idade, sala ):
        self.nome = nome # atributo
        self.email = email
        self.idade = idade
        self.sala = sala
        self.data_criacao = datetime.datetime.now()

    # def __str__(self):
    #     return '{}'.format(self.nome)

    def __str__( self ):
        return '{};{};{};{};{}'.format(
            self.nome,
            self.email,
            self.idade,
            self.sala,
            self.data_criacao
        )

    def maior_de_idade( self ):  # método maior_de_idade
        if self.idade > 17:
            return True
        return False

daniel = Usuario('Daniel Alves Leandro', 'daniel.leandro@outlook.com.br', 32, 'outra')
lucas = Usuario('Lucas Salles', 'lucas.salles@4linux.com.br', 15, 'linus')

print(daniel.maior_de_idade())
print(lucas.maior_de_idade())
print(lucas.nome, lucas.email, lucas.idade, lucas.sala, lucas.data_criacao)
print(lucas.data_criacao)
print(str(lucas))

#########################################################################


exit()
class Vetor:

    def __init__(self, x, y):    # parametro self carrega o estado do objeto / x/y estado do vetor
        self.x = x
        self.y = y

    def soma_das_componentes(self):
        return self.x + self.y

v = Vetor(5, 2) # v é um objeto da classe vetor
u = Vetor(2, 2)

v.x = 10
v.y = 20

print(u.x)