from math import inf
from collections import deque
def task():
    n, m, k = map(int, input().split())
    graph = dict()
    res = dict()
    for i in range(n + m + 2):
        res[i] = dict()
    for _ in range(k):
        a, b = map(int, input().split())
        b += n
        graph[a] = graph.get(a, list()) + [b]
        res[a][b] = 1
        res[b][a] = 0
    for i in range(1, n + 1):
        graph[0] = graph.get(0, list()) + [i]
        res[0][i] = 1
        res[i][0] = 0
    for i in range(n + 1, n + m + 1):
        graph[i] = graph.get(i, list()) + [n + m + 1]
        res[i][n + m + 1] = 1
        res[n + m + 1][i] = 0
 
    def edmonds_karp():
        def find_augmenting_path_bfs():
            queue = deque()
            queue.append((0, [0], 1))
            visited = dict()
            while queue:
                current, path, bn_val = queue.popleft()
                if current == n + m + 1: #sink
                    return path, bn_val                    
                for b in res[current]:
                    if not visited.get((current, b), False) and res[current][b] > 0:
                        visited[(current, b)] = True
                        visited[(b, current)] = True
                        queue.append((b, path + [b], min(bn_val, res[current][b])))
            return False, False
        while True:
            path, bn_val = find_augmenting_path_bfs()
            if not path:
                return
            for i in range(len(path) - 1):
                a, b = path[i], path[i + 1]
                res[a][b] -= bn_val
                res[b][a] += bn_val
 
    edmonds_karp()
    buffer = list()
    for boy in range(1, n + 1):
        for girl in graph.get(boy, list()):
            if res[girl][boy]:
                buffer.append((boy, girl - n))
    buffer = list(set(buffer))
    print(len(buffer))
    for boy, girl in buffer:
        print(boy, girl)
        
 
 
task()

