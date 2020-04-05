from math import sqrt


def is_prime(n):
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True


while True:
    try:
        even = int(input())
        pivot = int(even / 2)
        for bias in range(0, pivot):
            a = pivot - bias
            b = pivot + bias
            if is_prime(a) and is_prime(b):
                print(a)
                print(b)
                break

    except:
        break
