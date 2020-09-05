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
    board[i] = ["."] * 500 + board[i] + ["."] * 500
for i in range(200):
    board.insert(0, ["."] * len(board[0]))
    board.append(["."] * len(board[0]))

print(board)
posX = len(board[0]) // 2
posY = len(board) // 2
# posY = 500
facing = 0
print(posY, posX)
count = 0
for i in range(10000):
    print("facing", facing)
    if board[posY][posX] == "#":
        facing = (facing +1) % 4
    else:
        facing = (facing -1) % 4

    if board[posY][posX] == ".":
        board[posY][posX] = "#"
        print("changed 1")
        count += 1
    else:
        board[posY][posX] = "."
        print("changed 2")

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
    print()
    print(posY, posX)

# [print(*j) for j in board]
for j in board:
    print(*j, sep="")
print("infect", count)
#part 1 done in 29:53, copy paste error, as well as inserting rows correctly, and discord