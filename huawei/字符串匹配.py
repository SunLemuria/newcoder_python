while True:
    try:
        s1 = input().strip()
        s2 = input().strip()
        print(str(all(s in s2 for s in s1)).lower())
    except:
        break