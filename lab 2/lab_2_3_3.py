import csv

def calcSum(data, id):
    sum = 0
    for item in data:
        if item.get('ClientID') == id:
            sum += float(item.get('Price'))
    return sum

def findFav(data, id):
    ordersSet = set()
    ordersList = list()
    for item in data:
        if item.get('ClientID') == id:
            ordersList.append(item.get('ProductID'))
            ordersSet.add(item.get('ProductID'))
    max = 0
    for item in ordersSet:
        if ordersList.count(item) > max:
            max = ordersList.count(item)
            fav = item
    return fav

with open('lab 2/orders.csv', 'r', newline="") as orders:
    with open('lab 2/analytics.csv', 'w', newline="") as anal:
        reader = csv.DictReader(orders, delimiter=";")
        
        info = list()
        analytics = list()
        clientsSet = set()
        clientsDict = dict()

        for order in reader:
            info.append(order)
            clientsSet.add(order.get("ClientID"))

        for item in clientsSet:
            clientsDict["ClientID"] = item
            clientsDict["FavProduct"] = findFav(info, item)
            clientsDict["Sum"] = calcSum(info, item)
            analytics.append(clientsDict.copy())
        
        cols = ["ClientID", "FavProduct", "Sum"]
        writer = csv.DictWriter(anal, delimiter=";", fieldnames=cols)
        writer.writeheader()
        writer.writerows(analytics)
    anal.close()
orders.close()