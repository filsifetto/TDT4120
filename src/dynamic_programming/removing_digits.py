from math import inf
def task():
    n = int(input())
    dp = [inf for _ in range(n + 1)]
    dp[0] = 0
    
    for i in range(1, n + 1):
        current_num = str(i)
        dp[i] = min([dp[i - int(c)] for c in current_num]) + 1

    print(dp[n])

task()

