while True:
    try:
        n = int(input())
        order = int(input())
        arr = [input() for i in range(n)]
        arr = sorted(arr, key=lambda x: int(x.split()[1]), reverse=not order)
        for i in arr:
            print(i)
    except:
        break
