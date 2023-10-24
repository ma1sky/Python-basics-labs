tickets = {}

n = int(input('Число строк: '))

for i in range(n):
    rowNum, seatNum, price = map(int, input('Введите место, ряд и цену: ').split())
    fullNum = (rowNum, seatNum)
    if fullNum not in tickets:
        tickets[fullNum] = []
    if price not in tickets[fullNum]:
        tickets[fullNum].append(price)

for item, price in tickets.items():
    rowNum, seatNum = item
    print(rowNum, seatNum,'-', len(price))