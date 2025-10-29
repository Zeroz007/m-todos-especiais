class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo=titulo
        self.autor=autor
        self.ano=ano
    def __eq__(self, value):
        return self.titulo==value.titulo and self.autor==value.autor and self.ano==value.ano
livro1=Livro("Python para todos","John Doe",2020)
livro2=Livro("Python para todos","John Doe",2021)
livro3=Livro("Começando com a linguagem python","John Doe",2021)
livro4=Livro("Linguagem javascript","John Doe",2021)
print(livro1==livro1)
print(livro2==livro3)
print(livro3==livro4)
print(id(livro1))
print(id(livro2))
print(id(livro3))
print(id(livro4))