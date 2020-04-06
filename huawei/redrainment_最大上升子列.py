while True:
    try:
        n = int(input().strip())

        array = [int(input().strip()) for _ in range(n)]

        dp = [1 for _ in range(n)]
        max_steps = 0
        for i in range(1, n):
            for j in range(0, i):
                if array[j] < array[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            max_steps = max(max_steps, dp[i])
        print(max_steps)
    except:
        break
