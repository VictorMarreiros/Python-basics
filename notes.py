#############################################################################         
# Tabela de Abertura de arquivos                                            #
#############################################################################         
# MODO   #                      OPERAÇÕES                                   #         
#############################################################################         
#   r    # leitura                                                          #         
#   w    # escrita, apaga o conteúdo se já existir                          #         
#   a    # escrita, mas preserva o conteúdo se já existir                   #         
#   b    # modo binário                                                     #         
#   +    # atualização (leitura e escrita)                                  #         
#############################################################################         
# Livro: Introdução a programação Python, NOVATEC. Cap 9. Pg 170. <Tabela 9.1>


#Ex:  open('<nome_do_arq.txt>', '<modo_de_operação>')
"""arquivo=open("numeros.txt", "w")
for numero in range(1, 101):             # range(1,<N>) -> tamanho do meu arquivo inicial
    arquivo.write(f"{numero}\n")         # .write("\n") -> escreve na linha e pula p/ prox 
arquivo.close()"""




arquivo=open("numeros.txt", "r")
for linha in arquivo.readlines():  # .readlines() -> lista['L1', 'L2', 'L3', .., 'Ln']
    print(linha)                   # para cada linha no arquivo: print linha
arquivo.close() 

# .readlines() --> cria uma lista em que cada elemento é uma linha do arquivo 