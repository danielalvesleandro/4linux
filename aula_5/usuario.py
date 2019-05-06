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