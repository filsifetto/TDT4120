from collections import deque
def task():
    n = int(input())
    graph = dict()
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, list()) + [b]
        graph[b] = graph.get(b, list()) + [a]
 
    def bfs(start):
        queue = deque()
        visited = [False for _ in range(n + 1)]
        queue.append((start, 0))
        visited[start] = True
        
        max_dist = 0
        max_node = -1
        while queue:
            a, distance = queue.popleft()
            if distance > max_dist:
                max_dist = distance
                max_node = a
            for b in graph.get(a, list()):
                if not visited[b]:
                    visited[b] = True
                    queue.append((b, distance + 1))
 
        return max_dist, max_node
 
    max_dist, nodeee = bfs(1)
    max_dist, node = bfs(nodeee)
    print(max_dist)
 
task()

