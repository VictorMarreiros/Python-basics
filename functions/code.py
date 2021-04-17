def divisor(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You Fool"


xdividend = int(input("Entre o Dividendo: "))
ydivisor = int(input("Entre o divisor: "))

result = divisor(xdividend, ydivisor)
print(result)





#def divisor(dividend, divisor):
#    if divisor != 0:
#        print(dividend / divisor)
#    else:
#        print("You Fool")


#xdividend = int(input("Entre o Dividendo: "))
#ydivisor = int(input("Entre o divisor: "))

#divisor(xdividend, ydivisor)