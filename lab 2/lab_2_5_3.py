import os

while True: 
    left, right = map(int, input().split(' '))

    if left <= right:
        break

counter = 0
for i in range(1, 101):

    fileInPath = f'lab 2/example/fileIn{i}.txt'
    fileInSize = int(os.path.getsize(fileInPath) / 1024)

    if left <= fileInSize <= right:
        counter += 1

print(counter)