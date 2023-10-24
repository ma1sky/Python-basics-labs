import os
import random as r

os.mkdir('lab 2/example')
fileList = ['file' + str(i) for i in range(1, 101)]
for fileName in fileList:
    with open(f'lab 2/example/{fileName}.txt', 'wb') as file:
        size = r.randint(1, 100)
        file.write(b'\x00' * (size*1024))
    file.close()