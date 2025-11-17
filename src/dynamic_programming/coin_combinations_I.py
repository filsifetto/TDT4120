n, goal = map(int, input().split())
values = list(map(int, input().split()))
values.sort()
 
dp = [0 for _ in range(goal + 1)]
dp[0] = 1
 
for i in range(goal):
    for c in values:
        if i + c <= goal:
            dp[i + c] = (dp[i + c] + dp[i])%(10**9 + 7)
            # dp[i + c] += dp[i]
        else:
            break
print(dp[goal])

