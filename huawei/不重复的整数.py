while True:
    try:
        string = input()
        d = {}
        result = ''
        for s in reversed(string):
            if s not in d:
                d[s] = 1
                result += s
            else:
                pass
        print(result)
    except:
        break