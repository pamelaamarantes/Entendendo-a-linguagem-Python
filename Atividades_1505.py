
class restaurante:
    nome = ''
    categoria =''
    ativo = False
restaurante_praca = restaurante()
restaurante_pizza = restaurante()

restaurantes = [restaurante_praca,restaurante_pizza]

print(restaurante_praca.ativo)

#Atividades# 

# Acesse o valor do atributo nome da instância restaurante_praca da classe Restaurante

nome_restaurante = restaurante_praca.nome

# Verifique o valor inicial do atributo ativo para a instância restaurante_praca e exiba uma mensagem informando se o restaurante está ativo ou inativo

if restaurante_praca.ativo:
    print('O restaurante está ativo.')
else:
    print('O restaurante está inativo.')

# Acesse o valor do atributo de classe categoria diretamente da classe Restaurante.
categoria = restaurante.categoria

# Altere o valor do atributo nome para 'Bistrô'.

restaurante_praca.nome = 'Bistrô'

#Crie uma nova instância da classe Restaurante chamada restaurante_pizza com o nome 'Pizza Place' e categoria 'Fast Food'.

restaurante_pizza = restaurante()

restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'


#Verifique se a categoria da instância restaurante_pizza é 'Fast Food'.

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')


#Mude o estado da instância restaurante_pizza para ativo.

restaurante_pizza.ativo = True

#Imprima no console o nome e a categoria da instância restaurante_praca.
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')

#Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, 

class Musica:
    Musicas = []
    def __init__(self,nome,artista,duracao):
        self.nome = nome
        self.artista = artista   
        self.duracao = duracao     
        Musica.Musicas.append(self)
    def __str__(self):
        return f'{self.nome}  | {self.artista} | {self.duracao}'
    def listar_musicas():
        for Musicas in Musica.Musicas:
            print(f'{Musicas.nome}  | {Musicas.artista} | {Musicas.duracao}')
                  
                  
Musico_Homem = Musica('Afonso','Ator',60)
Musico_Mulher = Musica('Pamela','Atriz',10)

Musica.listar_musicas()

print(Musico_Homem)
print(Musico_Mulher)




#Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano.Crie uma instância dessa classe e atribua valores aos seus atributos.

class Carro:
    Carros = []
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

# Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos.Instancie um restaurante e atribua valores aos seus atributos.

class Restaurante1:
    Restaurantes1= []
    def __init__(self,nome, categoria,gerente, cidade,ativo=False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.gerente = gerente
        self.cidade = cidade
        
Restaurante_sp = Restaurante1(nome = 'PizzaBar',categoria = 'Pizza',ativo = False, gerente ='Rosely',cidade = 'São Paulo')

#Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

class NovoRestaurante:
    NovoRestaurantes = []
    def __init__ (self, nome, categoria,ativo= False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

NovoRestaurante_ex = NovoRestaurante(nome='MC', categoria='Fast Food')

#Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante

class NovoRestaurante:
    NovoRestaurantes = []
    def __init__ (self, nome, categoria,ativo= False):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        NovoRestaurante.NovoRestaurantes.append(self)
    def __str__(self):
        return f'{self.nome}  | {self.categoria} '
    def listar_NovoRestaurante():
        for NovoRestaurantes in NovoRestaurante.NovoRestaurantes:
            print(f'{NovoRestaurantes.nome}  | {NovoRestaurantes.categoria}')
                  
            

NovoRestaurante.listar_NovoRestaurante()
NovoRestaurante_ex = NovoRestaurante(nome='MC', categoria='Fast Food')
print(NovoRestaurante_ex)



#Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor

class Cliente:
    Clientes = []
    def __init__(self,nome,  idade, profissão, cidade):
        self.nome = nome
        self.idade = idade
        self.profissão = profissão
        self.cidade = cidade


Cliente1 = Cliente (nome = 'Alessandra', idade = 20, profissão = 'atriz', cidade = 'Rio de Janeiro')
Cliente2 = Cliente (nome = 'Fernando', idade = 40, profissão = 'analista', cidade = 'Salvador')
Cliente3 = Cliente (nome = 'Ana', idade = 30, profissão = 'construtor', cidade = 'Maringa')


#Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão. Adicione um método especial __str__ para imprimir uma representação em string da pessoa. Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano. Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de saudação personalizada com base na profissão da pessoa.

class Pessoa:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}.'
        else:
            return f'Olá, sou {self.nome}!'

    def aniversario(self):
        self.idade += 1

