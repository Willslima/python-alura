class Conta:
    def __init__(self,numero, titular, saldo, limite = 1000.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print('O seu saldo é R${}'.format(self.saldo))

    def extrato_limite(self):
        print('O seu limite é R${}'.format(self.limite))

    def deposito(self, valor):
        self.saldo += valor
        print('Agora o seu saldo é {}'.format(self.saldo))

    def saque(self, valor):
        self.saldo -= valor
        print('Agora o seu saldo é {}'.format(self.saldo))

conta = Conta(1,'will',100)

print(conta.titular)

conta.extrato()

conta.deposito(150)

conta.saque(50)

conta.extrato_limite()
