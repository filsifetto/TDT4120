n = int(input())
 
def permute(n):
    if n == 1:
        print(1)
    elif n <= 3:
        print("NO SOLUTION")
    else:
        for j in range(2, n + 1, 2):
            print(j)
        for i in range(1, n + 1, 2):
            print(i)
 
permute(n)

