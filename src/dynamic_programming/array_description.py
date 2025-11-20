def task():
    n, m = map(int, input().split())
    x = [1] + list(map(int, input().split()))
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1

    

    for i in range(1, n + 1):
        if x[i - 1] != 0:
            dp[i] = dp[i - 1]
        else:
            if x[i] == 1 or x[i] == m:
                if abs(x[i - 2] - x[i]) < 2:
                    dp[i] = dp[i - 2] + 1
                else:
                    dp[i] = dp[i - 2]
            else:
                if x[i] == x[i - 2]:
                    dp[i] = dp[i - 2] + 2
                elif abs(x[i] - x[i - 2] < 2):
                    dp[i] = dp[i - 2] + 1
                else:
                    dp[i] = dp[i - 2]

    print(dp[n])

task()
