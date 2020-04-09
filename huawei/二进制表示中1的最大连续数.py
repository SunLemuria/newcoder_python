while True:
    try:
        # num = int(input().strip())
        # length = 0
        # summary = []
        # if num & 1:
        #     length += 1
        # while num:
        #     num = num >> 1
        #     if num & 1:
        #         length += 1
        #     else:
        #         summary.append(length)
        #         length = 0
        # print(max(summary))
        n = int(input().strip())


        def dec2bin(num):
            #  二进制数后
            # base = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('A') + 6)]
            # base = ['0', '1']
            mid = []
            while True:
                if num == 0:
                    break
                num, rem = divmod(num, 2)
                mid.append(str(rem))

            return ''.join([str(x) for x in mid[::-1]])


        bit_string = dec2bin(n)

        print(max(map(len, bit_string.split('0'))))
    except:
        break