class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True
    
    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"         # !r - indica ao interpretador que deve colocar ' ' na formatação dessa variável

    def disconnected(self):
        self.connected = False
        print(f"{self.name} - Disconnected")

class Printer(Device):                                              # essa é a forma como informamos ao interpretador que essa classe Printer() herdará a classe pai Device
    def __init__(self, name, connected_by, capacity):               # devemos passar todos os atributos que esse objeto tem
        super().__init__(name, connected_by)                        # utilizando super(). indicamos que será utilizado um methodo da classe pai/ super class
        self.capacity = capacity                                    # e podemos informar todos os atributos, a mais, que esse herdeiro tem
        self.remaining_pages = capacity                             
    
    def __str__(self):
        return f"{super().__str__()} {self.remaining_pages} remaining pages from {self.capacity}"  # utilizando o __str__ da classe pai com super().
    
    def print(self, pages):
        if not self.connected:
            print(f"The {self.name} is not connected.")
            return 
        print(f"Printing {pages} pages.")
        self.remaining_pages -= pages


printer = Printer("Printer", "USB", 500)    # creating a printer with de arguments of class chieldren
printer.print(20)                           
printer.disconnected()

printer.print(100)                          # try to print with disconnected printer
