# attendance -> comparecimento
student_attendance = {"Rolf":96, "Bob":80, "Anne":100}

# student é a chave
# attendence é o valor
# .items() --> para acessar os itens do dicionário 
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

print("--- <> ---")


for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")


print("--- <> ---")

cars_ages = {
    "celta":1999, 
    "gol quadrado":2002, 
    "uninho":2000,
    "chevett":2005
    }

for car in cars_ages:
    print(f"{car}: {cars_ages[car]}")
