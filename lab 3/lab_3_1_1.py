from functools import reduce
def intersec(*lists: set) -> bool:
    interOfSets = reduce(lambda set1, set2: set1&set2, list(map(set, lists)))
    return len(interOfSets) == 0

while True:
    try:
        inStr = list(str(item) for item in input('Введите числовые множества : ').split(';'))
        inData = list(map(lambda item: set(int(i) for i in item.split()), inStr))
        print(intersec(*inData))
    except ValueError:
        print('Несоответствие формата данных')