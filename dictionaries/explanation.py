
# Os dicionários podem ser acessados mais rapidamente
# na memória. Por isso tem o desempenho de busca melhor

friends_1 = {"Rolf":24, "Adam":30, "Anne":27}  # essa é a declaração padrão de um dicionário

print(friends_1["Rolf"])            # esse é um dos formatos que podemos utilizar para pesquisar chaves em nosso dicionário
print(friends_1["Anne"])            # ao pesquisar pela chave, o interpretador trará o valor relacionado à chave pesquisada
print()

# Também podemos ter uma lista de dicionários
lista = [                                               # disctionary_of_dictionaries = [{"key": value}, {"key", value}, {"key": value}]
    {"name": "Rolf", "age":24},                         # cada dicionário dentro de um dicionário tem dois items("name": "nome" e "age": idade )
    {"name": "Adam", "age":30},                         # podemos utilizar o .items() para ter acesso a cada dicionário dentro de um dicionário
    {"name": "Anne", "age":27}                          # da mesma forma podemos utilizar o .values() para acessar apenas o valor de cada item 
]

for dicionario in lista:                                          # cada item da variável Lista[] é um Dicionário{}
    print(f"Item da Lista --> {dicionario.items()}")              # queremos printar cada um dos dicionários{nome:valor, idade:valor} 
                                                                  # dessa lista[dicionario1, dicionario2, dicionario3]
print()

for dicionario in lista:                                                    
    print(f"Valores de cada item da Lista --> {dicionario.values()}")    # Printando apenas os valores com a função .values() 

# .clear()  --> limpa a lista