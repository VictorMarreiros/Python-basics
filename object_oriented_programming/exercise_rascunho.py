class Store:
    def __init__(self, name, items):
        # You'll need 'name' as an argument to this method.
        self.name = name
        self.items = items
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def __str__(self):
        return f"This store {self.name} has items --> {self.items}"
    
    def __repr__(self):
        return f"Store('{self.name}', {self.items})"

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self):
        # Add together all item prices in self.items and return the total.
        return sum([item["price"] for item in self.items])     

        # retornando a soma(dos .valores({"chave": value} do dicionário self.items)
        #exemplo: total = 0
        #         for name, price in self.items.items():
        #              total += price
        #         return total


store1 = Store("lojinha", {"Arroz": 100, "Fejão": 5.90, "Macarrão": 4, "Pão Pummam": 5.30, "Asa de Frango": 7.50})

print(store1)
print(store1.stock_price()) 



