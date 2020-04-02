while True:
    try:
        num = int(input())
        lt = []

        while num != 1:
            for i in range(2, int(num+1)):
                if num % i == 0:  # i是num的一个质因数
                    lt.append(i)
                    num = num / i # 将num除以i，剩下的部分继续分解
                    break
        for n in lt:
            print(n, end=' ')

    except:
        break
