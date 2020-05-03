# https://www.nowcoder.com/practice/dbace3a5b3c4480e86ee3277f3fe1e85?tpId=37&tqId=21299&rp=0&ru=/ta/huawei&qru=/ta/huawei/question-ranking

while True:
    try:
        n = int(input().strip())
        s = n ** 3
        avg = int(s / n)
        if s % 2 == 0:  # 偶数
            result = str(avg-1) + "+" + str(avg+1)
            for i in range(n // 2 - 1):
                diff = 2 * i + 3
                result = str(avg - diff) + '+' + result + '+' + str(avg + diff)
        else:
            result = str(avg)
            for i in range(n // 2):
                diff = 2 * (i + 1)
                result = str(avg - diff) + '+' + result + '+' + str(avg + diff)
        print(result)
    except:
        break