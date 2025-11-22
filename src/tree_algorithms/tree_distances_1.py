from collections import deque
def task():
    n = int(input())
    graph = dict()
    for _ in range(n - 1):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, list()) + [b]
        graph[b] = graph.get(b, list()) + [a]
        
    def bfs(start):
        max_dist = 0

        queue = deque()
        queue.append((start, 0))
        visited = [False for _ in range(n + 1)]
        while queue:
            node, dist = queue.popleft()
            max_dist = max(dist, max_dist)
            for neighbour in graph.get(node):
                if not visited[neighbour]:
                    visited[neighbour] = True
                    queue.append((neighbour, dist + 1))
        return max_dist

    for i in range(1, n + 1):
        print(bfs(i))
task()
