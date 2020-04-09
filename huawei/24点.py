# 无法找到形如3*5+1*9的解,只能找到1*(3*5+9)或9+1*3*5
# 因为每次只pop出来一个,
# 如pop出来3,剩下的三个数5,1,9需要组合成8或21或25,
# pop出来5,剩下的三个数3,1,9需要组合成4.8或19或29,
# pop出来1,剩下的三个数3,5,9需要组合成23或24或25,其中找到1*(3*5+9)
# pop出来9,剩下的三个数3,5,1需要组合成24/9或15或24*9,其中找到9+1*3*5
def trans(num, x):
    total = 0
    if len(x) == 1:
        return abs(num - x[0]) < 0.001  # 递归到最后只剩一个时,直接判断是否相等,若相等表示找到解法
    else:
        for i in range(len(x)):  # 表示对所有可能位置单独取出
            a = x[i]
            b = x[:]
            b.pop(i)
            total += trans(num - a, b) or trans(num + a, b) or trans(num * a, b) or trans(num / a, b)  # 全部是0表示没有找到答案
        return total


while True:
    try:
        nums = [float(n) for n in input().strip().split()]
        total = trans(24.0, nums)
        print('true' if total else 'false')
    except:
        break
