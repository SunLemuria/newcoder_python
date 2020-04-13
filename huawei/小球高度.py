while True:
    try:
        h = int(input().strip())
        total_s = h + h + h / 2 + h / 4 + h / 8
        h5 = h / 32
        print(round(total_s, 3))
        print(round(h5, 5))
    except:
        break