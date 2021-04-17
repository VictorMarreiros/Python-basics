user = {"username": "Jose", "acess_level": "guest"}


def get_admin_password():
    return "1234"


def make_secure(func):
    def secure_function():
        if user["acess_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']!r}"
    return secure_function


get_admin_password = make_secure(get_admin_password)
print(get_admin_password())

user = {"username": "jose", "acess_level": "admin"}
print(get_admin_password())