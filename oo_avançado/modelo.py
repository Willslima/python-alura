class Programa:
    def __init__(self, nome, ano, like = 0):
        self._nome = nome.title()
        self.ano = ano
        self._like = like
    
class Filme(Programa):
    def __init__(self, duracao):
        self.duracao = duracao

class Serie(Programa):
    def __init__(self, temporadas):
        self.temporadas = temporadas

la_casa_de_papel = Serie('la casa de papel',2017, 5)

vingadores = Filme('vigadores - guerra infinita', 2018, 160)

print(f'Nome: {vingadores.nome} - Duração: {vingadores.duracao} - Ano: {vingadores.ano}')

print(f'Nome: {la_casa_de_papel.nome} - Temporadas: {la_casa_de_papel.temporadas} - Ano: {la_casa_de_papel.ano}')