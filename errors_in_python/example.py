def divide(dividend: float, divisor: int) -> float:
    if divisor == 0:
        raise ZeroDivisionError("Can't be divided by 0")

    return dividend / divisor


students = [
    {"name": "Bob", "grades": [75, 90]},
    {"name": "Rolf", "grades": []},
    {"name": "Jen", "grades": [100, 90]},
]


try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = divide(sum(grades)/len(grades))
        print(f"{name} average {average}")
except ZeroDivisionError as e:
    print(f"ERROR: {name} has no grades!")
else: 
    print("-- Akk student averages calculated --")
finally:
    print("-- End of student average  calculation --")

