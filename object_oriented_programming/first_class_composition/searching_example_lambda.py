# pesquisar sobre: from operator import itemgetter


def search(sequence, expected, finder):           # finder(elem) ==> get_friend_name(elem)
    for elem in sequence:                         # para cada elemento na sequencia chama a função finder(elem)
        if finder(elem) == expected:              # e compara com o expected="name_friend"
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")


friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]


print(search(friends, "Bob Smith", lambda friend: friend["name"]))
# lambda <recebe_valor_friend>: <retorna_valor>        --> lambda recebe_friend: retorna_friend["name"]
# a função lambda aqui, substitui o def get_friend_name()

# print(search(friends, "Rolf Smith", get_friend_name))   # --> elemento existente
