import os

from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_lactea = Bebida('Leite', 5.0, 'Médio')
bebida_lactea.app_desconto()
prato_pao = Prato('Pão', 2.0, 'O mais genérico')
prato_pao.app_desconto()
restaurante_praca.add_cardapio(bebida_lactea)
restaurante_praca.add_cardapio(prato_pao)
#restaurante_praca.receber_avaliacao('Gui', 10)
#restaurante_praca.receber_avaliacao('Lais', 8)
#restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    #Restaurante.listar_restaurantes()
    os.system('cls')
    #print(bebida_lactea, prato_pao)
    restaurante_praca.mostra_cardapio

if __name__ == '__main__':
    main()