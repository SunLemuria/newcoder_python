def str_cmp(n1, n2):  # 长度相同的数字字符串, 逐位比较大小, 若有任何一位上n1<n2, 返回True
    for i in range(len(n1)):
        if n1[i] < n2[i]:
            return True
    else:
        return False


def get_sign(n):
    # 正数返回True
    return not n.startswith('-')


def compute(n1, n2):
    s1 = get_sign(n1)  # 若n1为正数s1为True
    s2 = get_sign(n2)  # 若n2为正数s2为True
    # 字符串中除'-'外的数字部分
    numbers1 = n1 if s1 else n1[1:]
    numbers2 = n2 if s2 else n2[1:]

    maxlen = max(len(numbers1), len(numbers2))
    x = numbers1.zfill(maxlen)
    y = numbers2.zfill(maxlen)

    result = ''  # 结果字符串
    carry_flag = 0  # 进位标志
    # 根据符号选择执行加法或减法
    if s1 ^ s2:  # 两个数符号不相同时,get_sign值不同,异或为True,执行减法
        # 判断哪个大
        if str_cmp(x, y):
            s1, s2 = s2, s1
            x, y = y, x
        # 以大减小, 再取大的符号
        for i in range(1, len(y) + 1):
            first = int(x[-i]) - carry_flag
            second = int(y[-i])
            if first < second:
                carry_flag = 1
                first += 10
            else:
                carry_flag = 0
            result += str(first - second)
        result = result.rstrip('0')
        if result == '':
            result = '0'
        else:
            sign = '-' if not s1 else ''  # n1绝对值大,所以结果符号与n1相同
            result = sign + result[::-1]
        return result
    else:
        for i in range(1, maxlen + 1):
            temp = int(x[-i]) + int(y[-i]) + carry_flag
            if temp > 9:
                carry_flag = 1
                temp = temp - 10
            else:
                carry_flag = 0
            result += str(temp)
        if carry_flag > 0:
            result += str(carry_flag)
        # 在这个条件分支两个数符号相同,只判断一个即可
        sign = '-' if not s1 else ''
        return sign + result[::-1]


while True:
    try:
        num1 = input().strip()
        num2 = input().strip()
        print(compute(num1, num2))
    except:
        break
