# C05EX03.CPP
# Programa Fatorial
# Upgraded Object_oriented_programming

from typing import List


class Aluno:

    def __init__(self, nome: str):
        self.nome = nome
        self.notas = []
        self.media = 0
        self.nota_max = 100
    
    def __str__(self) -> str:
        return f"Aluno {self.nome}, Notas: {self.notas}, Média: {self.media:.2f}"

    def cMedia(self):
        if len(self.notas) == 0:
            raise ZeroDivisionError(f"O aluno não possui notas -> Lista de notas: {self.notas}")

        self.media = sum(self.notas) / len(self.notas)
        print(f"Aluno -> {self.nome}, Média: {self.media:.2f}\n")

    def poeNota(self, nota: float):   # armazena em self.notas, todas as notas divididas por 10
        if nota < 0:
            raise ValueError(f"A nota não pode ser negativa.. Nota inserida: {nota}")
        elif nota > self.nota_max:
            raise ValueError(f"A nota deve ser um numero de 0 a {self.nota_max}. --> Nota inserida: {nota}")

        self.notas.append((lambda nota: nota / 10)(nota))  # list(map(função <lambda <retorno_nota>: <f(cada_nota/10)> >, para_cada_nota <notas[75, 90, 83, 92]>)) 
    
    def pegaNota(self):
        print(f"{self.nome} - Notas:  {self.notas}\n")


if __name__ == '__main__':
    aluno1 = Aluno("Adolfo")
    print(aluno1)
    print()

    try:
        for i in range(0, 4):
            aluno1.poeNota(int(input(f"Insira a {i + 1}° nota: ")))
        print()
        
        aluno1.cMedia()
        aluno1.pegaNota()
        aluno1.poeSala(1)

        print(aluno1)

    except ValueError as e:
        print(e)
    except ZeroDivisionError as a:
        print(a)