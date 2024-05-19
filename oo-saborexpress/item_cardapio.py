from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod #polimorfismo se moldar de forma diferente em diferentes classes 
    def aplicar_desconto(self):
        pass
