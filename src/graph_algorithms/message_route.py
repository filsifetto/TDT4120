from collections import deque
 
def task():
    n, m = map(int, input().split())
 
    graph = dict()
 
    for i in range(m):
        a, b = map(int, input().split())
 
        graph[a] = graph.get(a, list()) + [b]
        graph[b] = graph.get(b, list()) + [a]
 
    def bfs(start):
        queue = deque()
        queue.append((start, [start]))
        visited = [False for _ in range(n + 1)]
        visited[start] = True
 
        while queue:
            current, path= queue.popleft()
            if current == n:
                return path
            for node in graph.get(current, list()):
                if not visited[node]:
                    visited[node] = True
                    queue.append((node, path + [node]))
        return False
    
    path = bfs(1)
    if path:
        print(len(path))
        for n in path: print(n, end= " ")
    else:
        print("IMPOSSIBLE")
 
task()

