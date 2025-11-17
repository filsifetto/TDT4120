n = int(input())
 
def find(y, x):
    level = max(x, y)
 
    if level%2 == 0:
        print(level**2 - (x - 1) - (level - y))
    else:
        print(level**2 - (y - 1)  - (level - x))
 
for i in range(n):
    y, x = map(int, input().split())
    find(y, x)

