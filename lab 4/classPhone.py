from classProduct import product

class phone(product):
    def __init__(self, name, price, model):
        product.__init__(self, name, price)
        self.__model = model

    @property
    def model(self):
        return self.__model
    
    def __del__(self):
        print(f"Телефон {self.name} удален.")
    def __str__(self):
        return f"Наименование: {self.name} \t Цена: {self.price:.2f} \nМодель: {self.model}\n"