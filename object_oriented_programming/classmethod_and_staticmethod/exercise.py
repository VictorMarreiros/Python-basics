# 1. The 'franchise' method, which takes in a 'store' as argument. It should return a new 'Store' object,
#    with a 'name' equal to the argument + "- franchise"
#
# 2. The 'store_details' method, which also takes in a 'store' as argument. It should return a string
#    representing the argument.
###

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({'name': name, 'price': price})

    def __repr__(self):
        return f"Store {self.name!r}, {self.items}"                     # !r - indica ao interpretador que deve colocar '' na formatação dessa variável

    def stock_price(self):              # retorna a soma do valor de todos os itens no estoque
        return sum(item["price"] for item in self.items)

    @classmethod
    def franchise(cls, store):
        return cls(store.name + "- franchise")
        # Return another store, with the same name as the argument's name, plus " - franchise"

    @staticmethod
    def store_details(store):
        return f"'{store.name}, total stock price: {int(store.stock_price())}'"
        #return "{}, total stock price: {}".format(store.name, int(store.stock_price()))  --> O exercício pedia para que fizesse dessa forma (passei mt tempo para descobrir T-T)

        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'


store = Store("Test")
store2 = Store("Amazon")
store2.add_item("Keyboard", 160)

print(store)
print(store2)
print()

print(Store.franchise(store))      # returns a Store with name "Test - franchise"
print(Store.franchise(store2))     # returns a Store with name "Amazon - franchise"
#store2.add_item("Keyboard", 160)  
print()                            

print(Store.store_details(store))  # returns "Test, total stock price: 0" 
print(Store.store_details(store2)) # returns "Amazon, total stock price: 160"