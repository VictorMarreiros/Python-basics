
class Student:
    
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __str__(self):
        return f"Student --> {self.name}, Grades --> {self.grades}, Average --> {self.average_grades()}"

    def __repr__(self):
        return f"Student('{self.name}', {self.grades})"

    def average_grades(self):
        return sum(self.grades) / len(self.grades)



student = Student("Bob", (90, 100, 100, 81, 93))
student2 = Student("Rolf", (100, 75, 80, 91, 86))

print(student.name)
print(student.average_grades())
print()

print(student)

print()
print(f"{student2.name} : {student2.average_grades()} ")



