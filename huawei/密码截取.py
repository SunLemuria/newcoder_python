def check(alist):
    res = 0
    n = len(alist)
    for i in range(n - 1):
        # shuang shu
        if alist[i] == alist[i + 1]:
            first = i
            last = i + 1
            while first >= 0 and last < (n) and alist[first] == alist[last]:
                first -= 1
                last += 1
            res = max(res, last - first - 1)
        # dan shu
        if alist[i - 1] == alist[i + 1]:
            first = i - 1
            last = i + 1
            while first >= 0 and last < (n) and alist[first] == alist[last]:
                first -= 1
                last += 1
            res = max(res, last - first - 1)
    return res


while True:
    try:
        alist = input().strip()
        res = check(alist)
        print(res)
    except:
        break