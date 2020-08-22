from collections import deque
import sys
a = 277678
length = 600
start = length // 2
b = [deque([0]*length) for i in range(length)]
Xpos = length // 2
Ypos = length // 2
b[Ypos][Xpos] = 1
dist = 1
direction = 1
count = 1
numToFind = 277678
for i in range(600):
    while Xpos -  start< dist:
        Xpos += 1
        count += 1
        print(Ypos, Xpos)
        b[Ypos][Xpos] = count
        if count == numToFind:
            print(abs(Ypos - start) + abs(Xpos - start))
            sys.exit(1)
    while start -  Ypos< dist:
        Ypos -= 1
        count += 1
        b[Ypos][Xpos] = count
        if count == numToFind:
            print(abs(Ypos - start) + abs(Xpos - start))
            sys.exit(1)
    while start -  Xpos< dist:
        Xpos -= 1
        count += 1
        b[Ypos][Xpos] = count
        if count == numToFind:
            print(abs(Ypos - start) + abs(Xpos - start))
            sys.exit(1)
    while Ypos -  start< dist:
        Ypos += 1
        count += 1
        b[Ypos][Xpos] = count
        if count == numToFind:
            print(abs(Ypos - start) + abs(Xpos - start))
            sys.exit(1) 
    dist += 1
#1 8 16 24 32
# [print(*i) for i in b]
#part 1 done in 25:49