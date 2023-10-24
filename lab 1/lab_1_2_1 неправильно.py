numbers = list(map(int, input('Введите список чисел : ').split()))

k = 0

def checkList(someList):
    for item in someList:
        if item > 0:
            return True

def decOfListNums(someList, start, end):
    for i in range(start-1, end):
        if someList[i] > 0:
            someList[i] -= 1

while checkList(numbers):
    ai, aj = map(int, input('Введите отрезок [ai, aj] : ').split())
    if 1 <= ai <= aj <= len(numbers):
        k += 1
        decOfListNums(numbers, ai, aj)
        
    else:
        print('Отрезок введён некорректно ')

print('Минимальное кол-во операции = ',k) 