import sys
# function abs() -- sempre retorna o numero absoluto e positivo ( como se fosse a matriz de um numero |-1| = 1)
number = 13

user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == "y":
    print("You have to try guess out our number from 0 to 20")
    user_number = int(input("Guess out number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:    # verify utilizando a função 'abs()' que sempre seta o result como positivo
        print("You were off by one.")
    elif number - user_number in (2, -2):   # verify utilizando 'in' statement com uma tupla de elementos (2, -2)
        print("you were off by two.")
    else:
        print("Sorry, it's wrong!")
else:
    print("\nYou don't wanted to play T-T")
    print('Ok, Good Bye!')
    sys.exit()
