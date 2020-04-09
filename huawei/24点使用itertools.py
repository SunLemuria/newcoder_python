# https://www.cnblogs.com/hhh5460/p/6926909.html

import itertools


def twentyfour(cards):
    '''史上最短计算24点代码'''
    for nums in itertools.permutations(cards):  # 四个数
        for ops in itertools.product('+-*/', repeat=3):  # 三个运算符（可重复！）
            # # 构造三种中缀表达式 (bsd)
            # bds1 = '({0}{4}{1}){5}({2}{6}{3})'.format(*nums, *ops)  # (a+b)*(c-d)
            # bds2 = '(({0}{4}{1}){5}{2}){6}{3}'.format(*nums, *ops)  # (a+b)*c-d
            # bds3 = '{0}{4}({1}{5}({2}{6}{3}))'.format(*nums, *ops)  # a/(b-(c/d))
            #
            # for bds in [bds1, bds2, bds3]:  # 遍历
            #     try:
            #         if abs(eval(bds) - 24.0) < 1e-10:  # eval函数
            #             return bds
            #     except ZeroDivisionError:  # 零除错误！
            #         continue
            bd = '{0}{4}{1}{5}{2}{6}{3}'.format(*nums, *ops)
            try:
                if abs(eval(bd) - 24.0) < 1e-10:  # eval函数
                    return bd
            except ZeroDivisionError:  # 零除错误！
                continue

    return 'Not found!'


cards = [int(n) for n in input().split()]
print(twentyfour(cards))
