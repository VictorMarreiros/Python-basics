#friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
friends = ["Sam", "Samantha", "Saurabh"]
starts_s = [friend for friend in friends if friend.startswith("S")]

print("Lista friends: ", friends)
print("Lista starts_s: ", starts_s)

print("friends[] == starts_s[] is ", friends is starts_s)

print(f"{friends[0]} == {starts_s[0]} is ", friends[0] is starts_s[0])

print("ID das listas na memória -> friends: ", id(friends), " -> starts_s: ", id(starts_s))
