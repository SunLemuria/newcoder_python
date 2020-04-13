# -*- coding:utf-8 -*-
class Transform:
    def calcCost(self, A, B):
        # write code here
        a, b = tuple(map(int, raw_input().strip().split(',')))
        diff = 0
        while a or b:
            a_one = a & 1
            b_one = b & 1
            if a_one != b_one:
                diff += 1
            a = a >> 1
            b = b >> 1
        return diff
