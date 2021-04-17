# Comparisons: ==, !=, <, >, >=, <=
# Comparison: is -- serve para comparar se dois elementos são exatamente a mesma coisa (se estão no mesmo local da memoria)

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)
print(friends is abroad)  # False -- ocorre porquê cada lista tem seu proprio local na memória

abroad = friends
print(friends is abroad)  # True -- agora sim, as duas listas são exatamente o mesmo elemento na memória