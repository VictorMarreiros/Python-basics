class Livro:
    TIPOS = ("Capa-dura", "Brochura")               # definindo uma matriz de TIPOS de livros dentro da classe/objeto

    def __init__(self, nome, tipo_livro, peso):     # método inicializador da classe, onde são definidos os atributos referentes ao objeto
        self.nome = nome                            # nome do livro
        self.tipo_livro = tipo_livro                # tipo do livro
        self.peso = peso                            # peso do livro
    
    def __repr__(self):                                                         # método __repr__ que retorna um print da estrutura do objeto
        return f"<Livro {self.nome}, {self.tipo_livro}, Peso {self.peso}g>"     # para auxiliar no debug do arquivo
    
    @classmethod                                    # definindo um método da classe - cls refere-se a própria classe em Python
    def capa_dura(cls, nome, peso):                 # um @classmethod sempre começa com o parametro 'cls'
        return cls(nome, cls.TIPOS[0], peso + 100)        # posso utilizar o cls para inicializar ela mesma <a classe> e passar o cls.TIPOS[0] como parametro
                                                    # dessa forma, sempre que o usuário for chamar a classe, ele só precisará passar o nome e peso
                                                    # na chamada do objeto/classe o método deverá ser utilizado --> Livro.capa_dura("nome", 100)
    @classmethod
    def brochura(cls, nome, peso):
        return cls(nome, cls.TIPOS[1], peso)

livro1 = Livro.capa_dura("Harry Potter", 1500)      # criação do objeto com o método da classe .capa_dura() 
print(livro1)

print()
livro2 = Livro.brochura("Algoritmos", 1500)
print(livro2)