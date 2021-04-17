#1. Modify the code so that the evens list contains only the even numbers of the numbers list.
# You do not need to print anything
#2. For part 2, add a clause to the if statement such that if the user's input is "q", your program prints "Quit".
#Remember that for these coding exercises, Python will care about uppercase and lowercase letters,
# so make sure to use the right ones!

# --- Part I ---
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []      #evens --> pares  | even number --> numero par
for number in numbers[1::2]:
    evens.append(number)
    # também é possível verificar se o resto da divisão do numero por 2 é igual a 0.
    # EX.: if number % 2 == 0 : evens.append(number)

print(evens)

# --- Part II ---
user_input = input("Press 'a' to Add ou 'q' to Quit: ").lower()
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")