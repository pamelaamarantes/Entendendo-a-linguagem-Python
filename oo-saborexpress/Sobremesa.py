from item_cardapio import ItemCardapio


class sobremesa(ItemCardapio):
    def __init__(self,tipo, tamanho,preco,descricao):
        super().__init__(tipo,tamanho) #super permite que acessamos informações de outras classes
        self.tamanho = tamanho
        self._preco=preco
        self.descricao = descricao
        self.tipo = tipo


    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.15)

    