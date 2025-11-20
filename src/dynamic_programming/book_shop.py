def task():
    n, x = map(int, input().split())
    h = list(map(int, input().split()))
    s = list(map(int, input().split()))
    dp = [[0 for _ in range(x + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        weight = h[i - 1]
        value = s[i - 1]
        for j in range(x + 1):
            if weight <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[n][x])

task()
