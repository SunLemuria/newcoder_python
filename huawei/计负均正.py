while True:
    try:
        n = int(input().strip())
        nums = [int(n) for n in input().strip().split()]
        sum_of_p = 0
        num_of_p = 0
        num_of_n = 0
        for num in nums:
            if num == 0:
                continue
            elif num > 0:
                sum_of_p += num
                num_of_p += 1
            else:
                num_of_n += 1
        print(num_of_n, round(sum_of_p/num_of_p, 1))
    except:
        break