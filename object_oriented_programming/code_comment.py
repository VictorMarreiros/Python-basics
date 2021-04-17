
# Obejeto Aluno, cada aluno deve ter nome e um conjunto de notas 
class Student:
    # Método __init__ constróe a classe/objeto, aqui são definidas todas as propriedades do objeto, como ex: nome, sobrenome, idade, nota, grau, etc..
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    # todos os metodos dentro de uma classe precisam ter o parametro self
    # self permite que nós acessemos as propriedades do próprio objeto (self object)
    # como por exemplo: self.name, self.grades que são propriedades criadas no método __init__
    def average_grades(self):                           #Cada função dentro de uma classe é um método  /-/  Método: Média de Notas
        return sum(self.grades) / len(self.grades)



# Iniciando um novo objeto Aluno --> Name: Victor / Grades: 90, 100, 100, 81, 93
student = Student("Bob", (90, 100, 100, 81, 93))
# student - passa a ser uma nova variável para o python, e por isso podemos chamá-la a qualquer momento
student2 = Student("Rolf", (100, 75, 80, 91, 86))


# para acessar as propriedades do objeto no python, basta informar o objeto e informar qual propriedade que acessar --> student.name
print(student.name)
print(student.average_grades())
print()

print(f"{student2.name} : {student2.average_grades()} ")



