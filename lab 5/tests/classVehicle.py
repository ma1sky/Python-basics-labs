from classProduct import product

class vehicle(product):
    def __init__(self, name, price, weight):
        try:
            super().__init__(name, price)
            if isinstance(weight, (int, float)) and weight > 0:
                self.weight = weight
            else:
                raise TypeError("Некорректный тип данных или значение для веса")
        except TypeError as e:
            print(f"Ошибка: {e}")
            raise TypeError

    def __add__(self, other):
        try:
            if isinstance(other, vehicle):
                return self.weight + other.weight
            else:
                raise TypeError("Невозможно выполнить операцию сложения. Ожидается объект класса Vehicle")
        except TypeError as e:
            print(f"Ошибка: {e}")
            raise TypeError

    def __del__(self):
        print(f"Машина {self.name} ликвидирована.")
    
    def __str__(self):
        return f"Наименование: {self.name}\tЦена: {self.price:.2f}\nВес: {self.weight}\n"
