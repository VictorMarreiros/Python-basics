# decorators_with_parameters != decorating_functions_with_parameters
# estamos usando a biblioteca para manter a documentação das nossas funções
import functools

user = {"username": "Jose", "access_level": "guest"}        # exercise: niveis de usuários [0, 1, 2]


def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} admin permissions for {user['username']}"

        return secure_function

    return decorator                            # esse é o retorno da chamada do decorator @make_secure()


@make_secure("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure("guest")
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password())
print(get_admin_password.__name__)
print(get_dashboard_password())
print(get_dashboard_password.__name__)