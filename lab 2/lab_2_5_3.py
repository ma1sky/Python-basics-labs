import os

while True: 
    left, right = map(int, input().split(' '))

    if left <= right:
        break

counter = 0
for i in range(1, 101):

    filePath = f'lab 2/example/file{i}.txt'
    fileSize = int(os.path.getsize(filePath) / 1024)

    if left <= fileSize <= right:
        counter += 1

print(counter)