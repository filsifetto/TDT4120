from math import inf
def task():
    n, m, q = map(int, input().split())
    graph = dict()
 
    fw = [[inf for _ in range(n + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        fw[i][i] = 0
    
    for _ in range(m):
        a, b, w = map(int, input().split())
        fw[a][b] = w
        fw[b][a] = w
    queries = list()
    for _ in range(q):
        a, b = map(int, input().split())
        queries.append((a, b))
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            for k in range(1, n + 1):
                fw[j][k] = min(fw[j][k], fw[j][i] + fw[i][k])
 
    for a, b in queries:
        dist = fw[a][b]
        print(dist) if dist != inf else print(-1)
task()

