class Cliente:

    def __init__(self, nome):
        self.__nome = nome
    
    @property #Criando um getter
    def nome(self):
        return self.__nome.title()
    
    @nome.setter #Criando um setter
    def nome(self, nome):
        print('Chamando setter')
        self.__nome = nome.title()
        print('Nome agora é {}'.format(self.__nome))

cliente = Cliente('willian')


cliente.nome = 'will'
