class Conta:
    def __init__(self,numero, titular, saldo, limite = 1000.0):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print('O seu saldo é R${}'.format(self.__saldo))



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

    
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        print('O seu limite é R${}'.format(self.__limite))

    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    
conta = Conta(1,'will',100)
conta2 = Conta(2,'willian',100)

conta.limite = 2500
conta.limite
