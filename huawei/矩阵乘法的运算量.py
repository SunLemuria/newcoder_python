while True:
    try:
        n = int(input())
        ll = []
        for i in range(n):
            ll.append(tuple(map(int, input().split())))
        cal = input()
        brackets = []
        new_shape = None
        total_cal = 0
        for s in cal:
            if s != ')':  # 左括号与字母进栈
                brackets.append(s)
            else:  # 遇到右括号开始计算
                if len(brackets) == 1:
                    # 最后一个右括号,已经计算完毕
                    break
                # 取出栈中的矩阵
                M2 = brackets.pop()
                M1 = brackets.pop()
                brackets.pop()
                if len(M1) == 1:
                    shape1 = ll[ord(M1) - 65]
                else:  # 若取出的为'new_shape', 表示形状不能从ll列表中取出
                    shape1 = new_shape
                if len(M2) == 1:
                    shape2 = ll[ord(M2) - 65]
                else:
                    shape2 = new_shape
                total_cal += shape1[0] * shape1[1] * shape2[1]
                new_shape = (shape1[0], shape2[1])
                brackets.append('new_shape')
        print(total_cal)
    except:
        break
