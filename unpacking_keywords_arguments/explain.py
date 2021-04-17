# kwargs -- keywords arguments
# **kwargs --> é utilizado como convenção para esse tipo de função
def named(**kwargs):  # cria um novo dicionario com chave="valor", armazenando na variavel 'kwargs{}'
    print(kwargs)
    print(kwargs["school"])


details = {"name": "John", "age": 25, "school": "computing"}

named(**details) #passando chave="valor dp dicionário 'details'

# passando como argumento chave="valor", chave="valor"
#named(name="Bob", age=25, school="Computing")