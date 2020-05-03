from fractions import Fraction

while True:
    try:
        fraction = [int(x) for x in input().strip().split('/')]
        fraction = Fraction(*fraction)

        denominators = []  # 保存埃及分数的分母
        remain = fraction  # 剩余未被分解的部分
        while remain:  # 只需要确定分母的大小
            result, res = divmod(remain.denominator, remain.numerator)  # 确定分母
            deno = result + 1 if res else result  # 有余数说明不能整除，分子不能直接化为1
            denominators.append(deno)
            remain -= Fraction(1, deno)  # 进入下一循环继续处理， 直到reamin为0
        result = [str(Fraction(1, d)) for d in denominators]
        print('+'.join(result))
    except:
        break