# 用的最笨的穷举法,还可以再优化


while True:
    try:
        st1 = input()
        st2 = input()


        def find_longest(s1, s2):
            count = 0
            idx1, idx2 = 0, 1
            n = len(s1)
            for i in range(n):
                for j in range(i, n - 1):
                    if s1[i:j + 1] in s2:
                        if j + 1 - i > count:
                            count = j + 1 - i
                            idx1 = i
                            idx2 = j + 1
            print(s1[idx1:idx2])


        n, m = len(st1), len(st2)
        find_longest(st1, st2) if n <= m else find_longest(st2, st1)
    except:
        break
