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
    edges = list()
    for _ in range(m):


