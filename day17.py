# from collections import deque
step = 3
step=324
path = [0]
pos = 1
for i in range(1, 50000001):
    # path.rotate(step)
    pos = (pos + step) % (len(path))
    path.insert(pos, i)
    pos += 1
    # if i == 1:
        # path.pop()
        # p
    # while path[0] != 0:
    #     path.rotate(1)
    if i % 100000 == 0:
        print(i)
        break

    # print(pos)
# print(path)
# final = path.index(2017)
# print(path[final-3:final+3])

print(path[0])
#part 1 done in 16:03