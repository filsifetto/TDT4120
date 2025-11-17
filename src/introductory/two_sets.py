n = int(input())
 
if n%4 == 0:
    print("YES")
    print(n//2)
    print(1, 4, end=" ")
    for i in range(5, n + 1, 4):
        print(i, i + 3, end=" ")
        print()
    print(n//2)
    print(2, 3, end=" ")
    for i in range(6, n + 1, 4):
        print(i, i + 1, end=" ")
    print()
 
elif n%4 == 3:
    print("YES")
    print(n//2 + 1)
    print(1, 2, end=" ")
    for i in range(4, n + 1, 4):
        print(i, i + 3, end=" ")
        print()
    print(n//2)
    print(3, end=" ")
    for i in range(5, n + 1, 4):
        print(i, i + 1, end=" ")
    print()
 
else:
    print("NO")

