import unittest

def soma(x, y):
    return x + y

def sub(x, y):
    return x - y

def gerar_lista_par(n):
    lista_de_numeros = []
    x = 1
    while x <= n:
        if x % 2 == 0:
            lista_de_numeros.append(x)
        x = x + 1
    return lista_de_numeros

class Testes(unittest.TestCase):

    def test_soma(self):
        resultado = soma(5, 5)
        self.assertEqual(resultado, 10)

    def test_sub(self):
        resultado = sub(5, 5)
        self.assertEqual(resultado, 0)

    def test_gerar_lista_par(self):

        def par(x):
            return x % 2 == 0

        for numero in gerar_lista_par(5012):
            self.assertTrue(par(numero))

unittest.main()