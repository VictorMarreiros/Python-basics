def multiply(*args):           # recebendo todos os valores
    total = 1
    for arg in args:
        total *= arg
        print(total)

    return total


def apply(*args, operator):     #recebendo todos os args com (*)
    if operator == "*":
        return multiply(*args)  #desestruturando os valores da tupla com (*), passando os valores um por um - One-by-One
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 2, 3, 4, 5, operator="*"))   # o operador="*" neste caso, é a seleção de qual operação o usuário deseja efetuar 