from Avaliacao_1605 import Avaliacao

#adicionando uma class e seus atributos
class Restaurante:
    restaurantes =  []
    def __init__(self,nome,categoria):
        self._nome = nome
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)
    def __str__(self):
        return f'{self._nome}  | {self.categoria}'
    
#realizando metodo de class e organizando as informações de acordo com cada item listado
    @classmethod
    def lista_restaurantes(cls):
        print(f'{"Nome do Restaurante".ljust(25)} | {"Categoria".ljust(25)} | {"Avaliação".ljust(25)} | {"Status"}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {str(restaurante.categoria.ljust(25))} | {str(restaurante.media_avaliacoes.ljust(25))} | {restaurante._ativo}')


    @property
    def ativo(self):
        return 'verdade' if self._ativo else 'falso'

    def alterar_status(self):
            self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)


    @property
    def media_avaliacoes(self): 
        if not self._avaliacao:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
Restaurante.lista_restaurantes()
restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.alterar_status()
restaurante_pizza = Restaurante('pizza express', 'Italiana')

                   
    

   



