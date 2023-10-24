s = str(input('Строка s = '))
x = str(input('Строка x = '))

def subStrCheck(string, substring):
    return string.lower().find(substring.lower())

def subStrDel(string, substring):
    strList = list(string)
    start = subStrCheck(string, substring)
    end = start + len(substring)

    if subStrCheck(string, substring) != -1:
        for i in range(start, end):
            strList.pop(start)        
        return ''.join(strList)
    else: 
        return string

while subStrCheck(s, x) != -1:
    s = subStrDel(s, x)

print('Измененная строка : ',s)