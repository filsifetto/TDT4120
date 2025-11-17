import sys
sys.setrecursionlimit(10**6)
def task():
    n, m = map(int, input().split())
    graph = dict()
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, list()) + [b]
 
    def topological_sort():
        visited = [False for _ in range(n + 1)]
        top_sort = list()
 
        def dfs(start):
            visited[start] = True
            for k in graph.get(start, list()):
                if not visited[k]:
                    dfs(k)
            top_sort.append(start)
        
        for i in range(1, n + 1):
            if not visited[i]:
                dfs(i)
 
        return top_sort[::-1]
 
 
    count = [0 for _ in range(n + 1)]
    count[1] = 1
    
    for i in topological_sort():
        for k in graph.get(i, list()):
            count[k] += count[i]
 
    print(count[n]%(10**9 + 7))
task()
