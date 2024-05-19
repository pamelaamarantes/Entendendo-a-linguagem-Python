from Restaurante import Restaurante
from bebidas import Bebidas
from pratos import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebidas ('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)


def main():
    #print(prato_paozinho)
    #print(bebida_suco)
    restaurante_praca.exibir_cardapio



if __name__ == '__main__':
    main()