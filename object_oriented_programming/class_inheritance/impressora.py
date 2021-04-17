class Dispositivo:
    def __init__(self, nome, conectado_por):
        self.nome = nome
        self.conectado_por = conectado_por
        self.conectado = True
    
    def __str__(self):
        return f"Dispositivo {self.nome!r}, ({self.conectado_por})"    # !r - indica ao interpretador que deve colocar '' na formatação dessa variável
    
    def desconectar(self):
        self.conectado = False
        print(f"{self.nome!r} disconnected.")

class Impressora(Dispositivo):
    def __init__(self, nome, conectado_por, capacidade):
        super().__init__(nome, conectado_por)
        self.capacidade = capacidade
        self.paginas_restantes = capacidade
    
    def __str__(self):
        return f"{super().__str__()}({self.paginas_restantes} paginas restantes)"

    def imprime(self, paginas):
        if not self.conectado:
            print(f"Não foi possivel imprimir {paginas} paginas - {self.nome!r} está desconectada - favor conectá-la por {self.conectado_por}.")
            return 
        self.paginas_restantes -= paginas
        print(f"{self.paginas_restantes} paginas restantes")



impressora = Impressora("Impressora", "USB", 100)
print(impressora)

impressora.imprime(50)
impressora.imprime(10)
impressora.desconectar()
impressora.imprime(20)



