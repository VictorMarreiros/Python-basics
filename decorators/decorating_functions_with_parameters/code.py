# decorators_with_parameters != decorating_functions_with_parameters

import functools
user = {"name": "Jose", "acess_level": "admin"}     # altere "admin" para "guest" e vise-versa


#  permitir que qualquer tipo de dado seja aceito (*args e **kwargs), significa que essa função pode ser chamada
#  por outras funções, e não somente a função que foi @decorated
# em outras palavras podemos chamar @make_secure para mais de uma função e não somente pela função get_password()

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):   # aceita qualquer tipo de argumento (*args, **kwargs)
        if user["acess_level"] == "admin":  # a função verifica se o usuário tem permissão
            return func(*args, **kwargs)
        else:                            # se não tiver, apenas printa a msg e volta para a prox linha depois da chamada
            return f"The user <{user['acess_level']}> has no acess level <admin>"

    return secure_function


@make_secure
def get_password(panel: str) -> str:  # para que get_password seja utilizado, o usuário deve passar o argumento correto
    if panel == "admin":              # caso contrário, o código para antes de entrar em get_password
        return "1234"                 # ou pode fazer outra coisa antes de entrar nessa função get_password(panel)
    elif panel == "billing":
        return "super_secure_password"


print(get_password("admin"))
print(get_password.__name__)  # printa o nome da função que está sendo chamada (experimente comentar @functools.wraps())