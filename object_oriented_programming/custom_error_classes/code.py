class TooManyPagesReadError(ValueError):        # criamos um novo erro customizado para o nosso programa
    pass                                        # criamos uma nova class o o nome e herdamos 'ValueError'
# pass --> só queremos que a nova classe 'TooManyPagesReadError' seja uma cópia da classe 'ValueError'
# a classe 'ValueError' é uma das principais classes de erro internas ao python

class Book:
    def __init__(self, name: str, page_count: int):
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr__(self) -> str:
        return f"<Book: {self.name}, read {self.pages_read} pages out of {self.page_count}>"
    
    def read(self, pages: int):                      # o usuário informa quantas paginas o usuário leu
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(             # Aqui criamos o nosso erro customizado 'TooManyPagesReadError'
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
            )
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages out of {self.page_count}.")


python101 = Book("python101", 100)
print(python101)

try:                                            # tente fazer:
    python101.read(35)                          # --> usuário leu 35 paginas de 100pgs
    python101.read(80)                          # --> o usuário não pode ler mais 80 paginas, pois 100pg é o maximo
except TooManyPagesReadError as e:              # armazenando o retorno do erro na variável 'e'
    print(e)                                    # printando a variável 'e'




# ---> Notes <---
# https://docs.python.org/3/tutorial/errors.html   --> documentation

# -> BaseException              --> The base class for all built-in exceptions. It in not meant to be directly inherited
#                                   by user-defined classes (for that, use 'Exception').
# -> Exception                  --> All built-in, non-system-existing exceptions are derived from this class.
#                                   All user-defined exceptions should also be derived from this class.
# -> ValueError                 --> Raised when an operation or function receives an argument that has the right type,
#                                   but an inappropriate value.
# -> TypeError                  --> Raised when an operation or function is applied to an object of inappropriate type.
# -> ZeroDivisionError          --> Raised when the second argument of a division or modulo operation is zero.
# -> OSError                    --> This Exception is raised when a system function returns a system-related error.
#                                   Ex: 'I/O Failures', 'file not found', 'disk full'
# -> NameError                  --> Raised when a local or global name is not found.
# -> ConnectionError            --> A base class for connection-related issues.
# -> RuntimeError               --> Raised when an error is detected that doesn't fall in any of the other categories.
# -> OverflowError              --> Raised when the result of an arithmetic operation is too large to be represented.
# -> MemoryError                --> Raised when an operation runs out of memory but the situation may still be rescued
#                                   (by deleting some objects).
