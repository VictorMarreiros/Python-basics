from time import sleep


def age_program(age):
    choice = input("Give me seconds (s), hours (h) or days (d)? ")
    if choice == "s":
        # Convert years to seconds
        print("You've lived more then {} seconds".format(age * 365 * 24 * 60 * 60))
    elif choice == "h":
        # Convert years to hours
        print("You've lived more then {} hours".format(age * 365 * 24 * 60))
    elif choice == "d":
        # Convert years to days
        print("You've lived more then {} days".format(age * 365 * 24))
    else:
        print("rs..")
        age_in_seconds = int(input("Please enter the number of seconds you've lived for: "))
        # Convert seconds to years
        print("You've lived for {} years [*CONGRATS*]".format(int(age_in_seconds / 60 / 60 / 24 / 365)))
    sleep(2)


def user_age():
    return int(input("How old are you? "))


# Start
# =========================================

name = input("Hello user, what is your name? ")

# Devemos saber a hora de utilizar esse tipo de notação               ->  f"{variable}"
# no caso de cálculos direto no format é melhor utilizar a notação    -> "{}".format(variable * 2)
print(f"Welcome {name}, to the age program!")
print()

user_age = user_age()
print()
age_program(user_age)

print()
print(f"See ya {name}!")
