def task():
    t = int(input())
    tasks = [int(input()) for _ in range(t)]
    n = max(tasks)
    
    dp = [0 for _ in range(n + 1)]
    d = [0 for _ in range(n + 1)]

    dp[0] = 0
    dp[1] = 2
    d[0] = 0
    d[1] = 1

    for i in range(n + 1):
        sm = 0
        sd = 0
        for j in range(1, i):
            sd += d[j] + d[i - j]           
            sm += dp[j] + dp[i - j]
        d[i] = sd + 1
        sm += 2*d[i] + 1
        dp[i] = sm
    print(d)

    for t in tasks:
        print(dp[t])

task()
