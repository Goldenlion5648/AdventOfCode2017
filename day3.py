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
def findValue(board, Ypos, Xpos):
    total = 0
    for i in range(-1, 2, 1):
        for j in range(-1, 2, 1):
            if i == 0 and j == 0:
                continue
            total += board[Ypos+i][Xpos+j]
    return total


for i in range(600):
    while Xpos -  start< dist:
        Xpos += 1
        count = findValue(b, Ypos, Xpos)
        print(Ypos, Xpos)
        b[Ypos][Xpos] = count
        if count > numToFind:
            # print(abs(Ypos - start) + abs(Xpos - start))
            print(count)
            sys.exit(1)
    while start -  Ypos< dist:
        Ypos -= 1
        count = findValue(b, Ypos, Xpos)
        b[Ypos][Xpos] = count
        if count > numToFind:
            # print(abs(Ypos - start) + abs(Xpos - start))
            print(count)
            sys.exit(1)
    while start -  Xpos< dist:
        Xpos -= 1
        count = findValue(b, Ypos, Xpos)
        b[Ypos][Xpos] = count
        if count > numToFind:
            # print(abs(Ypos - start) + abs(Xpos - start))
            print(count)
            sys.exit(1)
    while Ypos -  start< dist:
        Ypos += 1
        count = findValue(b, Ypos, Xpos)
        b[Ypos][Xpos] = count
        if count > numToFind:
            # print(abs(Ypos - start) + abs(Xpos - start))
            print(count)
            sys.exit(1) 
    dist += 1
#1 8 16 24 32
# [print(*i) for i in b]
#part 1 done in 25:49
#part 2 done in 5:20