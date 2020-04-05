import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    arrays = []

    while True:
        try:
            # 读取每一行
            line = sys.stdin.readline().strip()
            if not line:
                break
            # 把每一行的数字分隔后转化成int列表
            values = list(map(int, line.split(',')))
            arrays.append(values)
        except:
            break
    answers = []
    sign = 0
    length = len(arrays)
    idx1 = 0
    idx2 = n
    empty = 0
    while True:
        to_extend = arrays[sign][idx1: idx2]
        if not to_extend:
            empty += 1
        if empty >= 100:
            break
        answers.extend(to_extend)
        sign += 1
        if sign >= length and sign % length == 0:
            sign = 0
            idx1 += n
            idx2 += n
    print(', '.join(str(a) for a in answers))
