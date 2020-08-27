factor_a=  16807
factor_b = 48271
start_a = 65
start_b = 8921
start_a = 512
start_b = 191

div = 2147483647
prodA = [start_a]
prodB = [start_b]
count = 0
prevA = start_a
prevB = start_b
for i in range(5000000):
    curA = (prevA * factor_a)%div
    curB = (prevB * factor_b)%div
    # prodA.append((prodA[-1] * factor_a)%div)
    # prodB.append((prodB[-1] * factor_b)%div)
    while curA % 4 != 0:
        prevA=curA
        curA = (prevA * factor_a)%div

    while curB % 8 != 0:
        prevB=curB
        curB = (prevB * factor_b)%div
    if curA % 4 == 0 and curB % 8 == 0:
        if bin(curA)[-16:] == bin(curB)[-16:]:
            count += 1
            # print(i)
            # print(curA, curB)
            # break
    if i % 100000 == 0:
        print(i)
    prevA=curA
    prevB=curB

# print(prodA)
# print(prodB)
print(count)
# Generator A starts with 512
# Generator B starts with 191
#part 1 done in 14:24
#part 2 done in 10:11