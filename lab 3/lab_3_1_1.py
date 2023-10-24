from functools import reduce
def intersec(*lists: list) -> bool:
    interOfSets = reduce(lambda set1, set2: set1&set2, list(map(set, lists)))
    return True if len(interOfSets) == 0 else False
list1 = [1, 2, 3, 4 ,5 ]
list2 = [1, 3, 4, 5, 6]
list3 = [1, 3, 4, 7]
print(intersec(list1, list2, list3))