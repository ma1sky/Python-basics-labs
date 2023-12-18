from classProduct import product

class phone(product):
    def __init__(self, name, price, model):
        try:
            super().__init__(name, price)
            if isinstance(model, str):
                self.__model = model
            else:
                raise TypeError("Некорректный тип данных для модели")
        except TypeError as e:
            print(f"Ошибка: {e}")
            raise TypeError

    @property
    def model(self):
        return self.__model

    def __del__(self):
        print(f"Телефон {self.name} удален.")

    def __str__(self):
        return f"Наименование: {self.name}\tЦена: {self.price:.2f}\nМодель: {self.model}\n"
