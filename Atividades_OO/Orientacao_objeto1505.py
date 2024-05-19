class Restaurante:
    restaurantes =  []
    def __init__(self,nome,categoria):
        self._nome = nome
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome}  | {self.categoria}'
    

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(27)}|{'Categoria'.ljust(26)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)}  | {restaurante.categoria.ljust(25)} | {restaurante._ativo}')

    def alterar_status(self):
        self._ativo = not self._ativo
        
@property
def ativo(self):
    return 'verdade' if self._ativo else 'falso'

    

restaurante_praca = Restaurante('Praça','Gourmet')
restaurante_praca.alterar_status()
restaurante_pizza = Restaurante('Pizza Express','Italiana')

Restaurante.listar_restaurantes()





