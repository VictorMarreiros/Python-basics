#friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print("Lista friends: ", friends)
print("Lista starts_s: ", starts_s)

print("friends[] == starts_s[] : ", friends is starts_s)
# False -- cada lista está armazenada em um local diferente na memoria

print(f"{friends[0]} == {starts_s[0]} : ", friends[0] is starts_s[0])
# True  -- pois o conteúdo na posição 0, das duas listas, é o mesmo

print("ID na memoria da lista -> friends: ", id(friends), "ID na memoria da lista -> starts_s: ", id(starts_s))
# 
# função id() --> printa o ID da posição de memoria de cada lista 


# --> Essa foi a base da List Comprehension
#for friend in friends:
#    if friend.startswith("S"):          #função .startswith("")  --> verifica o primeiro caractere de uma string
#        starts_s.append(friend)


# .clear()  --> limpa a lista