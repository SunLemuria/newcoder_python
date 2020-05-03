while True:
    try:
        string = input().strip()
        count = dict()
        for s in string:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
        least_time = min(count.values())
        for s in string:
            if count[s] == least_time:
                continue
            else:
                print(s, end='')
        print()
    except:
        break
