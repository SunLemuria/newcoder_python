while True:
    try:
        n = int(input().strip())
        mass = [int(m) for m in input().split()]
        nums = [int(x) for x in input().split()]

        possible_weights = {0}

        for i in range(n):
            temp = possible_weights.copy()
            for j in range(nums[i]):
                for t in temp:
                    possible_weights.add(t + mass[i] * (j + 1))
        print(len(possible_weights))
    except:
        break