def substring_repeat(pd):
    for i in range(len(pd)  -3):
        if pd.count(pd[i:i+3]) > 1:
            return True
    return False


def check(pd):
    if len(pd) <= 8:
        return False
    upper, lower, digit, other = 0, 0, 0, 0
    for s in pd:
        if s.isupper():
            upper = 1
        elif s.islower():
            lower = 1
        elif s.isdigit():
            digit = 1
        else:
            other = 1
    if upper + lower + digit + other <= 2:
        return False
    if substring_repeat(pd):
        return False
    return True


while True:
    try:
        passwd = input().strip()
        result = "OK" if check(passwd) else "NG"
        print(result)
    except:
        break