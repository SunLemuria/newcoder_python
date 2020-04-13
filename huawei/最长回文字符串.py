def check(alist):
    res = 0
    n = len(alist)
    for i in range(n - 1):
        # shuang shu
        if alist[i] == alist[i + 1]:
            first = i
            last = i + 1
            while first >= 0 and last < (n) and alist[first] == alist[last]:
                first -= 1
                last += 1
            res = max(res, last - first - 1)
        # dan shu
        if alist[i - 1] == alist[i + 1]:
            first = i - 1
            last = i + 1
            while first >= 0 and last < (n) and alist[first] == alist[last]:
                first -= 1
                last += 1
            res = max(res, last - first - 1)
    return res


while True:
    try:
        alist = input().strip()
        res = check(alist)
        print(res)
    except:
        break


# dp1 O(n^2)
def longestpalindrom(s):
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    result = ''
    for j in range(n-1, -1, -1):
        for i in range(j, n):
            if i == j:
                dp[j][i] = True
            elif i == j + 1:
                dp[j][i] = s[j] == s[i]
            else:
                dp[j][i] = dp[j + 1][i - 1] and s[j] == s[i]
            if dp[j][i] and i+1-j > len(result):
                result = s[j: i+1]
    return result


# dp2 O(n)
def longestpalindrom2(s):
    n = len(s)
    dp = [0 for _ in range(n)]
    result = ''
    for j in range(n-1, -1, -1):
        for i in range(n-1, j-1, -1):
            if i == j:
                dp[i] = True
            elif i == j + 1:
                dp[i] = s[j] == s[i]
            else:
                dp[i] = dp[i - 1] and s[j] == s[i]
            if dp[i] and i+1-j > len(result):
                result = s[j: i+1]
    return result
