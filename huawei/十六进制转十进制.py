def convert(n):
    d = 0
    for c in n:
        if ord(c) >= 65:
            num = 10 + ord(c) - 65
        else:
            num = ord(c) - 48
        d = d * 16 + num
    print(d)


def main():
    while True:
        try:
            num = input()[2:]
            convert(num)
        except:
            break


if __name__ == "__main__":
    main()
