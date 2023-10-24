numbers = [int(i) for i in input('Введите список чисел : ').split()]

k = 0

def findStart(someList):
    start = 0
    for item in someList:
        if item == 0:
            start += 1
        else:
            break
    return start

def findEnd(someList, start):
    end = start
    for i in range(start, len(someList)):
        if someList[i] == 0:
            break
        else: 
            end += 1
    return end

def checkList(someList):
    for item in someList:
        if item > 0:
            return True

while checkList(numbers):
    print(findStart(numbers), findEnd(numbers, findStart(numbers)))

    ai = findStart(numbers)
    aj = findEnd(numbers, ai)
    for i in range(ai, aj):
        numbers[i] -= 1
    print(numbers)
    k += 1

print('Минимальное кол-во операции = ',k) 