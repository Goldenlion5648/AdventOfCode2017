a='''###.#######...#####.#..##
.####...###.##...#..#....
.#.#...####.###..##..##.#
########.#.#...##.#.##.#.
..#.#...##..#.#.##..####.
..#.#.....#....#####..#..
#.#..##...#....#.##...###
.#.##########...#......#.
.#...#..##...#...###.#...
......#.###.#..#...#.####
.#.###.##...###.###.###.#
.##..##...#.#.#####.#...#
#...#..###....#.##.......
####.....######.#.##..#..
..#...#..##.####.#####.##
#...#.#.#.#.#...##..##.#.
#####.#...#.#.#.#.##.####
....###...#.##.#.##.####.
.#....###.#####...#.....#
#.....#....#####.#..#....
.#####.#....#..##.#.#.###
####.#..#..##..#.#..#.###
.##.##.#.#.#.#.#..####.#.
#####..##.#.#..#..#...#..
#.#..#.###...##....###.##'''

# a = '''.........
# .........
# .........
# .....#...
# ...#.....
# .........
# .........
# .........'''
# a='''..#
# #..
# ...'''
board = list(map(list, a.split("\n")))
for i in range(len(board)):
    board[i] = ["."] * 1000 + board[i] + ["."] * 1000
for i in range(400):
    board.insert(0, ["."] * len(board[0]))
    board.append(["."] * len(board[0]))

# print(board)
posX = len(board[0]) // 2
posY = len(board) // 2
# posY = 500
facing = 0
print(posY, posX)
count = 0
for i in range(10000000):
    # print("facing", facing)
    if board[posY][posX] == "#":
        facing = (facing +1) % 4
    elif board[posY][posX] == ".":
        facing = (facing -1) % 4
    elif board[posY][posX] == "2":
        facing = (facing -2) % 4

    if board[posY][posX] == ".":
        board[posY][posX] = "1"
        # print("changed 1")
        # count += 1
    elif board[posY][posX] == "1":
        board[posY][posX] = "#"
        # print("changed 1")
        count += 1
    elif board[posY][posX] == "#":
        board[posY][posX] = "2"
        # print("changed 2")
    elif board[posY][posX] == "2":
        board[posY][posX] = "."
        # print("changed 2")

    if facing == 0:
        posY -= 1
    elif facing == 2:
        posY += 1
    elif facing == 1:
        posX += 1
    elif facing == 3:
        posX -= 1
    # [print(*j) for j in board]
    # for j in board:
    #     print(*j, sep="")
    # print()
    # print(posY, posX)
    if i % 10000 == 0:
        print(i)

# [print(*j) for j in board]
# for j in board:
#     print(*j, sep="")
print("infect", count)
#part 1 done in 29:53, copy paste error, as well as inserting rows correctly, and discord