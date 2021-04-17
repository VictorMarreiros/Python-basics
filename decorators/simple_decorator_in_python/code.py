user = {"username": "jose", "acess_level": "guest"} # user com acess_level: "guest" - convidado


def get_admin_password():                   # Não queremos que o usuário tenha acesso direto à essa função
    return "1234"                           # a função make_secure() garante que isso não acontecerá


# decorator
def make_secure(func):                      # recebe a funcão get_admin_password como arg
    def secure_function():                      # funções podem ser declaradas dentro de outras funções
        if user["acess_level"] == "admin":      # verifica o nível de acesso do user
            return func()                       # se o nível for "admin" retorna a chamda da função get_admin_password()
    return secure_function                  # retorna outra funcão secure_function


get_admin_password = make_secure(get_admin_password)
print(get_admin_password())                         # user ainda com acess_level: "guest" -> deve retornar None

user = {"username": "jose", "acess_level": "admin"}  # alterando acess_level: "admin"
print(get_admin_password())                          # deve retornar a senha do admin "1234"