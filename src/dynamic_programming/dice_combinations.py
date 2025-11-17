n = int(input())
 
dp = [1 for _ in range(n + 1)]
 
def get(i):
    if i < 0:
        return 0
    return dp[i]
 
for i in range(1, n + 1):
    sm = 0
    for j in range(1, 7):
        sm += get(i - j)
    dp[i] = sm%(10**9 + 7)
 
print(dp[n])
