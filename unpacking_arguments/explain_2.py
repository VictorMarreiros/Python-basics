# (*) arguments

def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))      # o (*) desestrutura a lista, passando cada valor como um argumento único
#add(nums)             # dessa forma a lista [3, 5] seria passada para o argumento X e nada seria passado para o Y






# (**) keywords arguments

def sub(w, z):             # argumentos W e Z   ==  chaves "w" e "z" ---> valores "w": 15  e "z": 5
    return w - z

d_nums = {"w": 15, "z": 5} # quando a chave do dicionario for igual aos argumentos que estão sendo pedidos
print(sub(**d_nums))       # podemos usar (**) para passar chave="valor" como cada argumento