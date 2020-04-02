while True:
    try:
        string = input()
        d = {}
        count = 0
        for s in string:
            if s not in d:
                d[s] = 1
                count += 1
            else:
                pass
        print(count)
    except:
        break
