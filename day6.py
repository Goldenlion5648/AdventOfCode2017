from collections import Counter
a = "11 11  13  7   0   15  5   5   4   4   1   1   7   1   15  11"
# a = "0 2 7 0"
a = list(map(int, a.split()))
print(a)
seen = set()
seen.add(tuple(a))
def findMin(a):
    maxSeen = -1
    pos = -1
    for i in range(len(a)):
        if a[i] > maxSeen:
            pos = i
            maxSeen = a[i]
    return pos
pos = findMin(a)
count = 0
timeMap = dict()
while True:
    print("pos", pos)
    num = a[pos]
    a[pos] = 0
    pos = (pos + 1) % len(a)
    while num > 0:
        a[pos] += 1
        pos = (pos + 1) % len(a)
        num -= 1
    if tuple(a) in seen:
        print("time", count - timeMap[tuple(a)])
        break
    else:
        seen.add(tuple(a))
        timeMap[tuple(a)] = count
    print(a)
    pos = findMin(a)
    count += 1
print(len(seen))
#part 1 done in 10:05

#part 2 done in 8:15