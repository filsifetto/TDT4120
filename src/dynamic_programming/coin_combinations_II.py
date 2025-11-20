def task():
    n, m = map(int, input().split())
    
    values = list(map(int, input().split()))
    values.sort()
    
    dp = [[0 for _ in range(m + 1)] for i in range(n)]
 
    dp[0][0] = 1
 
    for i in range(n):
        val = values[i]
        for j in range(val, m + 1):
            dp[i][j] = sum([dp[k][j - val] for k in range(i + 1)])%(10**0 + 7)
 
    sm = 0
    for i in range(n):
        sm = (sm + dp[i][-1])%(10**9 + 7)
    print(sm)
 
task()

