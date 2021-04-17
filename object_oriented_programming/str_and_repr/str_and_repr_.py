class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):                                  # seta uma nice string padrão ao printar o objeto, ex: print(object)
        return f"Person: {self.name}, age {self.age}"   # ela retona as informações do objeto de maneira mais clara 
    
    def __repr__(self):                                 # seta uma string padrão para auxiliar desenvolvedores com os parametros do objeto
        return f"Person('{self.name}', {self.age})"     # ela retorna a forma como ela deve ser utilizada, ajudando no debug do codigo


bob = Person("Bob", 25)
print(bob)
