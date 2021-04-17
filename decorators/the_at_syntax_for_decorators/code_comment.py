import functools            # biblioteca nativa do python
                # estamos usando a biblioteca para manter a documentação das nossas funções
                # que foram @decorated
                # como boas praticas sempre que usar um decorator é preciso usar @functools.wraps(<function_decorated>)
                # exemplo linha 12 e linha 23


user = {"username": "Jose", "acess_level": "guest"}


# make_secure é o @decorator. e secure_function é apenas a função que substituirá a outra
def make_secure(func):                          # o decorator faz a chamada da função vir para cá
    @functools.wraps(func)                      # utilizado para manter o nome da função original na documentação. ao utilizar .__name__ para debugar a função
    def secure_function():                      # entrando dentro da função secure_function()
        if user["acess_level"] == "admin":      # e verificando o nível de acesso do usuário
            return func()                       # antes de realmente chamar a 'função' get_admin_password() = func()
        else:
            return f"The user: {user['username']!r} has no admin permission"

    return secure_function                      # retorna o resultado da secure_function()


# decorator com a sintaxe @
@make_secure                # faz com que a função get_admin_password() não seja mais uma função
def get_admin_password():   # ao invés disso, a função que é chamada é secure_function()
    return "1234"


#get_admin_password = make_secure(get_admin_password)   --->> o decorator @ substitui essa linha
#               --> significa que ao chamar get_admin_password() o código deverá chamar o decorator @make_secure antes

print(get_admin_password.__name__)  # com o uso do fuctools.wraps(func) - retornará o nome da função que foi 'decorada'
                                    # saida: get_admin_password
                                # caso não fosse utilizado functools.wraps(func), ao rodar esse print(<func>.__name__)
                                # a saida seria: secure_function

#print(get_admin_password.__name__) --> serve para verificar o nome da função que foi chamada

