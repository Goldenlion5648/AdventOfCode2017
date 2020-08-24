from collections import Counter
a='''0: 3
1: 2
2: 4
4: 4
6: 5
8: 6
10: 8
12: 8
14: 6
16: 6
18: 8
20: 8
22: 6
24: 12
26: 9
28: 12
30: 8
32: 14
34: 12
36: 8
38: 14
40: 12
42: 12
44: 12
46: 14
48: 12
50: 14
52: 12
54: 10
56: 14
58: 12
60: 14
62: 14
66: 10
68: 14
74: 14
76: 12
78: 14
80: 20
86: 18
92: 14
94: 20
96: 18
98: 17'''
# a='''0: 3
# 1: 2
# 4: 4
# 6: 4'''
maxes = Counter()
for i in a.split("\n"):
    cur = i.split(": ")
    maxes[int(cur[0])] = int(cur[1])
print(maxes)
poses = Counter()
directions = Counter()
for i in range(max(list(maxes.keys()))+1):
    if i not in maxes:
        maxes[i] = 0
    else:
        directions[i] = 1
    poses[i] = 0

# maxes.sort()
# print(maxes)
print(poses)
curX = 0
curY = 0
timestep = 0
hitSpots = []
caught = True
while caught or curX != max(list(poses.keys())) + 1:
    moved = False
    # if not caught:
    #     curX += 1
    #     print("new curX", curX)
    #     moved = True
    # if timestep == 0:
    if not caught:
        curX += 1
        print("new curX", curX)

    if maxes[curX] != 0 and poses[curX] == curY:
        caught = True
        print("caught and added", curX, maxes[curX])
        hitSpots.append(curX * maxes[curX])
    else:
        caught = False

    # if not caught:
    #     curX += 1
    #     print("new curX", curX)

    #     if maxes[curX] != 0 and poses[curX] == curY:
    #         caught = True
    #         print("caught and added", curX, maxes[curX])
    #         hitSpots.append(curX * maxes[curX])
    #     else:
    #         caught = False
    caught = False
    

    # if not caught:

    # if poses[curX] == curY:

    for i in poses:
        if maxes[i] != 0:
            if poses[i] + directions[i] >= maxes[i]:
                directions[i] = -directions[i]
            elif poses[i] + directions[i] < 0:
                directions[i] = -directions[i]
            
            poses[i] += directions[i]

    timestep += 1
    print("curX", curX)
    print("poses", poses)

# print(maxes)
print(hitSpots)
print(sum(hitSpots))
#part 1 done in 51:11 due to error in bouncing code