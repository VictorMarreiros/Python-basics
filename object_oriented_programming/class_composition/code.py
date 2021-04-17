# class_composition é a contra partida de herança
# serve para contruir classes que USAM outras, ao invés de herdá-las.

# queremos criar uma estante de livros composta por vários livros

from typing import List

class BookShelf:                                                # BookShelf --> Estante de livros
    def __init__(self, *books: List[Book]):                     # *books --> aceita n books como argumento
        self.books = books
    
    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)!r} books"      # retorna a quantidade de book na shelf


class Book:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self) -> str:
        return f"Book {self.name!r}"


book1 = Book("Harry Potter")
book2 = Book("Python 101")

shelf = BookShelf(book1, book2)

print(shelf)