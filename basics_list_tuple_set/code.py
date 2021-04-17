# x = []  List   ---> ordenada por indices e permite alteração do conteúdo da lista
# w = ( , )  Tuple  ---> ordenada por indices e não permite alteração do conteúdo na tupla
# my_tuple = tuple('1')
# y = {}  Set    ---> não tem ordem por isso não pode ser alterado de modo convencional

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

science_class = science.difference(art)
art_class = art.difference(science)

union_classes = science.union(art)         #une as tabelas sem repetir dados
both_classes = art.intersection(science)   #pega somente dados que estão presentes nas duas tabelas (intersecção)


print(f"Alunos que estudam somente Science: {science_class}")
print(f"Alunos que estudam somente Art: {art_class}")
print(f"União de todos os alunos: {union_classes}")
print(f"Alunos que fazem as duas matérias: {both_classes}")



# <set1>.union(<set2>) --- <union 'set1' to 'set2'>
# friends = local.union(abroad)

# <set1>.difference(<set2>) --- <remove from 'set1' the content in 'set2'>
# local_friends = friends.difference(abroad)

