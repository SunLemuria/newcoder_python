def dp(n):
    # 初始位置在0,每次按掷出点数移动,移动时经过位置n的概率是多少
    f0 = 1
    f1 = 1 / 6
    f2 = 1 / 6 * (f0 + f1)
    f3 = 1 / 6 * (f0 + f1 + f2)
    f4 = 1 / 6 * (f0 + f1 + f2 + f3)
    f5 = 1 / 6 * (f0 + f1 + f2 + f3 + f4)
    result = 1 / 6 * (f0 + f1 + f2 + f3 + f4 + f5)
    for _ in range(7, n + 1):
        f0 = f1
        f1 = f2
        f2 = f3
        f3 = f4
        f4 = f5
        f5 = result
        result = 1 / 6 * (f0 + f1 + f2 + f3 + f4 + f5)
    print(result)
    print(2/7)


dp(8)
