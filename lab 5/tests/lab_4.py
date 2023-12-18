from classProduct import product
from classVehicle import vehicle
from classPhone import phone

try:
    l, w, h = map(float, input("Объем ящика для товара: ").split())
except ValueError:
    print("Неверный формат вводенных данных")


milk = product("Молоко", 130)
milk.volume = 13

apples = product("Яблоки", 100)
apples.volume = 20

print(f"Цена за {milk.name} со скидкой =",milk.discount(23.4),"\n")
print(f"Количество {apples.name}, которые можно уместить в коробку объемом {l * w * h} =",apples.calcCount(l, w, h) ,"\n")
print(f"Цена за {milk.name} и {apples.name} =", milk + apples,"\n")
print(apples)
print(milk)

BMW = vehicle("BMW", 13000, 2000)
Audi = vehicle("Audi", 10000, 3000)

print(f"Общий вес {BMW.name} и {Audi.name} =", BMW + Audi)
print(BMW)
print(Audi)

iphone = phone("iphone", 5000, 10)
samsung = phone("samsung", 3000, 3)
print(iphone)
print(samsung)