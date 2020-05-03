# https://www.nowcoder.com/practice/c4f11ea2c886429faf91decfaf6a310b?tpId=37&tqId=21303&rp=0&ru=/ta/huawei&qru=/ta/huawei/question-ranking

while True:
    try:
        n = input()
        nums = [int(x) for x in input().strip().split()]
        m = input()
        nums.extend([int(x) for x in input().strip().split()])
        print(''.join([str(x) for x in sorted(set(nums))]))
    except:
        break