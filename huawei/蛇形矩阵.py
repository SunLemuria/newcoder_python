while True:
    try:
        n = int(input().strip())
        ll = [[0 for _ in range(n)] for _ in range(n)]
        i, j = 0, 0
        current_num = 1
        max_num = n * (n + 1) / 2
        while not current_num > max_num:
            ll[i][j] = current_num
            current_num += 1
            # i, j的更新
            if i == 0:  # 更新到了第0行时,要跳到j+1行,0列
                i = j + 1
                j = 0
            else:
                i -= 1  # 没到第0行,就继续往右上方移动
                j += 1
        for row in ll:
            print(' '.join([str(r) for r in row if r]))
    except:
        break
