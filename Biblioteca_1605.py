#Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.

from Livros_1605 import Livro

#No arquivo biblioteca.py, empreste o livro chamando o método emprestar e imprima se o livro está 
#disponível ou não após o empréstimo.

livro_biblioteca = Livro('Harry Potter','J. K. Rowling',1997)
print(f'Antes de emprestar (biblioteca): Livro disponível? {livro_biblioteca._disponivel}')
livro_biblioteca.emprestar()
print(f'Depois de emprestar (biblioteca): Livro disponível? {livro_biblioteca._disponivel}')


#No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter 
#a lista de livros disponíveis publicados em um ano específico.

ano_especifico = 1997
livros_disponiveis_ano = Livro.verificar_disponibilidade(ano_especifico)
print(f"'\n Livros disponíveis em '{ano_especifico}: {livros_disponiveis_ano}\n")
for livro in livros_disponiveis_ano:
    print(livro)