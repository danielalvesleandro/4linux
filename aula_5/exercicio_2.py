class ContaBancaria:  #classe
    
    def __init__(self):
        self.rendimento = 0.02
        self.quantidade = 0.00

    def sacar(self, quantidade):  # método
        if self.quantidade - quantidade > 0:

        print('Sacar {}'.format(quantidade))
    
    def depositar(self, quantidade):  # método
        print('Retirar {}'.format(quantidade))
    
    def calcular_rendimento(self):  # método
        print('Calculando rendimentos'

class ContaCorrente(ContaBancaria):  # subclasse / classe filha herdando da classe mãe
        def __init__(self):
        super().__init__()
        self.rendimento = 0.00

class ContaPoupanca(ContaBancaria):  # subclasse / classe filha herdando da classe mãe
    def __init__(self):
        super().__init__()
        self.rendimento = 0.05




