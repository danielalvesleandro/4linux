import unittest
import datetime
import exercicio_2

class CatracaTest(unittest.TestCase):

        def test_validade(self):

            validade = datetime.datetime.now() - datetime.timedelta(days=365)
            saldo = 3.00
            concessionaria = 'sptrans'

            ticket = exercicio_2.Ticket(validade, saldo, concessionaria)

            catraca = exercicio_2.Catraca(concessionaria='sptrans')

            with self.assertRaises(exercicio_2.ExpiredTicketError):
                catraca.liberar(ticket)

if __name__ == '__main__':
    unittest.main()