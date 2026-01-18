from Modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self.ativo}'
    @classmethod
    def liste_r(cls):
        print(f'{'Nome restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_av).ljust(25)} | {restaurante.ativo}')
    def liste_c(self): # Use self, pois queremos as avaliações DESTE restaurante
        print(f'Avaliações do restaurante {self._nome}')
        print(f"{'Cliente'.ljust(25)} | {'Nota'}")
        for avaliacao in self._avaliacao:
            print(f'{str(avaliacao._cliente).ljust(25)} | {avaliacao._nota}')
    @property
    def ativo(self):
        return '☒' if self._ativo else '☐'
    def alt_estado(self):
        self._ativo = not self._ativo
    def recebe_av(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
    @property
    def media_av(self):
        if not self._avaliacao:
            return '-'
        soma_nota = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quant_nota = len(self._avaliacao)
        media = round(soma_nota / quant_nota, 1)
        return media