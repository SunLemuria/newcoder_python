while True:
    try:
        string = input().lower()
        ch = input().lower()
        count = 0
        for s in string:
            if ch == s:
                count += 1
        print(count)
    except:
        break
