# a = input()
# board = [a.split("\n")]
board = []
for i in range(128):
    board.append(list(input()))
print(board)
def explore(board, seen2, start):
    # print("got", sorted(seen2))
    seen = seen2.copy()
    # fringe = fringe2.copy()
    fringe = [start]
    while len(fringe) > 0:
        pos = fringe.pop()
        # if board[fringe[pos][0]][fringe[pos][1]] == "1":
        potential = (pos[0]-1, pos[1])
        if potential[0] >= 0 and board[potential[0]][potential[1]] == "1" and potential not in seen:
            fringe.append(potential)
            seen.append(potential)
        potential = (pos[0]+1, pos[1])
        if potential[0] < len(board) and board[potential[0]][potential[1]] == "1" and potential not in seen:
            fringe.append(potential)
            seen.append(potential)
        potential = (pos[0], pos[1]-1)
        if potential[1] >= 0 and board[potential[0]][potential[1]] == "1" and potential not in seen:
            fringe.append(potential)
            seen.append(potential)
        potential = (pos[0], pos[1]+1)
        if potential[1] < len(board) and board[potential[0]][potential[1]] == "1" and potential not in seen:
            fringe.append(potential)
            seen.append(potential)
        # fringe.pop()
        # print("fringe", fringe)
    # print("returning", sorted(seen))
    return seen
fringe = []
seen = []
islandCount = 0

for y in range(len(board)):
    # print(y)
    for x in range(len(board[0])):
        print(y, x)
        added = False
        if board[y][x] == "1" and (y, x) not in seen:
            seen.append((y, x))
            seen = explore(board, seen, (y, x))
            # potential = (y-1, x)
            # if potential[0] >= 0 and board[potential[0]][potential[1]] == "1" and potential not in seen:
            #     print("found", potential)
            #     # fringe.append(potential)
            #     seen.append(potential)
            #     seen = explore(board, seen, (y, x)).copy()
            #     islandCount += 1
            #     added = True
            # potential = (y+1, x)
            # if potential[0] < len(board) and board[potential[0]][potential[1]] == "1" and potential not in seen:
            #     print("found", potential)
            #     # fringe.append(potential)
            #     seen.append(potential)
            #     seen = explore(board, seen, (y, x)).copy()
            #     islandCount += 1
            #     added = True
            # potential = (y, x-1)
            # if potential[1] >= 0 and board[potential[0]][potential[1]] == "1" and potential not in seen:
            #     print("found", potential)
            #     # fringe.append(potential)
            #     seen.append(potential)
            #     seen = explore(board, seen, (y, x)).copy()
            #     islandCount += 1
            #     added = True
            # potential = (y, x+1)
            # if potential[1] < len(board) and board[potential[0]][potential[1]] == "1" and potential not in seen:
            #     print("found", potential)
            #     # fringe.append(potential)
            #     seen.append(potential)
            #     seen = explore(board, seen, (y, x)).copy()
            #     islandCount += 1
            #     added = True
            # if added == False:
            islandCount += 1
            
            # islandCount += 1

seen.sort()
print(seen)

print("islandCount", islandCount)