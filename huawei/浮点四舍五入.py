while True:
    try:
        n = float(input())
        print(int(round(n + 0.1, 0)))
    except:
        break
