while True:
    try:
        x = input()
        for k in range(0, 4):
            x = 4 * k
            y = 25 - 7 * k
            z = 75 + 3 * k
            print("{0} {1} {2}".format(x, y, z))
    except:
        break
