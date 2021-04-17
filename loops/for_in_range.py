friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:              # for _ in list:  --> "para cada elemento na lista, faça: <code>"
    print(f"{friend} is my friend")

print("--- <> ---")

for friend in range(4):             # quando utilizamos a função range() ele cria uma lista com [0, 1, 2, 3]
    print(f"{friend} is my friend")