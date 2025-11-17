n = int(input())
A = list(map(int, input().split()))
 
sm = sum(A)
 
print((n**2 + n)//2 - sm)

