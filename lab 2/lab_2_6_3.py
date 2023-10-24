lenOfAlph = ord('z') - ord('a')

def delSymbols(data):
    syms = [' ',',','.','\n','"','?','!','-','U+2019','”','’','“','“','…','—']
    buffer = data
    for item in syms:
        final = buffer.replace(item, '')
        buffer = final
    return final.lower()

def calcPart(lenOfList, sum):
    return float((sum/lenOfList)*100)

with open('lab 2/article.txt', 'r') as inData:
    text = inData.read()
    lenOfText = len(list(text))

    unsortedDict = {}
    for sym in range(ord('a'), ord('z')+1):
        unsortedDict[chr(sym)] = calcPart(lenOfText, list(text).count(chr(sym)))
inData.close()

with open('lab 2/article_solved.txt', 'w') as outData:
    
    sortedDict = sorted(unsortedDict.items(), key = lambda item: item[1], reverse=True)
    for item in sortedDict:
        outData.write(f'{item[0]}: {"{:.4f}".format(item[1])}\n')
outData.close()