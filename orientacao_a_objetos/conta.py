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

    def __saque_disponivel(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saque(self, valor):
        if(self.__saque_disponivel(valor)):
            self.__saldo -= valor
            print('Agora o seu saldo é R${}'.format(self.__saldo))
        else:
            print("O valor solicitado de R${} é maior que o saldo/limite !!!".format(valor))

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

    @staticmethod
    def codigo_banco():
        return 'O código é 001'
    
conta = Conta(1,'will',100)
conta2 = Conta(2,'willian',100)

conta.limite = 500

print(Conta.codigo_banco())