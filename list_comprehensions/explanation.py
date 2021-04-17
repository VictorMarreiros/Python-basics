#sempre que uma list comprehension for criada, será para compor uma nova lista a partir dela
#List Comprehension:  <result> for <each_item> in <list>
#  -->  <o resultado q quer colocar na nova lista> for <para cada valor> in <da lista base>

numbers = [1, 3, 5]
doubled = [x * 2 for x in numbers]
print(doubled)