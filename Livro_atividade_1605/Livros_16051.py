#Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao. Inicie um atributo chamado disponivel como True por padrão

class Livro:
     livros = []
     def __init__(self,titulo,autor,ano_publicacao):
          self.titulo = titulo
          self.autor = autor
          self.ano_publicacao = int(ano_publicacao)
          self._disponivel = True
          Livro.livros.append(self)

#Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e  ano de publicação do livro. Crie duas instâncias da classe Livro e imprima essas instâncias.

     def __str__(self) :
          return f"Livro: {self.titulo} | Autor: {self.autor} | Ano de Publicação: {self.ano_publicacao} | Disponivel: {self._disponivel} "
     
#Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False.
#Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.

     def emprestar(self):
          self._disponivel = False


#Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.

     @staticmethod
     def verificar_disponibilidade(ano):
        livros_disponiveis_ano = []
        
        for livro in Livro.livros:
            if livro.ano_publicacao == ano and livro._disponivel:
                livros_disponiveis_ano.append(livro)
        
        return livros_disponiveis_ano
        


Livro_emprestado = Livro('Harry Potter','J. K. Rowling',1997) 
print(f"'O livro está disponivel? :'{Livro_emprestado._disponivel}'")





