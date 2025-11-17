n = int(input())
 
for _ in range(n):
    a, b = map(int, input().split())
    if a > 2*b or 2*a < b:
        print("NO")
    elif (a + b)%3 == 0:
        print("YES")
    else: print("NO")

