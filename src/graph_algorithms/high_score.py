from collections import deque
from math import inf
def task():
    n, m = map(int, input().split())
 
    graph = dict()
 
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a] = graph.get(a, list()) + [(b, w)]
 
    distance = [-inf for _ in range(n + 1)] 
    distance[1] = 0
 
    for _ in range(n):
        for a in range(1, n + 1):
            if distance[a] == -inf:
                continue
            else:
                for b, w in graph.get(a, list()):
                    distance[b] = max(distance[b], distance[a] + w)
    flagged = list()
    for a in range(1, n + 1):
        if distance[a] == -inf:
            continue
        else:
            for b, w in graph.get(a, list()):
                if distance[b] < distance[a] + w:
                    flagged.append(b) 
                    distance[b] = distance[a] + w
 
    visited = [False for _ in range(n + 1)]
    def bfs(start):
        queue = deque()
 
        queue.append(start)
        visited[start] = True
 
        while queue:
            current = queue.popleft()
            if current == n:
                return True
            for b, w in graph.get(current, list()):
                if not visited[b]:
                    visited[b] = True
                    queue.append(b)
    
    for i in flagged:
        if not visited[i]:
            if bfs(i):
                print(-1)
                return
    print(distance[n])
 
task()

