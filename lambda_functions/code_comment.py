# Uma função lambda permite criar essa mesma função com apenas uma linha
def double(x):
    return x * 2


sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
#doubled = map(double, sequence)

# Lambdas são funções sem um nome
# são usadas para calcular o retorno dos parametros fornecidos
# normalmente serão descomplicadas em apenas uma linha
# para que não haja a necessidade de criar uma função def()
# só para fazer um cálculo simples

# a função map() pega cada valor na 'sequence'<list> e joga na função lambda, para o valor de x
# para cada valor na lista sequence, chama a função lambda para multiplicá-lo por 2
doubled = list(map(lambda x: x * 2, sequence))  # map(lambda <recebe_valor>: <retorna_valor * 2> <para_cada_v_na_sequencia>)
print(doubled)

# sintaxe --> outra forma de escrever a linha acima
#doubled = [(lambda x: x * 2)(x) for x in sequence]
#print(doubled)