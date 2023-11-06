def findMax(data: dict) -> int:
    max = 0
    for item in data:
        if len(item[1]) > max:
            max = len(item[1])
            fav = item
    return fav
with open('контроша 1/out.txt', 'w') as fileOut:
    with open('контроша 1/in.txt', 'r') as fileIn:
        n = int(fileIn.readline())
        transactions = {}
        for item in range(0, n):
            sys, num = fileIn.readline().strip('\n').split(' ')
            if sys not in transactions:
                transactions[sys] = []
            if num not in transactions[sys]:
                transactions[sys].append(num)
        print(transactions)
        print(findMax(transactions), file=fileOut)

fileIn.close()
fileOut.close()