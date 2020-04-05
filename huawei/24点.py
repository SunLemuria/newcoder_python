def trans(num, x):
    total = 0
    if len(x) == 1:
        return abs(num - x[0]) < 0.001  # 递归到最后只剩一个时,直接判断是否相等,若相等表示找到解法,返回非零值,让total变成非零
    else:
        for i in range(len(x)):  # 表示对所有可能位置单独取出
            a = x[i]
            b = x[:]
            b.pop(i)
            total += trans(num - a, b) + trans(num + a, b) + trans(num * a, b) + trans(num / a, b)  # 全部是0表示没有找到答案
        return total


while True:
    try:
        nums = [float(n) for n in input().strip().split()]
        total = trans(24.0, nums)
        print('true' if total else 'false')
    except:
        break
