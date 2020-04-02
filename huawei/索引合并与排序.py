while True:
    try:
        n = int(input())
        d = {}
        for _ in range(n):
            key, value = tuple(map(int, input().split()))
            if key not in d:
                d[key] = value
            else:
                d[key] += value
        d = sorted(d.items(), key=lambda x: x[0])
        for k, v in d:
            print(k, v)
    except:
        break
