try :
    while True :
        length = int(input())
        nums = str(input())
        nums = nums.split(" ")
        iNums = []
        for num in nums :
            num = int(num)
            iNums.append(num)
        iNums.sort()
        index = 1
        for num in iNums :
            if index != length :
                print(num, end = " ")
            else :
                print(num)
            index += 1
except EOFError :
    pass