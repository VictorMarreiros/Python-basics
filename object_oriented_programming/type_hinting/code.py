# Type Hinting - Python3.5 + - boas práticas para especificar exatamente quais são os tipos de variáveis que devem ser passadas como argumento
# e também o tipo da varíavel de retorno. --> Sem esse tipo de escrita, o código funcionará normalmente
# A principal vantagem do utilizar o Type Hinting no código é que ele facilita a vida do desenvolvedor na hora de achar bugs 


from typing import List      # essa biblioteca formata o jeito que as Listas, Sets, Tuplas são mostrados no debug


class Store:
    def __init__(self, name: str, items: Set[items]):                               # <-- especificando claramente qual será o tipo de cada argumento à ser passado
        self.name:str = name
        self.items = items
    
    def __str__(self) -> str:                                                       # especificando claramente qual será o tipo de retorno do método __str__
        return f"This store {self.name} has items --> {self.items}"

    def __repr__(self) -> str:                                                      # especificando claramente qual será o tipo de retorno do método __repr__
        return f"Store('{self.name}', {self.items})"

    def add_item(self, name: str, price: float):                                    # argumentos -    name: str, price: float
        item = {"name": name, "price": price}
        self.items.append(item)

    def stock_price(self) -> float:                                                 # retorno será '  -> float  '
        return sum([item["price"] for item in self.items])     


store1 = Store("lojinha", {"Arroz": 100, "Fejão": 5.90, "Macarrão": 4, "Pão Pummam": 5.30, "Asa de Frango": 7.50})

print(store1)
print(store1.stock_price()) 



