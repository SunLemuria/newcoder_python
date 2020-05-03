def add_long(s1, s2):
    max_len = max(len(s1), len(s2))
    s1 = s1.rjust(max_len, '0')
    s2 = s2.rjust(max_len, '0')

    result = ''
    flag = 0  # 进位
    for i in range(max_len):
        j = max_len - i - 1
        this = int(s1[j]) + int(s2[j]) + flag
        if this > 9:
            flag = 1
            this -= 10
        else:
            flag = 0
        result = str(this) + result
    return result


while True:
    try:
        # s1 = input().strip()
        # s2 = input().strip()
        s1 = '1361680'
        s2 = '4750391361917973848562'

        print(add_long(s1, s2))
    except:
        break