import datetime

'''
    Para que a catraca seja liberada, 
    o ticket deve estar DENTRO DO PRAZO
    de validade, ter saldo maior do que 4 reais, 
    e pertencer à concessionária.
'''

########################################################################
# Execões
########################################################################

class ExpiredTicketError(Exception):
    pass

class InsuficienteFundsError(Exception):
    pass

class ConcessionariaInvalidError(Exception):
    pass

########################################################################
# Constantes
########################################################################

PRECO_PASSAGEM = 4.00

########################################################################
# Classes
########################################################################

class Ticket:

    def __init__(self, validade, saldo, concessionaria):
        self.validade = validade
        self.saldo = saldo
        self.concessionaria = concessionaria


class Catraca:

    def __init__(self, concessionaria):
        self.concessionaria = concessionaria
        self.estado = 'trancada'

    def liberar(self, ticket):
        
        if ticket.validade < datetime.datetime.now():
            raise ExpiredTicketError
        
        if ticket.saldo < PRECO_PASSAGEM:
            raise InsuficienteFundsError

        


        
        
        ticket.saldo -= PRECO_PASSAGEM
        self.estado = 'liberada'

    def liberada(self):
        if self.estado != 'trancada':
            return True 
        return False

if __name__ == '__main__':

    try:
        
        validade = datetime.datetime.now() - datetime.timedelta(days=2)
        saldo = 100.00
        concessionaria = 'sptrans'

        ticket = Ticket(validade, saldo, concessionaria)

        catraca = Catraca(concessionaria='sptrans')
        catraca.liberar(ticket)

    except ExpiredTicketError:
        print('Teste de ticket vencido ok')

    try:    

        validade = datetime.datetime.now() + datetime.timedelta(days=365)
        saldo = 3.00
        concessionaria = 'sptrans'

        ticket = Ticket(validade, saldo, concessionaria)

        catraca = Catraca(concessionaria='sptrans')
        catraca.liberar(ticket)

    except InsuficienteFundsError:
        print('Teste de ticket sem saldo ok')


    try:    

        validade = datetime.datetime.now() + datetime.timedelta(days=365)
        saldo = 3.00
        concessionaria = 'emtu'

        ticket = Ticket(validade, saldo, concessionaria)

        catraca = Catraca(concessionaria='sptrans')
        catraca.liberar(ticket)

    except ConcessionariaInvalidError:
        print('Teste de ticket sem saldo ok')


    validade = datetime.datetime.now() + datetime.timedelta(days=365)
    saldo = 5.00
    concessionaria = 'sptrans'

    ticket = Ticket(validade, saldo, concessionaria)

    catraca = Catraca(concessionaria='sptrans')
    catraca.liberar(ticket)

    assert catraca.liberada() == True, 'Catraca nao sendo liberada'
    assert ticket.saldo == (saldo - PRECO_PASSAGEM), 'Ticket nao descontando valor'