while True:
    try:
        D = {'3': 0, '4': 1, '5': 2, '6': 3, '7': 4, '8': 5, '9': 6, '10': 7, 'J': 8, 'Q': 9, 'K': 10, 'A': 11, '2': 12,
             'joker': 13, 'JOKER': 14}
        a, b = input().split('-')
        s1, s2 = a.split(), b.split()
        if a == 'joker JOKER' or b == 'joker JOKER':  # 大小王直接胜出
            print('joker JOKER')
        elif len(s1) == len(s2):  # 长度相同,如对子之间,三个之间,炸弹之间,顺子之间,比较第一个字母即可
            print(a if D[s1[0]] > D[s2[0]] else b)
        elif len(a) == 7:  # 炸弹的情况, 且另一个不是炸弹,因为长度不相同
            print(a)
        elif len(b) == 7:
            print(b)
        else:  # 长度不相同,没有炸弹,也没有大小王
            print('ERROR')
    except:
        break
