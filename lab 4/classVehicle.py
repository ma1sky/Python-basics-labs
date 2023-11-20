from classProduct import product

class vehicle(product):
    def __init__(self, name, price, weight):
        product.__init__(self, name, price)
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight
    
    def __del__(self):
        print(f"Машина {self.name} ликвидированна.")
    
    def __str__(self):
        return f"Наименование: {self.name} \t Цена: {self.price:.2f} \nВес: {self.weight}\n"

