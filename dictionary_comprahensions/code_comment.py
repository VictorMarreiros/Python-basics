# Lista de usuários, onde cada valor da lista é uma tupla(), com (ID, "Nome", "Senha")
users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4ssword"),
    (3, "username", "1234"),
]

# 'user[1]'            --> será a chave <todos os indices [1] de cada linha da lista> - apenas o nome de user
# 'user[1]: user'      --> chave : user <cada tupla da lista 'users[]' será om VALOR da nova lista 'username_mapping{}'>
# 'user[1]: user for user in users' --> para cada usuário em users faça 'user[1]: user'
username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

# essa linha pesquisa pela chave username que o usuário informou dentro do set 'username_mapping'
# ao encontrar a chave
_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your datails are correct!")
else:
    print("Your details are incorrect.")