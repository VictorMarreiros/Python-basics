# Uma função lambda permite criar essa mesma função com apenas uma linha
def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]


 
doubled = list(map(lambda x: x * 2, sequence))
triple = list(map(lambda value: value * 3, sequence))

print(
        f"That's your first list: {sequence}\n"
        f"Doubled:                {doubled}\n"
        f"Triple:                 {triple}\n"
)
print(f"Thanks!")



# função  lambda <retorno>: <execução_da_função> (variável de saida)
#         (lambda   <x>    :    <x * 2>)(x)  
#doubled = [(lambda x: x * 2)(x) for x in sequence]
# 
doubled = [(lambda x: x * 2)(x) for x in sequence]