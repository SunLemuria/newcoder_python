while True:
    try:
        num = int(input().strip())
        count = 0
        for i in range(num+1):
            if str(i ** 2).endswith(str(i)):
                count += 1
        print(count)
    except:
        break