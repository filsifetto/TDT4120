import sys
sys.setrecursionlimit(10**6)
def task():
    n, m = map(int, input().split())
    graph = dict()
 
    for i in range(m):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, list()) + [b]
 
    top_sort = list()
    visited = [0 for _ in range(n + 1)]
 
    def dfs(start):     
        visited[start] = 1
        for n in graph.get(start, list()):
            if visited[n] == 1:
                return False
            if visited[n] == 0:
                if not dfs(n):
                    return False
        visited[start] = 2
        top_sort.append(start)
        return True
 
    for n in range(1, n + 1):
        if not visited[n]:
            if not dfs(n):
                print("IMPOSSIBLE")
                return
 
    print(" ".join(map(str, top_sort[::-1])))
 
task()

