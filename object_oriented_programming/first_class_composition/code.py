def devide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


def calculate(*values, operator):       # *values, operator = divide()
    return operator(*values)            # operator(*values) = divide(*values)


result = calculate(20, 4, operator=devide)  # posso definir o operador como uma função sem passar operator=divide()
                                            # passando a função dessa forma, dentro da função calculate()
                                            # podemos chamar operator() como se fosse o divide()
print(result)   # esse codigo tem um problema, caso o usuário passe mais de um valor em *values,
                # a função divide() espera apenas 2 valores e retornará erro