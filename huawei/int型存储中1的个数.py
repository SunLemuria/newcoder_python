while True:
    try:
        num = int(input())
        num_of_one = 0
        while num:
            if num & 1:  # 用位运算来判断
                num_of_one += 1
            num = num >> 1
        print(num_of_one)
    except:
        break
