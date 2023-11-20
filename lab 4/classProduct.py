class product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def price(self, name):
        self.__name = name

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, price):
        if price >= 0:
            self.__price = price
        else: 
            print("Некорректное значение цены")

    @property
    def volume(self):
        return self.__volume
    
    @volume.setter
    def volume(self, volume):
        if volume > 0:
            self.__volume = volume
        else :
            print("Некорректное значение объема")

    def discount(self, discValue):
        if 1 <= discValue <= 99 :
            return(round(self.price * discValue / 100, 2)) 
        else:
            print("Некорректное значение")
    
    def calcCount(self, l, w, h):
        if h and l and w > 0:
            count = (h * l * w) // self.volume
            return count
        else: 
            print("Некорректное значение объема")
    
    def __str__(self):
        return f"Наименование: {self.name} \t Цена: {self.price:.2f} \nОбъем: {self.volume}\n"
    
    def __add__(self, other):
        return self.price + other.price
    
    def __del__(self):
        print(f"Товар {self.name} удален.")

