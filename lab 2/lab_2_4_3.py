import os
import random as r

os.mkdir('lab 2/example')
fileInList = ['fileIn' + str(i) for i in range(1, 101)]
for fileInName in fileInList:
    with open(f'lab 2/example/{fileInName}.txt', 'wb') as fileIn:
        size = r.randint(1, 100)
        fileIn.write(b'\x00' * (size*1024))
    fileIn.close()