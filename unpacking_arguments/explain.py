# *args --> aceitará todos os argumentos que foram passados na chamada da função por conta do (*)
# e todos os argumentos serão armazenados em forma de tupla() --> 'args'
def multiply(*args): # recebe cada cada valor da tupla como um argumento individual
    print(args)
    total = 1           # começa em 1 pois será utilizado para multiplicação
    for arg in args:
        total *= arg    # Multiplica o total * arg e armazena no total a cada passagem

    return total


print(multiply(1, 3, 5)) # passando uma tupla de elementos


#print(multiply(-1))
#print(multiply(1, 3, 5, 8, 13))