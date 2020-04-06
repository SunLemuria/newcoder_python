from math import sqrt, ceil


def is_perfect(n):
    sum_of_divisors = 1
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            sum_of_divisors += i
            sum_of_divisors += int(n / i)
        elif i ** 2 == n:
            sum_of_divisors += i
    return sum_of_divisors == n  # 除去自身


while True:
    try:
        n = int(input().strip())
        count = 0
        for num in range(4, n + 1):
            if is_perfect(num):
                count += 1
        print(count)
    except:
        break