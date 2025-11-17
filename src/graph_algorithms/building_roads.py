class UnionFind:
    def __init__(self, nodes):
        self.parent = [i for i in range(nodes)]
        pass
 
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
 
        if root_x == root_y:
            return False
        self.parent[root_x] = root_y
        return True 
 
 
def task():
    n, m = map(int, input().split())
    uf = UnionFind(n)
    root = -1
    for i in range(m):
        a, b = map(int, input().split())
        root = a
        uf.union(a - 1, b - 1)
    
    count = 0
    edges_added = list()
    
    for i in range(n):
        if uf.find(i) != uf.find(root):
            count += 1
            edges_added.append((i + 1, root + 1))
            uf.union(i, root)
 
    print(count)
    for a, b in edges_added:
        print(a, b)
 
 
# def task():
#     n, m = map(int, input().split())
 
#     included = set()
#     count = 0
#     edges_added = list()
#     root = -1
 
#     for _ in range(m):
#         a, b = map(int, input().split())
#         root = a
#         included.add(a - 1)
#         included.add(b - 1)
 
#     for i in range(n):
#         if i in included:
#             continue
#         else:
#             count += 1
#             edges_added.append((root, i))
#             included.add(i)
        
#     print(edges_added)
 
 
task()

