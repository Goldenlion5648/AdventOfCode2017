from collections import deque, Counter
a= '''197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63'''
a = list(map(int, a.split(",")))
# a = [3, 4, 1, 5, 3]
skipSize = 0
curPos = 0
# nums = deque([i for i in range(0, 5)])
nums = ([i for i in range(0, 256)])
# nums = ([i for i in range(0, 5)])
# print(nums)
for j in range(len(a)):

    curList = []
    overflowed = False
    beforeAmount = 0
    overflowedAmount = 0
    for i in range(a[j]):
        curList.append(nums[(curPos+i)%len(nums)])
        if (curPos+i)//len(nums) >= 1:
            overflowed = True
            overflowedAmount += 1
            # print("beforeAmount", beforeAmount)
            # print("overflowedAmount", overflowedAmount)
        else:
            beforeAmount += 1
    print("curlist", curList)
    curList.reverse()
    print("reversed", curList)
    before = 0
    after  = 0
    print("overflowed", overflowed)
    if overflowed:
        # if len(curList) == len(nums):
        #     nums = curList.copy()
        # else:
        print(curList[-overflowedAmount:], nums[overflowedAmount:-beforeAmount], curList[0:beforeAmount])
        nums = curList[-overflowedAmount:]+ nums[overflowedAmount:-beforeAmount]+ curList[0:beforeAmount]
        # print(curList[-(beforeAmount):], nums[overflowedAmount:-beforeAmount], curList[0:overflowedAmount])
        # nums = curList[-(beforeAmount):]+ nums[overflowedAmount:-beforeAmount]+ curList[0:overflowedAmount]
        # nums = curList[0:overflowedAmount] + nums[overflowedAmount:-beforeAmount] + curList[-(beforeAmount-1):]
        # before= nums[(curPos+i)%len(nums)+1:curPos]
        # print("before", before)
        # print("first", curList[:(curPos+a[j])%len(nums)+1])
        # print("last", curList[0:len(curList)-(j+i)%len(nums)])
        # nums = curList[:(curPos+a[j])%len(nums)+1] + before + curList[0:len(curList)-(j+i)%len(nums)]
    else:
        before = nums[0:curPos]
        # after = nums[((j+i)%len(nums))+1:]
        after = nums[curPos+len(curList):]
        nums = before + curList + after
    if len(nums) != len(set(nums)):
        print("something went wrong", a[j])
        print(nums)
        print(Counter(nums))
        break
    print("new nums", nums)
    curPos += a[j] + skipSize
    curPos %= len(nums)
    skipSize += 1
    print("curPos", curPos)
    print("skipSize", skipSize)


print(nums[0],  "*", nums[1], "=", nums[0] * nums[1])
#not 5076