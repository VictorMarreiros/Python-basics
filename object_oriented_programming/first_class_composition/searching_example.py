
def search(sequence, expected, finder):           # finder(elem) ==> get_friend_name(elem)
    for elem in sequence:                         # para cada elemento na sequencia chama a função finder(elem)
        if finder(elem) == expected:              # e compara com o expected="name_friend"
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


def get_friend_name(friend):                      # ao receber o elemento=friend
    return friend["name"]                         # retorna o valor que estiver na chave 'name' - friend["name":"value"]


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]


# tentando encontrar um friend que não exite, forçando o raise RuntimeError()
print(search(friends, "Bob Smith", get_friend_name))  # finder=get_friend_name -> passando uma função como argumento


# print(search(friends, "Rolf Smith", get_friend_name))   # --> elemento existente
