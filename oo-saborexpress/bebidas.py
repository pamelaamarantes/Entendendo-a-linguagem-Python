from item_cardapio import ItemCardapio


class Bebidas(ItemCardapio):
    def __init__(self,nome, preco, tamanho):
        super().__init__(nome,preco) #super permite que acessamos informações de outras classes
        self.tamanho = tamanho


    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)