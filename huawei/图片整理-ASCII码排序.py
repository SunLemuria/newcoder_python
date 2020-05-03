while True:
    try:
        string = input().strip()
        print(''.join(sorted(string, key=ord)))
    except:
        break