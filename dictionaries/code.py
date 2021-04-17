# student_attendance --> lista de comparecimento de estudantes, com --> nome: comparecimento
student_attendance = {"Rolf":96, "Bob":80, "Anne":100}

# função .values() está pegando apenas os valores do dicionário student_attendence
attendance_values = student_attendance.values()

# Tirando a média dos valores de cada chave na lista
# utilizando a função .values()

print("Relatório de comparecimento de alunos")
for student, attendance in student_attendance.items():
    print(f"{student} compareceu {attendance}")

# printa a média entre SOMA dos VALORES da lista e DIVIDE 
# pela QUANTIDADE de VALORES na lista
# sum() -- para somar  &  len() -- para contar quantos valores existem 
print("Média comparecimento: ", sum(attendance_values) / len(attendance_values))