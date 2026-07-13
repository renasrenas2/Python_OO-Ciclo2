"""
Implemente um sistema orientado a objetos em Python para
representar uma biblioteca com as classes Biblioteca, Livro,
Autor e Usuario, aplicando os conceitos de associação,
agregação, composição e dependência. A classe Autor deve
armazenar nome e nacionalidade; a classe Livro deve conter
título, ano e uma referência a um Autor (agregação). A Biblioteca
deve possuir um nome e ser responsável por criar e armazenar
os livros internamente (composição). A classe Usuario deve
conter o nome e manter uma referência à Biblioteca à qual está
associado (associação), além de possuir um método para pegar
um livro emprestado, usando temporariamente o livro sem
armazená-lo (dependência).


associação, agregação, composição e dependência.


Autor - nome e nacionalidade

Livro - título, ano e uma referência a um Autor (agregação)

Biblioteca - nome e ser responsável por criar e armazenar os livros internamente (composição)

Usuario - nome e manter uma referência à Biblioteca à qual está associado (associação)
          possuir um método para pegar um livro emprestado, usando temporariamente o livro sem armazená-lo (dependência).

"""

class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome = nome
        self.nacionalidade = nacionalidade

class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livros(self, livro):
        self.livros.append(livro)

class Usuario:
    def __init__(self, nome):
        self.nome = nome
    
    def pegar_emprestado():
        for livro in livros:
            

            
def main():
    pass

if __name__ == "__main__":
    main()