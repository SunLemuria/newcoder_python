while True:
    try:
        n = int(input().strip())
        nums = [int(num) for num in input().strip().split()]
        order = int(input())
        print(' '.join([str(s) for s in sorted(nums, reverse=bool(order))]))
    except:
        break