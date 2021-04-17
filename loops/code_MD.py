grades = [35, 67, 98, 100, 100]
total = sum(grades)    # função sum() soma todos os elementos da lista
amount = len(grades)   # função len() conta quantos elementos existem na lista || str || int

print(f"A média da classe é {total / amount} pts")

#for grade in grades:
#    total += grade












###################################### search #################################
#---> https://www.programiz.com/python-programming/methods/list/pop
# ------------------------------------------------
# ------------------------------------------------
# programming languages list
languages = ['Python', 'Java', 'C++', 'French', 'C']

# remove and return the 4th item
return_value = languages.pop(3)
print('Return Value:', return_value)

# Updated List
print('Updated List:', languages)

# remove and return the last item 
print('\nWhen -1 is passed:') 
print('Return Value:', languages.pop(-1))
print('Updated List:', languages)

# remove and return the third last item
print('\nWhen -3 is passed:') 
print('Return Value:', languages.pop(-3))
print('Updated List:', languages)