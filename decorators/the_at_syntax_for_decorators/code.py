import functools    # essencial quando se está utilizando @decorators

user = {"username": "Jose", "acess_level": "guest"}


def make_secure(func):                  # decorator
    @functools.wraps(func)
    def secure_function():              # just a function
        if user["acess_level"] == "admin":
            return func()
        else:
            return f"The user: {user['username']!r} has no admin permission"

    return secure_function              # return a function


@make_secure                # decorator
def get_admin_password():
    return "1234"


print(get_admin_password.__name__)
print(get_admin_password())


#print(get_admin_password.__name__) --> serve para verificar o nome da função que foi chamada

