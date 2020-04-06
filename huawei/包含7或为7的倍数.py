from math import sqrt, ceil


def contains_7(n):
    if '7' in str(n) or n % 7 == 0:
        return True
    else:
        return False


while True:
    try:
        n = int(input().strip())
        count = 0
        for num in range(7, n + 1):
            if contains_7(num):
                count += 1
        print(count)
    except:
        break
