class Conta:
    def __init__(self,numero, titular, saldo, limite = 1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('O seu saldo é R${}'.format(self.__saldo))

    def get_limite(self):
        print('O seu limite é R${}'.format(self.__limite))

    def deposito(self, valor):
        self.__saldo += valor
        print('Agora o seu saldo é {}'.format(self.__saldo))

    def saque(self, valor):
        self.__saldo -= valor
        print('Agora o seu saldo é {}'.format(self.__saldo))

    def transferir(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)
        
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular
    
    def set_limite(self, novo_limite):
        self.__limite = novo_limite
        return self.__limite
    
conta = Conta(1,'will',100)
conta2 = Conta(2,'willian',100)

conta.extrato()
conta.transferir(50,conta2)

conta.extrato()
conta2.extrato()

print(conta.get_saldo())
print(conta.get_titular())

conta.set_limite(2500)
conta.get_limite()