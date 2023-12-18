class product:
    def __init__(self, name, price):
        try:
            if isinstance(name, str):
                self.__name = name
            else:
                raise TypeError("Некорректный тип данных для имени")

            if isinstance(price, (int, float)) and price >= 0:
                self.__price = price
            else:
                raise TypeError("Некорректный тип данных или значение для цены")

            self.__volume = 0 
        except TypeError as e:
            print(f"Ошибка: {e}")
            raise TypeError

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        try:
            if isinstance(name, str):
                self.__name = name
            else:
                raise TypeError("Некорректный тип данных для имени")
        except TypeError as e:
            print(f"Ошибка: {e}")
            raise TypeError

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        try:
            if isinstance(price, (int, float)) and price >= 0:
                self.__price = price
            else:
                raise TypeError("Некорректный тип данных или значение для цены")
        except TypeError as e:
            print(f"Ошибка: {e}")
            raise TypeError

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, volume):
        try:
            if isinstance(volume, (int, float)) and volume > 0:
                self.__volume = volume
            else:
                raise TypeError("Некорректный тип данных или значение для объема")
        except TypeError as e:
            print(f"Ошибка: {e}")
            raise TypeError

    def discount(self, discValue):
        try:
            if isinstance(discValue, (int, float)) and 1 <= discValue <= 99 :
                return round(self.price * discValue / 100, 2)
            else:
                raise TypeError("Некорректный тип данных или значение для скидки")
        except TypeError as e:
            print(f"Ошибка: {e}")
            raise TypeError

    def calcCount(self, l, w, h):
        try:
            if isinstance(l, (int, float)) and isinstance(w, (int, float)) and isinstance(h, (int, float)) and h > 0 and l > 0 and w > 0:
                count = (h * l * w) // self.volume
                return count
            else:
                raise TypeError("Некорректный тип данных или значение для расчета количества")
        except TypeError as e:
            print(f"Ошибка: {e}")
            raise TypeError
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")
            raise ZeroDivisionError

    def __str__(self):
        return f"Наименование: {self.name}\tЦена: {self.price:.2f}\nОбъем: {self.volume}\n"

    def __add__(self, other):
        try:
            if isinstance(other, product):
                return self.price + other.price
            else:
                raise TypeError("Невозможно выполнить операцию сложения. Ожидается объект класса Product")
        except TypeError as e:
            print(f"Ошибка: {e}")

    def __del__(self):
        print(f"Товар {self.name} удален.")
