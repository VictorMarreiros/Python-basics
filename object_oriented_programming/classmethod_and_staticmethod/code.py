class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weight {self.weight}g>"

    @classmethod
    def hardcover(cls, name, weight):
        return cls(name, cls.TYPES[0], weight + 100)

    @classmethod
    def paperback(cls, name, weight):
        return cls(name, cls.TYPES[1], weight)
    


book = Book.hardcover("Harry Potter", 1500)
print(book)

book2 = Book.paperback("Algorithms", 1500)
print(book2)