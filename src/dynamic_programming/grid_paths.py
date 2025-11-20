def task():
    n = int(input())
    graph = list()
    for _ in range(n):
        graph.append(list(map(lambda c : True if c == "." else False, input())))

    dp = [[0 for _ in range(n)] for i in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                try:
                    dp[i + 1][j] = (dp[i + 1][j] + dp[i][j])%(10**9 + 7)
                except Exception as e:
                    pass
                try:
                    dp[i][j + 1] = (dp[i][j + 1] + dp[i][j])%(10**9 + 7)
                except:
                    pass

    if graph[n - 1][n - 1]:
        print(dp[n - 1][n - 1])
    else:
        print(0)

task()
