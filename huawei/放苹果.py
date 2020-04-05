def fun3(m, n):
    result = 0
    if n == 1:
        return 1
    for i in range(m, -1, -n):
        result += fun3(i, n - 1)
    return result


# dp
def dp_fun(m, n):
    mat = [[0 for i in range(n + 1)] for i in range(m + 1)]
    for i in range(m + 1):
        mat[i][0] = 1
        mat[i][1] = 1
    for i in range(n + 1):
        mat[0][i] = 1
        mat[1][i] = 1
    for i in range(2, m + 1):
        for j in range(2, n + 1):
            if i < j:
                mat[i][j] = mat[i][i]
            else:
                mat[i][j] = mat[i][j - 1] + mat[i - j][j]
    return mat[m][n]


# recursive
def recur_fun(m, n):
    if m == 0 or n == 1:
        return 1
    if m < n:
        return recur_fun(m, m)
    else:
        return recur_fun(m, n - 1) + recur_fun(m - n, n)


while True:
    try:
        inp = [n for n in input().strip().split()]
        m = int(inp[0])
        n = int(inp[1])
        if not 0 <= m <= 10 and 1 <= n <= 10:
            print(-1)
        print(recur_fun(m, n))
    except:
        break
