def judge(rem, dif):  # 用rem中的数组通过加减运算得到dif
    if len(rem) == 1:
        return abs(rem[0]) == dif
    b = rem[:]
    a = b.pop(0)
    return judge(b, dif + a) or judge(b, dif - a)


while True:
    try:
        n = int(input().strip())
        nums = [int(n) for n in input().strip().split()]

        if sum(nums) % 2 != 0:
            print('false')
        else:
            multiple_of_5 = []
            multiple_of_3 = []
            remain = []
            for n in nums:
                if n % 5 == 0:
                    multiple_of_5.append(n)
                elif n % 3 == 0:
                    multiple_of_3.append(n)
                else:
                    remain.append(n)
            sum_of_5 = sum(multiple_of_5)
            sum_of_3 = sum(multiple_of_3)
            diff = abs(sum_of_5 - sum_of_3)
            if judge(remain, diff):   # 用remain中的数组通过加减运算得到diff
                print('true')
            else:
                print('false')
    except:
        break


