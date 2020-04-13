while True:
    try:
        ip = list(map(int, input().strip().split('.')))
        ip_decimal = int(input().strip())
        result = 0
        k = 0
        for i in reversed(ip):
            result += i * 2 ** k
            k += 8
        print(result)

        k = 0
        temp = 0
        result2 = list()
        while 1:
            k += 8
            temp = (ip_decimal - temp) % (2 ** k) // (2 ** (k - 8))  # 减掉前面已经处理过的低位数字
            if temp <= 0:
                break
            result2.append(str(int(temp)))
        print('.'.join(reversed(result2)))
    except:
        break
