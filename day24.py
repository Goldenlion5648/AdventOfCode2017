from collections import defaultdict
a='''14/42
2/3
6/44
4/10
23/49
35/39
46/46
5/29
13/20
33/9
24/50
0/30
9/10
41/44
35/50
44/50
5/11
21/24
7/39
46/31
38/38
22/26
8/9
16/4
23/39
26/5
40/40
29/29
5/20
3/32
42/11
16/14
27/49
36/20
18/39
49/41
16/6
24/46
44/48
36/4
6/6
13/6
42/12
29/41
39/39
9/3
30/2
25/20
15/6
15/23
28/40
8/7
26/23
48/10
28/28
2/13
48/14'''
# a='''0/2
# 2/2
# 2/3
# 3/4
# 3/5
# 0/1
# 10/1
# 9/10'''
def explore(curPath, pairs, highest):
    # print("current", curPath)
    for p in pairs:
        if curPath[-1] in p and p not in curPath:
            newCur = curPath[0:-1] + [p] + [p[0] if p[1] == curPath[-1] else p[1]]
            highest = max(explore(newCur, pairs, highest), highest)
    noEnd = curPath[0:-1]
    # print(noEnd)
    endVal = sum(list(map(sum, noEnd)))
    print("ending", endVal)
    return max(highest, endVal)


# a=''''''
# connections = defaultdict(set)
# # print(connections[])
pairs = []
for i in a.split("\n"):
    a, b = list(map(int,i.split("/")))
    # if a != 0:
    # connections[a].add(b)
# connections[b].add(a)
    pairs.append((a, b))
# print(connections)
# pairs.sort()
# print(*pairs, sep="\n")
# allCombos = list()
# curPath
highest = 0
for i in pairs:
    if 0 in i:
        highest = max(highest, explore([i, i[0] if i[1] == 0 else i[1]], pairs, 0))
        # current = 
print(highest)
# for i in current:
#     allCombos.append(i)
# print(current)
# # print(allCombos)
# added = True
# # fringe = current.copy()
# counter = 0
# while added:
#     counter += 1
#     if counter % 10 == 0:
#         print(counter)
#     toBeExtended = []
#     added = False
#     # current = fringe.copy()
#     for pos, j in enumerate(current):
#         for i in pairs:
#             # print(j)
#             # print(j)
#             if i not in j and j[-1] in i:
#                 nextOne = current[pos][0:-1] + [i, i[0] if i[1] == current[pos][-1] else i[1]]
#                 # print("nextOne", nextOne)
#                 if nextOne not in current:
#                     # allCombos.append(current[pos].copy())
#                     toBeExtended.append(current[pos].copy())
#                     # fringe.append(current[pos].copy())
#                     last = current[pos].pop()
#                     current[pos].append(i)
#                     # fringe.append(current[pos])
#                     current[pos].append(i[0] if i[1] == last else i[1])
#                     # print("new current", current)
#                     # temp = current.copy()
#                     # temp.pop()
#                     added = True
#     # print("before current", current)
#     for z in toBeExtended:
#         if z not in current:
#             current.append(z)
#             # print("added z", z)
#     # print("allCombos",allCombos)
#     print("after current",current)
#     print("len current", len(current))
# # print("allCombos", allCombos)
# print("got out")
# maxTotal = 0
# for j in current:
#     j.pop()
# for combo in current:
#     maxTotal = max(maxTotal, sum(list(map(sum, combo))))
# print(maxTotal)

# print("fringe", fringe)       
# for i, p in enumerate(pairs):
#     pos = 0
#     if p[0] != 0:
#         continue
#     seen = [p[1]]
#     chain = [p]
#     print("og", seen)
#     added = True
#     potentials = []
#     while added:
#         added = False
#         for j in pairs:
#             if seen[-1] in j and j not in chain:
#                 seen.append(sum(j)-seen[-1])
#                 chain.append(j)
#                 added = True
#                 break
#             # if seen[-1] in j and j not in seen:
#             #     seen.append(seen[-1][0])
#             #     seen.append(j)
#             #     added = True
#             #     break
#     print(chain)

# for i in connections:  
#     keys = list(connections[i])
#     for j in keys:
#         connections[i].add(pairs[j])
    # for c in keys:
        # connections[i].add(pairs[c])
        # 
#         print(c)
#         connections[i].add(c)
# print(connections)

